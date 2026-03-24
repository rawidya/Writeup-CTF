# HTB Challenge: Not-Posixtive

## 📝 Challenge Summary
**Not-Posixtive** is a Python-based sandbox challenge that exploits a unique collision in Python's hashing mechanism. The goal is to provide two different inputs that produce the same hash value while bypassing strict character filters.

---

## 🔎 Step-by-Step Analysis

### 1. The Hash Collision
The server validates your inputs using the following condition:
`debug[0] != debug[1] and hash(debug[0]) == hash(debug[1])`
In Python, integers are hashed to themselves (e.g., `hash(5) == 5`). However, there is a legendary exception: **`hash(-1)` and `hash(-2)` both return `-2`**. 

### 2. Generating -1 and -2
The server calculates its values based on the return code of a binary times a "mode".
`Result = ExitCode * Mode`
To get -1 and -2, we need:
1.  **Mode = -1**
2.  **ExitCode 1 and ExitCode 2**

### 3. Bypassing the "Mode" Filter
The mode input forbids the minus sign `-`. In Python, you can use the bitwise NOT operator **`~`** to get -1.
`~0` in Python evaluates to `-1`.

### 4. Exploiting `grep` Exit Codes
We use the `grep` binary (4 letters) to generate the exit codes:
- **Exit Code 1**: Run `grep` with a pattern that doesn't match a file (`grep NOMATCH server.py`).
- **Exit Code 2**: Run `grep` against a non-existent file (`grep ANY fakefile`).

### 5. Winning the Challenge
By combining `Mode = ~0` and the two `grep` commands, we satisfy the `hash(z1) == hash(z2)` condition and retrieve the flag.

---

## 🛠️ Tools Used
- **Python Internal Research**: Understanding the `hash(-1)` implementation.
- **Linux Exit Codes**: Utilizing standard binary behaviors for control.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
