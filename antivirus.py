import hashlib
import os
import shutil


SCAN_FOLDER = "scan_folder"
QUARANTINE_FOLDER = "quarantine"


os.makedirs(QUARANTINE_FOLDER, exist_ok=True)

def load_signatures():
    with open("signatures.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_files():
    signatures = load_signatures()

    for file in os.listdir(SCAN_FOLDER):
        file_path = os.path.join(SCAN_FOLDER, file)

        if os.path.isfile(file_path):
            file_hash = calculate_hash(file_path)

            if file_hash in signatures:
                print(f"[ALERT] Malicious file detected: {file}")
                shutil.move(file_path, os.path.join(QUARANTINE_FOLDER, file))
            else:
                print(f"[OK] File is clean: {file}")

if __name__ == "__main__":
    scan_files()
