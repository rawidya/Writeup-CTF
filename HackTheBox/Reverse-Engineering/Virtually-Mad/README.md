# HTB Write-up: Virtually Mad

## 📝 Challenge Summary
**Virtually Mad** is a low-level reverse engineering challenge featuring a custom Virtual Machine (VM). The binary reads a hexadecimal string from the user, interprets it as a series of 32-bit instructions, and executes them. To win, you must provide exactly 5 instructions that manipulate the VM registers into a specific target state while observing immediate-value constraints.

---

## 🔎 Recon (VM Architecture)
The 15KB binary implements a simple stackless VM with the following components:

### Registers & Flags
- `v8[0-3]`: Registers A, B, C, and D.
- `v8[12]`: Comparisons Flag (The high bit `0x10000000` is set on a successful comparison).

### Instruction Format (32-bit)
Instructions are parsed as follows:
- **Bits 24-31**: Opcode (e.g., `01`=MOV, `02`=ADD, `03`=SUB, `04`=CMP).
- **Bits 20-23**: Integrity Bit (Must be set to `1`).
- **Bits 16-19**: Destination Register (0-3).
- **Bits 12-15**: Mode (0 for Immediate value, 1 for Register source).
- **Bits 0-11**: Operand Value / Source Register.

**Critical Constraint**: The immediate value (bits 0-11) cannot exceed **256 (`0x100`)**.

---

## ⚙️ Strategy & Assembler Logic
We must reach the state: `A=512, B=-1, C=-1, D=0, Flag=True` in exactly 5 steps.

### Instruction 1 & 2: Building 512 in Register A
Since the max immediate value is 256, we use two additions:
- `ADD A, 256` -> `ADD A, 256`.
- Hex Calculation: `02` (Opcode) | `1` (Valid) | `0` (Dest A) | `0` (Mode Imm) | `100` (Val) = `02100100`.

### Instruction 3: Underflow to -1 in Register B
By subtracting 1 from the initial 0, we trigger an integer underflow:
- `SUB B, 1`.
- Hex Calculation: `03` (Opcode) | `1` (Valid) | `1` (Dest B) | `0` (Mode Imm) | `001` (Val) = `03110001`.

### Instruction 4: Copying Register B to C
We cannot move -1 directly because `0xFFFFFFFF` exceeds the 256 limit. Instead, we copy the current value of Register B to C:
- `MOV C, Register B`.
- Hex Calculation: `01` (Opcode) | `1` (Valid) | `2` (Dest C) | `1` (Mode Reg) | `100` (Source B) = `01121100`.

### Instruction 5: Setting the Comparison Flag
Finally, we compare Register D (already 0) with a value to set the flag:
- `CMP D, 0`.
- Hex Calculation: `04` (Opcode) | `1` (Valid) | `3` (Dest D) | `0` (Mode Imm) | `000` (Val) = `04130000`.

---

## ✅ Result
Concatenating the 5 instructions:
**Input Payload**: `0210010002100100031100010112110004130000`
**Flag**: `HTB{0210010002100100031100010112110004130000}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
