# HTB Write-up: Hexecution

## 📝 Challenge Summary
**Hexecution** is a custom architecture/VM challenge. You are provided with a "recipe" (`recipe.asm`) and a "cook" binary. The solution requires reverse-engineering a custom set of assembly instructions to understand a character permutation algorithm and a specific validation sequence.

---

## 🔎 Recon (Custom ISA Mapping)
The `recipe.asm` file uses a made-up language. Through analysis, we map the instructions to standard operations:
- `AES256`: Print character.
- `BOIL`: Load value (`MOV`).
- `SPELL`: Read input.
- `GOODBYE / WINDOW`: Load and Store from memory.
- `LADDER`: Jump/Compare.

### The "Encrypted" Key
At offset `0x40`, the program loads a string: `5maNcI4__U10_de5L13_Mn4U0u4trfn_`. This isn't the flag, but the target comparison string that the flag must match after being processed.

---

## ⚙️ Strategy: Reversing the Kitchen
The core logic involves processing input in 4-byte blocks and applying a specific shuffle.

### 1. The Shuffle Pattern
The `GOODBYE` and `WINDOW` sequence shows the following permutation for each 4-byte block:
- **Original `[0, 1, 2, 3]` -> Shuffled `[2, 1, 3, 0]`**
- Displacement: Byte 2 moves to index 0, Byte 1 stays, Byte 3 moves to index 2, and Byte 0 moves to index 3.

### 2. Index Mapping
The `LADDER` instructions check the input at specific, non-linear indices (0, 5, 10, 15...). We map the key string `5maNcI...` to these positions to reconstruct the **shuffled flag**:
- `5U1c_mI0_4a5_deNLu4M01ntr43_Ufn_`

---

## 🚀 Exploitation Steps
To recover the original flag, we undo the shuffle for every 4-character block:
- **Reverse Map: `[0, 1, 2, 3] -> [3, 1, 0, 2]`**
1.  `5U1c` -> `cU51`
2.  `_mI0` -> `0m_I`
3.  ... and so on.

The resulting string builds the sentence: `"Custom ISA and Emulation are Fun"`.

---

## ✅ Result
Combining the unshuffled blocks gives the final flag.
**Flag**: `HTB{cU510m_I54_aNd_eMuL4t10n_4r3_fUn}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
