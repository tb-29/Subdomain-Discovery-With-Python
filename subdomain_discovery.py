import os
import subprocess

def find_subdomains(domain, output_file, threads):
    # Constructing the Sublist3r command
    command = f"sublist3r -d {domain} -o {output_file}"

    # Add thread option if greater than 0
    if threads > 0:
        command = f"sublist3r -d {domain} -t {threads} -o {output_file}"

    subprocess.run(command, shell=True)

def main():
    # User input for file path and number of threads
    input_file = input("Enter the path to the main domain list file: ")
    threads_input = input("Enter the number of threads (0 for single process): ")

    # Default thread count is 0 (single process)
    threads = 0
    if threads_input.strip().isdigit():
        threads = int(threads_input.strip())

    # Check if the file exists
    if not os.path.isfile(input_file):
        print("File not found. Please provide a valid file path.")
        return

    # Read the file and process each domain
    with open(input_file, 'r') as file:
        domains = file.read().splitlines()

    for domain in domains:
        # Clean the domain of http:// or https:// prefixes
        domain = domain.replace("http://", "").replace("https://", "")
        
        # Define the output file for subdomains
        output_file = f"{domain}_subdomains.txt"
        
        # Start subdomain discovery
        print(f"Discovering subdomains for {domain}...")
        find_subdomains(domain, output_file, threads)
        print(f"Subdomains for {domain} have been saved to {output_file}.")

if __name__ == "__main__":
    main()
