# HTB Write-up: Noncesense Encryption

## 📝 Challenge Summary
**Noncesense Encryption** features a custom stream cipher where the key generation depends on a secret (the Flag) and a time-based Nonce. The challenge involves reversing a deterministic bit-mixer and solving a system of modular congruences using the Chinese Remainder Theorem (CRT).

---

## 🔎 Recon (Deconstructing the Stream Cipher)
The server uses a "Mixer" function (similar to an LFSR) to generate 50-bit blocks of the keystream from an intermediate value $R_i$.
The value $R_i$ is defined as:
**$R_i = \text{FLAG} \pmod{((\text{Nonce} + i) \times 0x13373)}$**

### Vulnerability 1: Mixer Reversibility
The mixer transformation is: `(High, Low) -> (Low, High XOR Low)`.
This is a standard reversible linear operation. Since we can encrypt a known plaintext (like a single 'a'), we can recover the first 50 bits of the keystream, and by reversing the mixer for 25 rounds, we can retrieve the exact value of $R_i$.

---

## ⚙️ Strategy: The CRT Attack
Once we have multiple $R_i$ values, we have a system of congruences:
$R_0 \equiv \text{FLAG} \pmod{\text{Nonce} + 0}$
$R_1 \equiv \text{FLAG} \pmod{\text{Nonce} + 1}$
...
Since $(\text{Nonce} + i)$ and $(\text{Nonce} + j)$ are consecutive integers, they are pairwise coprime (providing they don't share small factors). This is the perfect condition for the **Chinese Remainder Theorem**.

---

## 🚀 Exploitation Workflow
1.  **Collection**: Connect to the server and execute 50 encryption requests to gather 50 samples of $R_i$.
2.  **Normalization**: Reverse the 25-round mixer for each sample to get the raw remainders.
3.  **Nonce Brute-force**: Estimate the server's timestamp and iterate through a local window ($\pm 30$ seconds) to find the exact `Nonce` used.
4.  **Solve**: For the correct Nonce, solve the system of 50 congruences using CRT to recover the large integer representing the Flag.

---

## ✅ Result
The integer solution from CRT, when converted to bytes, reveals the flag.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
