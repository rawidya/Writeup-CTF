# HTB Challenge: Broken Shell

## 📝 Challenge Summary
**Broken Shell** is a Linux sandbox escape challenge (Bash Jail). The environment restricts the input to a very small set of characters and forbids the use of any letters. The goal is to bypass these restrictions to read the flag file.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying Restrictions
The allowed characters are limited to numbers, symbols like `?`, `$`, `{`, `}`, and bash operators. No letters (`a-z`, `A-Z`) are allowed.

### 2. The Wildcard Secret
In Bash, the `?` character matches any single character. While `/bin/ls` is forbidden, `/???/??` might match it. However, many files match this pattern, and the shell executes the first alphabetical match.

### 3. Using Bash Functions for Control
To pinpoint a specific command (like `ls` or `cat`), we can define a function and pass the wildcard as an argument. The shell expands the wildcard into multiple arguments (`$1`, `$2`, `$3`...). We can then execute the specific argument we want.

### 4. Exploitation
- **List Files**: `_(){ $7& } && _ /???/??` 
  - (If `ls` is the 7th match for 2-letter binaries in `/bin`).
- **Read Flag**: `_(){ $3 ???????????????????& } && _ /???/???`
  - (If `cat` is the 3rd match for 3-letter binaries, and the flag filename has 19 characters).

---

## 🛠️ Tools Used
- **Bash Wildcards**: `?` for character substitution.
- **Positional Parameters**: `$1`, `$2` to select specific results from a wildcard expansion.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
