# HTB Write-up: Maze

## 📝 Challenge Summary
**Maze** is a multi-layered reverse engineering challenge. You are given a PyInstaller executable (`maze.exe`), an encrypted image (`maze.png`), and a password-protected ZIP archive (`enc_maze.zip`). The journey involves unpacking Python bytecode, deobfuscating key generation logic, and finally reversing a recurrence relation in a custom ELF binary.

---

## 🔎 Recon (Deconstructing the Entry Point)
Initial inspection of `maze.exe` reveals it is a PyInstaller wrapper. We use `pyinstxtractor` to unpack the contents.

### The Python 3.8 Trap
A critical realization is that the executable was built with **Python 3.8**. Using a different version for unpacking results in a corrupted `PYZ` extraction, missing the essential `obf_path.pyc` module. Once extracted correctly, we find the primary logic in `maze.pyc`.

### Identifying the Dead End
The initial decompiled code suggests an XOR key of all zeros. Attempting to decrypt the `maze` file from the ZIP using this logic produces a corrupted ELF (Magic: `3F454C46...`). This is a classic "rabbit hole."

---

## ⚙️ Strategy: The Path Through the Maze
The real logic is hidden in `obf_path.obfuscate_route()`. By deobfuscating this module, we discover that the true XOR key is dynamically generated.

### 1. Seed Generation from Image Metadata
The program reads specific byte offsets from `maze.png` to generate a seed for Python's `random` module:
- `seed = img[4817] + img[2624] + img[2640] + img[2720]`
- This seed produces a 300-byte key used for the final XOR.

### 2. Binary Restoration
Applying the `(byte + 80) % 256` transformation followed by the dynamic XOR key restores the original ELF binary: `maze_solved.elf`.

---

## 🚀 The Final Boss: ELF Recurrence Relation
Opening the restored ELF in IDA Pro reveals an array of numbers at `0x2060`. The flag is verified by checking a mathematical relationship between every three characters:
- `target[i] = flag[i] + flag[i-1] + flag[i-2]`
- We know `flag[0-2]` is `HTB`. We can now solve for `flag[3]` and onwards using:
- **`flag[i] = target[i-2] - flag[i-1] - flag[i-2]`**

---

## ✅ Result
Running the recurrence solver produces the cleartext flag.
**Flag**: `HTB{...}` (derived from the math solver).

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
