# HTB Write-up: Nostalgia

## 📝 Challenge Summary
**Nostalgia** is a Game Boy Advance (GBA) reverse engineering challenge. We are provided with a ROM (`Nostalgia.gba`) that prompts for a cheat code. To solve it, we must analyze the ARM-based binary and patch the validation logic to force a "correct" result.

---

## 🔎 Recon (Emulation & Disassembly)
Running the ROM in `mGBA` reveals a simple input screen. Pressing **Start** submits the code, but without the correct sequence, nothing happens.

### Loading into IDA Pro
To analyze GBA ROMs, the processor type must be set to **ARM:LE:32:v4T**.
Static analysis points to `sub_15A8` as the handler for user input. At address **`0x1638`**, we find the critical decision point:
`ROM:00001638   BNE   loc_161E`
This `BNE` (Branch if Not Equal) instruction redirects the execution to a failure block if the cheat code comparison fails.

---

## ⚙️ Strategy: Inverting the Logic
Instead of searching for the complex cheat code in memory, we can simply patch the binary to accept *any* input.

### Identifying the Patch
- **Instruction**: `BNE` (Branch if Not Equal)
- **Opcode**: `D1`
- **Target**: `BEQ` (Branch if Equal)
- **Opcode**: `D0`

By changing the byte at `0x1638` from **`D1`** to **`D0`**, the program will now branch to the success state for every "wrong" code we enter.

---

## 🚀 Execution
1.  Open the ROM in a hex editor or use IDA's "Patch program" feature.
2.  Navigate to offset `0x1638`.
3.  Change the byte value from `D1` to `D0`.
4.  Apply the patch and save the new `.gba` file.
5.  Launch the patched ROM, enter any code (or none), and press Start.

---

## ✅ Result
The game accepts the code and displays the flag on the simulated screen.
**Flag**: `HTB{...}` (transcribed from the emulator).

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
