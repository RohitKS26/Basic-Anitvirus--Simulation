# Basic Antivirus Simulation

## Description
This project is a simple antivirus simulation developed using Python. 
It demonstrates the concept of signature-based malware detection by generating file hashes and comparing them with known malicious signatures.

## How It Works
- Scans files in a specified folder
- Generates SHA-256 hash for each file
- Compares hashes with a database of known malware signatures
- Flags and moves detected malicious files to a quarantine folder

## Technologies Used
- Python
- File Handling
- SHA-256 Hashing
- Signature-Based Malware Detection

## How to Run
1. Place files to scan inside the 'scan_folder'
2. Run the script: python antivirus.py
3. View scan results in the terminal

## Note
This is a basic educational project and not intended for real-world antivirus use.
