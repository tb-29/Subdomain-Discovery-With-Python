# Subdomain-Discovery-With-Python
A Python script to discover subdomains for domains listed in a text file using Sublist3r. Supports multi-threading for faster scans and saves results in separate files. Perfect for security researchers and bug hunters looking for efficient subdomain enumeration.

pip install -r requirements.txt

python3 subdomain_discovery.py

This Python script uses Sublist3r to discover subdomains and creates a text file with the main domain’s name. The script processes a list of domains, performs subdomain enumeration for each, and saves the results in individual text files named after the main domain.
