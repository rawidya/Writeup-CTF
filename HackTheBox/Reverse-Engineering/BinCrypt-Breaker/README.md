# HTB Challenge: BinCrypt-Breaker

## 📝 Challenge Summary
**BinCrypt-Breaker** is a multi-stage challenge. It starts with a "loader" binary that decrypts and executes a secondary binary directly in memory. To solve it, you must first extract the hidden binary and then reverse-engineer its internal flag-checking logic.

---

## 🔎 Step-by-Step Analysis

### Stage 1: The Loader
The provided `checker` executable reads an encrypted file `file.bin`. Investigating the `decrypt` function in the loader reveals a simple **XOR** cipher with the key `0xAB`. 

The loader uses `memfd_create` and `fexecve` to run the result without saving it to disk. We can replicate this by XORing `file.bin` with `0xAB` and saving it as a new file.

### Stage 2: The Hidden Executable
Running the decrypted binary prompts for a flag. Opening this new file in a disassembler (IDA/Ghidra) reveals the validation routine. The logic involves:
1.  **Permutations**: Swapping character positions according to a fixed table.
2.  **Transformations**: Applying mathematical operations (like XOR or ADD) to the permuted characters.
3.  **Comparison**: Checking the result against a hardcoded byte array.

To solve it, you must work backward from the comparison array, reversing the transformations and finally reversing the character permutations to recover the original flag.

---

## 🛠️ Tools Used
- **IDA Pro / Ghidra**: For static analysis of both the loader and the payload.
- **Python**: To write the initial XOR extractor and the final flag reconstructor.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
