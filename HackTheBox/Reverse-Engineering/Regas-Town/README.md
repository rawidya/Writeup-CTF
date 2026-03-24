# HTB Challenge: Regas-Town

## 📝 Challenge Summary
**Regas-Town** presents a massive binary that seems intimidating at first. However, the true challenge is not about deep assembly reversing but about identifying the validation rules hidden within the binary's metadata.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying the Rules
By running `strings` or searching for patterns in the 19MB binary, you will find a series of **Regular Expressions (Regex)**. These regexes act as the "gatekeeper" for the flag.

Example Rules Found:
- `^.{33}$`: Length is exactly 33 characters.
- `(?:^[H][T][B]).*`: Starts with "HTB".
- `(?:.[^0-9]*\d.*){5}`: Contains exactly 5 digits.
- `.{24}T.e.T.*`: Specific characters at the end of the string.

### 2. Solving the Crossword
Instead of debugging the code, you can treat these rules like a logic puzzle. By matching the constraints:
- "HTB" + "{" + "Crossword Logic" + "}"
- Satisfying the uppercase and digit requirements.
- Filling in the gaps based on common English phrases (e.g., "The King Of The Town").

### 3. Reconstructing the Flag
Combining all the constraints reveals the string:
`HTB{Y0u_Ar3_Th3_K1ng_O7_The_Town}`

This challenge teaches that sometimes the most effective way to "reverse" is to find the data validation patterns rather than the execution flow.

---

## 🛠️ Tools Used
- **Strings**: To extract the regex patterns.
- **Regex101**: To test and understand the constraints.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
