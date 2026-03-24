# HTB Challenge: Nostalgia

## 📝 Challenge Summary
**Nostalgia** is a Game Boy Advance (GBA) reverse engineering challenge. You are provided with a `.gba` ROM file that requires a secret "cheat code" to reveal the flag. The goal is to disassemble the ROM and patch the validation logic.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying the Architecture
GBA ROMs run on ARM processors. To analyze it correctly, you must use a disassembler (like IDA Pro or Ghidra) set to **ARM:LE:32:v4T**.

### 2. Locating the Validation Logic
By analyzing the cross-references and the game loop, you can find the function responsible for checking the user input (cheat code). At address `0x1638`, there is a conditional branch:
`BNE loc_161E` (Branch if Not Equal).
This branch triggers if the entered code is incorrect, preventing the flag from appearing.

### 3. Patching the Branch
To bypass the check, you can invert the logic. Changing `BNE` to `BEQ` (Branch if Equal) tells the game to follow the "correct code" path when the input is actually incorrect.
- **Original Bytes**: `F1 D1` (`BNE`)
- **Patched Bytes**: `F1 D0` (`BEQ`)

### 4. Verification
After applying the patch and saving the modified ROM, open it in an emulator (like mGBA). Pressing the Start button without entering a code will now bypass the validation and display the flag.

---

## 🛠️ Tools Used
- **IDA Pro**: For ARM disassembly and binary patching.
- **mGBA**: To run and verify the patched ROM.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
