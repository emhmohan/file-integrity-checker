# file_integrity_checker.py

import hashlib
import os

# Function to generate the hash value of a file
def generate_file_hash(filepath, algorithm='sha256'):
    try:
        hash_func = getattr(hashlib, algorithm)()
        with open(filepath, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")
    except Exception as e:
        print(f"[!] Error: {e}")

# Function to compare hash values and verify integrity
def verify_file(filepath, original_hash, algorithm='sha256'):
    current_hash = generate_file_hash(filepath, algorithm)
    if not current_hash:
        return False

    if current_hash == original_hash:
        print("[✓] File is intact. No changes found.")
        return True
    else:
        print("[✗] WARNING: File has been changed!")
        return False

# Main driver
if __name__ == "__main__":
    print("==== FILE INTEGRITY CHECKER ====")
    path = input("Enter the path of the file: ")
    algo = input("Enter hashing algorithm (default: sha256): ") or "sha256"
    
    print("\n1. Generate file hash")
    print("2. Verify file integrity\n")
    option = input("Choose option (1 or 2): ")

    if option == '1':
        result = generate_file_hash(path, algo)
        if result:
            print(f"\nGenerated hash:\n{result}")
    elif option == '2':
        ref_hash = input("Enter the original hash value: ")
        verify_file(path, ref_hash, algo)
    else:
        print("[!] Invalid option.")