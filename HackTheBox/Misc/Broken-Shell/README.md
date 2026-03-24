# HTB Write-up: Broken Shell

## 📝 Challenge Summary
**Broken Shell** is a restricted "Bash Jail" escape challenge. The environment allows only a minimal set of symbols and numbers, strictly forbidding all alphabetical characters. To solve it, we must use wildcard expansion and shell function parameters to execute commands blind.

---

## 🔎 Recon (The Restricted Environment)
The allowed character set is: `^[0-9${}/?\"[:space:]:&>_=()]+$`.
- Without letters, we cannot type `cat /flag.txt`.
- We can use **`/`** to navigate paths and **`?`** as a single-character wildcard.

The core technique relies on the fact that `/???/???` can expand to `/bin/cat` (if `cat` is the 3rd alphabetically matching 3-letter binary in `/bin`).

---

## ⚙️ Strategy: Wildcard Function Expansion
Alphabetical expansion is unpredictable. To gain control, we define a shell function and use its positional parameters.

### 1. Defining the Runner
We define a function `_` that executes its 7th parameter (`$7`) in the background:
`_(){ $7& }`
When we call `_ /???/??`, the shell expands the wildcard *before* passing it to the function. `/???/??` matches 2-letter binaries in `/bin` (like `cp, dd, df, du, id, ln, ls`).
- In many Linux distributions, **`ls`** is the 7th match.

### 2. Identifying the Flag
Executing `_(){ $7& } && _ /???/??` lists the current directory. We find a file named `this_is_the_flag_gg` (19 characters).

### 3. Reading the Flag
We repeat the process for **`cat`** (a 3-letter binary in `/bin/???/???`).
- `cat` is typically the 3rd match.
- We use 19 question marks (`?`) as the argument for the flag filename.

---

## 🚀 Final Payload
The final injection string:
`_(){ $3 ???????????????????& } && _ /???/???`
This expands to `cat this_is_the_flag_gg` and prints the contents.

---

## ✅ Result
The flag is revealed in the shell output.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
