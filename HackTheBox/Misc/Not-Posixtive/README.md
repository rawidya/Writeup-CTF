# HTB Write-up: Not Posixtive

## 📝 Challenge Summary
**Not Posixtive** is a Python-based challenge that explores a rare mathematical edge case: **the hash collision of small negative integers**. The goal is to produce two different command outputs with identical hashes while bypassing strict input filters.

---

## 🔎 Recon (The Logic Vulnerability)
The server code contains the following core check:
```python
if z1 != z2 and str(z1) != str(z2) and hash(z1) == hash(z2):
    # Success
```
In Python, integers typically return themselves as their hash. However, an intentional quirk in the CPython implementation causes **`hash(-1)`** to return **`-2`**, which is identical to the hash of **`-2`**.

This provides our collision: we need one command to return `-1` and the other to return `-2`.

---

## ⚙️ Strategy: Bypassing the Sandbox
The server restricts our input for the `mode` parameter (no signs like `-` or `+`) and the `binary` length (max 4 chars).

### 1. Reaching -1 without a Minus Sign
We use the bitwise inversion operator **`~`**. 
- **`~0`** is the equivalent of `-1`. This satisfies the character filter and the 2-character length limit.

### 2. Controlling Exit Codes with `grep`
The server calculates the result as `return_code * mode`. Using `mode = -1`, we need exit codes **1** and **2**.
- **`grep`** (4 characters) is the perfect candidate:
  - Exit code **1** occurs when a pattern is not found in a file.
  - Exit code **2** occurs when the specified file does not exist.

---

## 🚀 Exploitation Payload
We execute two separate runs:
1.  `bin=grep`, `switch=Nomatch`, `compl=server.py`, `mode=~0` -> **Result: -1**
2.  `bin=grep`, `switch=Nomatch`, `compl=fakefile`, `mode=~0` -> **Result: -2**

Since `-1 != -2` but `hash(-1) == hash(-2)`, the conditions are satisfied.

---

## ✅ Result
The hash collision is triggered, and the server prints the flag.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
