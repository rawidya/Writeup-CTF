# HTB Write-up: Wonky AES

## 📝 Challenge Summary
**Wonky AES** is a masterclass in side-channel analysis, specifically **Differential Fault Analysis (DFA)**. The challenge provides an AES-128 encryption service that intentionally injects a fault into the encryption process. By analyzing the relationship between correct and faulty ciphertexts, we can mathematically recover the encryption key.

---

## 🔎 Recon (Identifying the Vulnerability)
Static analysis of the provided C source code reveals a critical flaw:
- The system generates a random key for every session.
- It provides a `CipherFault` routine that injects a 1-byte error in the **9th round** of AES, just before the `MixColumns` transformation.

### The Physics of the Attack
In AES, a fault injected before `MixColumns` in round 9 will spread to exactly 4 bytes of the state in round 10. By comparing the correct ciphertext ($C$) and the faulty one ($C'$), we can eliminate thousands of potential candidates for the last round key ($K_{10}$).

---

## ⚙️ Strategy: The Automated DFA Attack
Since the key changes every session, we must maintain a single persistent connection.
1.  **Collection**: The solver script (using `pwntools`) collects 1000 pairs of (Correct, Faulty) ciphertexts. While DFA theoretically works with 2-4 pairs, 1000 ensures a single, unique key candidate by removing all mathematical noise (false positives).
2.  **Analysis**: For each 4-byte block, we iterate through byte candidates for $K_{10}$ that satisfy the fault equations.
3.  **Key Schedule Reversal**: Once the 16-byte $K_{10}$ is found, we reverse the AES key expansion algorithm to derive the original Master Key.

---

## 🚀 Exploitation Flow
1.  **Stage 1**: Connect and flood the service with encryption requests to gather the traces.
2.  **Stage 2**: Process the traces in-memory to recover $K_{10}$.
3.  **Stage 3**: Request the encrypted flag from the server.
4.  **Stage 4**: Decrypt the flag using the recovered Master Key.

---

## ✅ Result
The terminal output reveals the Master Key and the decrypted flag after the collection phase.
**Flag**: `HTB{...}` (derived from the DFA solver).

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
