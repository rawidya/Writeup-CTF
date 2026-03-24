# HTB Challenge: Phase-Madness

## 📝 Challenge Summary
**Phase-Madness** is a quantum cryptography challenge where the flag is encoded into the rotation phases of individual qubits. You must interact with a quantum server, observe measurement statistics, and use additional rotations to "map" the phase back into readable bit populations.

---

## 🔎 Step-by-Step Analysis

### 1. Understanding the Encoding
The server encodes each byte of the flag into a qubit using three patterns:
- `i % 3 == 0`: `RX(alpha)` rotation.
- `i % 3 == 1`: `RY(beta)` rotation.
- `i % 3 == 2`: `H` gate followed by `RZ(gamma)` rotation.

### 2. Phase-to-Population Mapping
Measuring a qubit in the Z-basis (the default) gives the probability of state $|1\rangle$.
- For `RX` and `RY`, the rotation angle $\theta$ directly correlates to the probability: $P(1) = \sin^2(\theta/2)$.
- For `RZ` after a Hadamard gate, the probability remains 0.5 regardless of the phase $\gamma$. To recover $\gamma$, you must add your own gate (e.g., another `RX(90)` or `H`) before measurement to translate the phase into a measurable bias.

### 3. Brute-Forcing the Bytes
Since the input bytes are in the range 0-255 (degrees), you can:
1.  Add a fixed rotation to the target qubit.
2.  Request multiple measurement shots.
3.  Compare the observed frequency of $|1\rangle$ against pre-computed frequencies for all 256 possible byte values.
4.  Pick the value with the smallest error.

---

## 🛠️ Tools Used
- **Python / Pwntools**: For automated server interaction.
- **Math/Numpy**: To calculate quantum state probabilities.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
