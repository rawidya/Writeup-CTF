# HTB Challenge: Untrusted-Node

## 📝 Challenge Summary
**Untrusted-Node** simulates a Quantum Key Distribution (QKD) protocol. You act as a Man-in-the-Middle (the Trusted Node). The protocol has a redundancy flaw: for every bit of the key, multiple identical qubits are sent. You must intercept and measure some while letting others pass to recover the secret key without being detected.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying the Flaw
The `transmitter.py` sends "chunks" of $k$ qubits for every single bit. All $k$ qubits are in the same encoded state (Z-basis or X-basis). Alice and Bob will later compare their bases to decide which bits to keep.

### 2. The Interception Strategy
Since you don't know the basis (Z or X) in advance, you can use the redundancy:
1.  **Intercept Qubits 0 & 1**: Measure the first qubit in the **Z-basis** and the second in the **X-basis**.
2.  **Pass the rest**: Let the remaining $k-2$ qubits pass through to Bob undisturbed (`gate = -1`).
3.  **Result**: You now have the bit value regardless of which basis is chosen later.

### 3. Reconciliation Bypass
During the "match" phase, the server asks you for gates to send back to Alice. To prevent Alice from noticing your measurements:
- Send a "garbage" gate index (e.g., `2`) for positions 0 and 1. This causes Alice to skip them.
- Send Bob's original gates for the remaining positions.

### 4. Key Recovery
When the server reveals the indices where Alice and Bob's bases matched, you check which basis was used. If it was Z, use your result from qubit 0. If it was X, use your result from qubit 1. This allows you to reconstruct the full key, hash it (SHA256), and decrypt the server's flag command.

---

## 🛠️ Tools Used
- **Pwntools**: To automate the two-stage interception and reconciliation process.
- **Quantum Man-in-the-Middle**: Replicating bits using the "No-Cloning Theorem" bypass provided by the redundancy.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
