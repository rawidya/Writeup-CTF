# HTB Challenge: Hexecution

## 📝 Challenge Summary
**Hexecution** features a custom assembly language ("Recipe") and a runner ("Cook"). The logic involves a character shuffling algorithm that must be reversed to obtain the flag. This challenge tests your ability to map abstract instructions to standard programming concepts.

---

## 🔎 Step-by-Step Analysis

### 1. Mapping the Custom ISA
The `recipe.asm` uses a custom set of opcodes. Here is the mapping to standard operations:
- `AES256`: Print character.
- `BOIL`: MOV (Set value).
- `SPELL`: Read input.
- `GOODBYE / WINDOW`: Load / Store to memory.
- `LADDER`: Jump / Comparison.

### 2. Identifying the Shuffle
The input is processed in 4-byte blocks. The `GOODBYE` and `WINDOW` sequence reveals a fixed permutation:
- Original order: `[0, 1, 2, 3]`
- Shuffled order: `[2, 1, 3, 0]`

### 3. Reconstructing the Comparison
The binary contains an "encrypted" string: `5maNcI4__U10_de5L13_Mn4U0u4trfn_`.
The `LADDER` instructions check specific indices of the shuffled input against this string. By following the indices, you can reconstruct how the shuffled flag should look in memory.

### 4. Reversing the Shuffle
Take the reconstructed shuffled string and apply the inverse permutation (`[3, 1, 0, 2]`) to every 4-character block to recover the original flag.

---

## 🛠️ Tools Used
- **Text Editor**: To analyze the `recipe.asm` file.
- **Manual Mapping**: No complex reversing tools needed if the logic is mapped correctly.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
