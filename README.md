# 🔒 File Integrity Checker

This Python script helps verify whether a file has been tampered with or remains intact using cryptographic hash functions like SHA256.

## 💡 How It Works

- It calculates a file’s hash using `hashlib`.
- You can save the hash of a clean file.
- Later, you can verify if the file was modified by comparing with the saved hash.

## 📌 Features

- Generate hash of any file
- Check file integrity
- Uses built-in Python libraries only

## 🛠️ Requirements

- Python 3.x
- No external dependencies

## ▶️ Usage

1. Run the script:
   ```
   python file_integrity_checker.py
   ```

2. Enter the file path and choose one of the options:
   - `1` to generate hash
   - `2` to verify integrity

## 🧪 Sample

**Generating Hash**
```
Enter the path of the file: report.pdf
Enter hashing algorithm (default: sha256):
Choose option (1 or 2): 1
Generated hash:
e4f1c9fddf5...a5bc
```

**Verifying File**
```
Choose option (1 or 2): 2
Enter the original hash value: e4f1c9fddf5...a5bc
[✓] File is intact. No changes found.
```

---

### 📁 Author

This script is part of an internship project on file security and integrity checking using Python.