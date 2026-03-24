# HTB Write-up: Rega's Town

## 📝 Challenge Summary
**Rega's Town** is a unique reverse engineering challenge where the primary obstacle isn't the code complexity, but the sheer volume of data. The provided 19MB binary hides its secrets behind a series of complex validation rules. Instead of deep debugging, the solution lies in treating the challenge as a logic puzzle by analyzing the embedded strings.

---

## 🔎 Recon (Finding the Rules)
Initial analysis of the `strings` output from the 19MB binary reveals a series of sophisticated Regular Expressions (Regex). These expressions define the exact structure, character set, and content requirements for a valid flag.

### The Logic Constraints
Key Regex patterns discovered:
- `^.{33}$`: The flag is exactly 33 characters.
- `HTB{...}`: Standard wrapper format.
- `^[[:upper:]]{3}.[[:upper:]].{3}[[:upper:]].{3}...`: Specific positions must be uppercase.
- `.{24}\\x54.\\x65.\\x54.*`: Fixed characters at specific offsets (T, e, T).
- `(?:.[^0-9]*\\d.*){5}`: Exactly 5 digits must be present in the string.
- `_[[:upper:]]\\dn[a-h]_`: A specific 4-character word structure (e.g., K1ng).

---

## ⚙️ Strategy: Solving the Puzzle
Since the binary acts as a massive validator for these rules, we can manually reconstruct the flag like a crossword puzzle.

### Building the String
1.  **Structure**: `HTB{___________________________}`
2.  **Sentence Analysis**: The uppercase rules and fixed letters suggest a theme: `"You Are The [Word] Of The Town"`.
3.  **Applying Leet-Speak**:
    - "You" -> **Y0u** (Satisfies the digit and uppercase rules).
    - "Are" -> **Ar3** (Satisfies the 5th digit requirement elsewhere).
    - "The" -> **Th3**.
    - "King" -> **K1ng** (Fits the `[Upper][Digit]n[a-h]` pattern).
    - "Of" -> **O7** (Fits the `_[O]\d_` constraint).

### Final Verification
Testing the string `HTB{Y0u_Ar3_Th3_K1ng_O7_The_Town}` against the rules:
- **Length**: 33 characters (Correct).
- **Digits**: 0, 3, 3, 1, 7 (Exactly 5 digits, Correct).
- **Format**: All positional uppercase and substring rules match.

---

## ✅ Result
The constructed string is the valid flag.
**Flag**: `HTB{Y0u_Ar3_Th3_K1ng_O7_The_Town}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
