# HTB Write-up: Untrusted Node

## 📝 Challenge Summary
**Untrusted Node** is a simulation of a Quantum Key Distribution (QKD) protocol. Alice and Bob attempt to establish a secure key, but the protocol has a redundancy flaw. As the "Trusted Node" in the middle, we can intercept the key bits without alerting the parties or causing a reconciliation failure.

---

## 🔎 Recon (The Redundancy Flaw)
Analysis of `transmitter.py` reveals that Alice sends a "chunk" of $k$ identical qubits for every single bit of the key. All qubits in a chunk share the same basis (Z or X) and the same bit value.
- To maintain the protocol's integrity, Bob only needs to successfully measure **one** qubit in the correct basis.

---

## ⚙️ Strategy: Man-in-the-Middle (MitM)
We exploit the extra qubits in each chunk to learn the key bit for both possible bases simultaneously.

### 1. Interception Phase
For every chunk of size $k$:
1.  Intercept **Qubit 0** and measure it in the **Z-basis** (Gate `0`). Store the result as $R_Z$.
2.  Intercept **Qubit 1** and measure it in the **X-basis** (Gate `1`). Store the result as $R_X$.
3.  Pass the remaining $k-2$ qubits through to Bob unaltered (Gate `-1`).

### 2. Reconciliation Phase
When Bob shares his measurement bases, we must force the Transmitter to skip the qubits we measured (0 and 1) so it doesn't see our interference.
- We send a **Garbage Gate (`2`)** for the first two positions. Since `2` matches neither `0` nor `1`, Alice skips them.
- We provide Bob's real gates for the rest of the chunk.

### 3. Key Reconstruction
When Alice confirms a "match," we check which basis Bob used.
- If Bob matched on Z (0), the key bit is our $R_Z$.
- If Bob matched on X (1), the key bit is our $R_X$.

---

## 🚀 Exploitation Workflow
1.  Collect the `sync_signal` (chunk sizes).
2.  Perform the double-basis measurement via the first payload.
3.  Intercept and spoof the second payload during gate reconciliation.
4.  Reconstruct the full binary key, hash it with SHA-256, and use it to decrypt the final command.

---

## ✅ Result
The protocol is successfully subverted, allowing us to fetch the secret flag.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
