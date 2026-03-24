# HTB Challenge: Wonky AES

## 📝 Challenge Summary
**Wonky AES** is a classic Cryptography challenge involving a **Differential Fault Analysis (DFA)** attack on AES-128. An intentional fault is injected during the encryption process, which can be exploited to recover the master key.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying the Vulnerability
The server provides two ciphertexts for every plaintext: a correct one ($C$) and a faulty one ($C'$). The source code reveals that a bit-flip fault is injected in the 9th round of AES, just before the `MixColumns` operation.

### 2. Collecting Data
Because the round key is required to propagate back to the master key, you need to collect multiple pairs of $(C, C')$. A single fault propagates to 4 bytes of the ciphertext. By collecting around 1000 pairs, you can mathematically solve for the candidates of the 10th round key ($K_{10}$).

### 3. Recovering the Key
1.  Use the DFA equations for AES to find $K_{10}$.
2.  Reverse the AES Key Schedule starting from $K_{10}$ to obtain the original 128-bit master key ($K_0$).
3.  Request the encrypted flag from the server and decrypt it using $K_0$.

### 4. Implementation
The attack must be performed in a single session because the key is randomized on every connection. A Python script using `pwntools` is the standard tool for this automation.

---

## 🛠️ Tools Used
- **Python / Pwntools**: For server interaction.
- **DFA Solver**: Custom implementation of the AES DFA equations.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
