# HTB Write-up: Global Hyperlink Zone

## 📝 Challenge Summary
**Global Hyperlink Zone** is a quantum computing challenge that requires initializing a "hyperlink" by constructing a specific quantum circuit. The server acts as a validator, checking if the measured state of 5 qubits satisfies complex entanglement and correlation conditions.

---

## 🔎 Recon (Analyzing the Circuit Logic)
The server source code defines the winning state through a set of measurement outcome checks:
- No qubit should be in a uniform state (always 0 or always 1). This implies all qubits must be in a **superposition**.
- Qubits 0, 1, and 3 must produce **identical** results (Correlation).
- Qubits 2 and 4 must produce **identical** results (Correlation).
- The results of (2, 4) must be the **opposite** of (0, 1, 3) (Anti-correlation).

---

## ⚙️ Strategy: Engineering Entanglement
To solve this, we must build a circuit that creates a superposition of two specific 5-qubit states: `|00101>` and `|11010>`.

### 1. Creating the Root Superposition
We apply a **Hadamard (H)** gate to qubit 0. This puts it into the state $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$.

### 2. Cascading the Entanglement
We use **CNOT (CX)** gates with qubit 0 as the control to entangle the other qubits:
- `CX:0,1`, `CX:0,3`: This ensures qubits 1 and 3 always mirror qubit 0.
- `CX:0,2`, `CX:0,4`: This initially links qubits 2 and 4 to qubit 0.

### 3. Implementing Anti-correlation
To satisfy the last condition, we apply **Pauli-X (NOT)** gates to qubits 2 and 4. This flips their values relative to the control qubit, ensuring anti-correlation while maintaining the link.

---

## 🚀 Final Payload
The sequence of instructions is:
`H:0;CX:0,1;CX:0,3;CX:0,2;CX:0,4;X:2;X:4`

This circuit creates the state:
$\Psi = \frac{1}{\sqrt{2}}(|00101\rangle + |11010\rangle)$

---

## ✅ Result
Submitting the gate sequence initializes the hyperlink and returns the flag.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
