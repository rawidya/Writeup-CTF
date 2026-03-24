# HTB Challenge: Virtually-Mad

## 📝 Challenge Summary
**Virtually-Mad** involves a custom-built Virtual Machine (VM) implemented in a small Linux binary. The program accepts a hexadecimal string as a set of 5 instructions. You must craft these instructions to manipulate the VM's internal register state to match a specific "winning" condition.

---

## 🔎 Step-by-Step Analysis

### 1. Understanding the VM Architecture
The VM uses 32-bit instructions with a fixed format:
- **Opcode**: Action to perform (MOV, ADD, SUB, CMP).
- **Destination**: The target register (A, B, C, or D).
- **Operand Type**: Whether the source is a constant (Immediate) or another register.
- **Value**: The constant or the source register index.

### 2. Constraints & Goal
- **Constraints**: Immediate values cannot exceed `0x100`. You must use exactly 5 instructions.
- **Winning Condition**: 
  - Register A = `512`
  - Register B = `-1`
  - Register C = `-1`
  - Register D = `0`
  - Comparison Flag = `Set`

### 3. Crafting the Instructions
Since we can't set A to 512 directly (max 256), we must add:
1. `ADD A, 256`
2. `ADD A, 256` -> A is now 512.

To get -1 in B (starts at 0):
3. `SUB B, 1` -> B is now -1 (underflow).

To get -1 in C (can't use immediate):
4. `MOV C, B (Register Mode)` -> C is now -1.

To set the flag:
5. `CMP D, 0` -> Since D is 0, the comparison flag is set.

### 4. Converting to Hex
Convert each instruction into the 32-bit hex format based on the bitmask identified during analysis. The final string is the concatenated hex codes.

---

## 🛠️ Tools Used
- **IDA Pro / Ghidra**: To reverse engineering the instruction decoder and the opcodes.
- **Hex Converter**: To manually assemble the 32-bit instructions.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
