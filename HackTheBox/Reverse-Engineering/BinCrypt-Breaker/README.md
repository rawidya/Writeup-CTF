# HTB Write-up: BinCrypt-Breaker

## 📝 Challenge Summary
**BinCrypt-Breaker** is a two-part binary exploitation challenge. You are given a loader (`checker`) and an encrypted data file (`file.bin`). To solve it, you must first decrypt the hidden executable within the data file and then reverse-engineer its complex flag-checking routine, which involves permutations and bitwise operations.

---

## 🔎 Part 1: Decrypting the Hidden Executable
Analysis of the `checker` binary in IDA Pro reveals its primary purpose: it acts as a wrapper.
1.  **Dynamic Decryption**: The loader opens `file.bin`, reads its content, and XORs every byte with the constant key **`0xAB`**.
2.  **In-Memory Execution**: The decrypted data is written to a temporary memory-backed file descriptor and executed using `fexecve`. It never touches the disk in its decrypted form.

### Extraction Script
We can replicate the decryption logic in Python to retrieve the underlying executable for deeper analysis:
```python
with open('file.bin', 'rb') as f:
    data = bytearray(f.read())
for i in range(len(data)):
    data[i] ^= 0xAB
with open('extracted_elf', 'wb') as f:
    f.write(data)
```

---

## ⚙️ Part 2: Reversing the Flag Check
The extracted ELF (`extracted_elf`) prompts for a 28-character flag (excluding `HTB{}`). The validation logic is split into several layers of transformations.

### 1. Character Swapping (Permutation)
A sub-function performs specific byte swaps between indices:
- (0, 12), (14, 26), (4, 8), and (20, 23).
Since swapping is its own inverse, we can reverse this by applying the same swaps after we recover the rest of the string.

### 2. The Main Transformation Loop
The core validation (function `sub_12E4`) processes the input in two 14-character halves. For each half, it performs:
1.  **XOR Layer**: Characters at indices `[2, 4, 6, 8, 11, 13]` are XORed with a specific key (e.g., `2` for the first half, `3` for the second).
2.  **Shuffle Layer**: A set of 8 rounds of permutations based on a hardcoded map.
    - Map: `[9, 12, 2, 10, 4, 1, 6, 3, 8, 5, 7, 11, 0, 13]`

### 3. Reversing the Shuffle
To reverse the shuffle, we calculate the **Inverse Permutation Map** and apply it 8 times to the target encrypted string.
If position `J` moves to `I`, in our reverse map, the character at `I` must move back to `J`.

---

## 🚀 Final Solver Strategy
1. Split the hardcoded encrypted string from the binary into two 14-char parts.
2. Apply the XOR-key correction.
3. Apply the 8-round inverse permutation.
4. Join the halves and apply the final character swaps.

---

## ✅ Result
Reversing the transformations reveals the original plaintext flag.
**Flag**: `HTB{...}` (derived from the decrypted buffer).

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
