# HTB Challenge: Flagportation

## 📝 Challenge Summary
**Flagportation** is a quantum computing challenge that implements a 3-qubit quantum teleportation protocol. You must act as the receiver and apply the necessary corrections to restore the teleported state and recover the flag.

---

## 🔎 Step-by-Step Analysis

### 1. Understanding Teleportation
In a standard teleportation circuit, Alice has two qubits and Bob has one. Alice measures her two qubits ($m_0, m_1$) and sends the results to Bob. Bob must then apply a correction operator to his qubit to restore the original state.
The correction operator is: $X^{m1} Z^{m0}$.

### 2. Interaction Loop
For each 2-bit chunk of the flag, the server provides:
- The **Basis** (Z or X) used for encoding.
- The results of measurements $m_0$ and $m_1$.

### 3. Applying Corrections
You must send the instructions to apply the corresponding gates to Bob's qubit (qubit 2):
- `m0=1, m1=0`: Send `Z:2`
- `m0=0, m1=1`: Send `X:2`
- `m0=1, m1=1`: Send `Z:2;X:2` (Order is important!)
- `m0=0, m1=0`: Send a no-op like `Z:2;Z:2`.

### 4. Measuring the Result
After applying the correction, specify the same **Basis** the server provided (Z or X) to measure qubit 2. 
- If basis was Z, the measurement result is the second bit of the pair.
- If basis was X, the measurement result is the first bit of the pair.

Combining these pairs for all rounds (e.g., 204 rounds) allows you to reconstruct the binary string of the flag.

---

## 🛠️ Tools Used
- **Pwntools**: To automate the high-speed interaction for multiple rounds.
- **Quantum Logic**: Implementing the correction matrix.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
