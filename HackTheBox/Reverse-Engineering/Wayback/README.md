# HTB Challenge: Wayback

## 📝 Challenge Summary
**Wayback** is a time-based reverse engineering challenge. A password was generated at a specific point in time using a time-seeded random number generator. The goal is to identify the seeding formula and brute-force the timeframe to recover the password.

---

## 🔎 Step-by-Step Analysis

### 1. Analyzing the Binary
The binary `V1` uses the standard C library function `srand()` to seed the random number generator. Decompiling the `generate_password` function shows that the seed is calculated using the `time(0)` value and members of the `tm` struct (month, year, hour, etc.).

### 2. Replicating the Seed
The seed formula is:
```c
seed = (100000000 * (month + 1)) + (1410065408 * year) + (10000 * hour) + ...
```
Note that the multiplication with `1410065408` will likely overflow in a 32-bit integer, which is a key detail when replicating the logic in other languages.

### 3. Brute-Forcing the TimeWindow
The challenge description specifies that the password was generated between **December 10th and 11th, 2013**. This gives us a limited window of only 48 hours (172,800 seconds).

1.  Iterate through each second in that window.
2.  Calculate the seed for that second using the reconstructed formula.
3.  Call `srand(seed)` and then call `rand()` 20 times to generate a password candidate.
4.  Try using the candidate as an AES-CBC key to decrypt the provided data.

### 4. Speeding it Up
Since Python is slow for hundreds of thousands of operations, a C-based solver or using `ctypes` to call `libc` is recommended to achieve the result in seconds.

---

## 🛠️ Tools Used
- **IDA Pro / Ghidra**: To reverse the seed formula.
- **C/Python**: To implement the brute-force solver.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
