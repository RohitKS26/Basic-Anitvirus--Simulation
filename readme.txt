Basic Antivirus Simulation Project

Description:
This project is a simple antivirus simulation created using Python.
It demonstrates how signature-based malware detection works by
calculating file hashes and comparing them with known signatures.

How it works:
- The program scans files in a specified folder.
- It calculates the SHA256 hash of each file.
- If the hash matches a known malware signature, the file is flagged.
- Detected files are moved to a quarantine folder.

Tools and Concepts Used:
- Python
- File handling
- SHA256 hashing
- Signature-based malware detection

How to run:
1. Place files to scan inside the 'scan_folder'.
2. Run the script using: python antivirus.py
3. The program will display scan results in the terminal.

Note:
This is a basic educational project and not a real antivirus software.
