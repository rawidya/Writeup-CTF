# HTB Challenge: Maze

## 📝 Challenge Summary
**Maze** is a multi-stage reverse engineering task. It starts as a PyInstaller-packed executable that protects an encrypted archive. The challenge involves correctly unpacking the Python environment, deobfuscating hidden logic, and ultimately reversing a native ELF binary to find the flag-building algorithm.

---

## 🔎 Step-by-Step Analysis

### 1. Unpacking the Executable
The provided `maze.exe` is a PyInstaller bundle. Use `pyinstxtractor` to unpack it.
**Critical**: Use **Python 3.8** for extraction to avoid unmarshalling errors.
```bash
python3.8 pyinstxtractor.py maze.exe
```

### 2. Deobfuscating Python Logic
After extraction, you'll find `.pyc` files. Decompile them (e.g., using `uncompyle6` or `pycdc`). One file, `obf_path.pyc`, contains the real key generation logic. It uses the `maze.png` file as a source for a seed to generate the decryption key for `enc_maze.zip`.

### 3. Native Binary Reversing
Unzipping the archive reveals an ELF binary. Open it in a disassembler. The binary contains an array of numbers and a transformation function.
- **Algorithm**: The binary performs a series of XOR and shift operations on the array.
- **Goal**: Reverse these operations or implement the logic in a Python script to reconstruct the flag.

---

## 🛠️ Tools Used
- **Pyinstxtractor**: To unpack the PyInstaller bundle.
- **Python 3.8**: Required for correct extraction.
- **uncompyle6 / pycdc**: To decompile `.pyc` files.
- **Ghidra / IDA Pro**: To analyze the native ELF binary.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
