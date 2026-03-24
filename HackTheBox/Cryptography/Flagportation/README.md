# HTB Write-up: Flagportation

## 📝 Challenge Summary
**Flagportation** is a quantum computing challenge that implements a simplified **Quantum Teleportation** protocol. A 2-bit secret is encoded into a 3-qubit state. By observing the measurement results of the first two qubits and applying the correct mathematical "corrections" to the third, we can teleport and reconstruct the original bits.

---

## 🔎 Recon (The Teleportation Protocol)
The server provides the following information for each block of the flag:
- **Basis**: Either `Z` or `X`.
- **Measurement 0 ($m_0$)**: Result of the first qubit.
- **Measurement 1 ($m_1$)**: Result of the second qubit.

Our task is to provide the "instructions" (gates) to be applied to the third qubit (Qubit 2) before it is measured to recover the second bit of the secret.

---

## ⚙️ Strategy: Quantum Error Correction
Standard quantum teleportation requires the receiver to apply a correction operator based on the classical bits $m_0$ and $m_1$ sent by the sender:
**$\text{Correction} = X^{m_1} Z^{m_0}$**

### Instruction Mapping
We translate this formula into the server's gate format:
- $m_0=0, m_1=0$: No correction needed. (Used `Z:2;Z:2` as an identity/no-op).
- $m_1=1, m_0=0$: Apply `X:2`.
- $m_1=0, m_0=1$: Apply `Z:2`.
- $m_1=1, m_0=1$: Apply `Z:2` then `X:2`.

---

## 🚀 Decoding the Secret
After the correction, we measure Qubit 2 in the same `Basis` provided by the server.
- The **First Bit** is implied by the Basis (`Z`=0, `X`=1).
- The **Second Bit** is the result of our measurement on Qubit 2.

### Automation Script
The challenge consists of over 200 blocks. We use a Python script with `pwntools` to:
1.  Parse the basis and $m_0, m_1$ values.
2.  Send the corresponding correction gates.
3.  Receive the result of our measurement.
4.  Join the 28-bit results and convert the final binary string into the flag bytes.

---

## ✅ Result
All qubits are successfully teleported and decoded, revealing the secret message.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
