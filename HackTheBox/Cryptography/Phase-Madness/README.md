# HTB Write-up: Phase Madness

## 📝 Challenge Summary
**Phase Madness** is an advanced engineering challenge in the realm of Quantum Computing. The server encodes each byte of the flag into the rotation phases of a single qubit using one of three methods. The goal is to reconstruct the original bytes by performing specialized measurement "probes" to translate quantum phase into classical population statistics.

---

## 🔎 Recon (The Encoding Matrix)
The server encodes data based on the index `i` of each byte:
- `i % 3 == 0` -> **RX(α)**: Rotation around the X-axis.
- `i % 3 == 1` -> **RY(β)**: Rotation around the Y-axis.
- `i % 3 == 2` -> **H + RZ(γ)**: Hadamard followed by rotation around the Z-axis.

### The Measurement Problem
In the Z-basis (standard measurement), the `H + RZ(γ)` case always yields a 50/50 probability (1/2), regardless of the angle $\gamma$. This "madness" hides the data from simple observation.

---

## ⚙️ Strategy: Phase-to-Population Mapping
To recover the hidden phases, we add our own quantum gates before measurement to "interfere" with the state and reveal the angle.

### 1. Probing RX/RY
For the first two cases, the probability $P(1)$ follows the formula:
$P(1) = \sin^2(\frac{\alpha}{2})$
We can reverse this math or use a brute-force comparison of observed statistics against every possible degree (0-255).

### 2. Solving the RZ Ambiguity
For the `H + RZ` case, we apply a **$90^\circ$ RX probe** (`RX:90`). This translates the Z-phase into an observable change in the Z-basis population:
$P(1) = \frac{1}{2} - \frac{1}{2}\sin(\text{angle})$
To eliminate sign ambiguity and noise, we use a **double-probe technique** using both `RX:90` and `RX:270` ($180^\circ$ difference), allowing us to uniquely pinpoint the byte using a minimum squared error approach.

---

## 🚀 Exploitation Workflow
1.  **Connect**: Iterate through every qubit representing the flag bytes.
2.  **Measure**: Perform 1024 (or more) shots for each probe.
3.  **Heuristics**: Since the flag likely contains printable ASCII, the solver prioritizes candidates in the readable range when statistics are tight.
4.  **Reconstruct**: Assemble the recovered bytes into the final flag string.

---

## ✅ Result
The mathematical "clarity" revealed by the probes produces the cleartext flag.
**Flag**: `HTB{...}` (derived from the quantum statistics solver).

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
