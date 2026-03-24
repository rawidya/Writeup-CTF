# HTB Challenge: Noncesense-Encryption

## 📝 Challenge Summary
**Noncesense-Encryption** focuses on a custom stream cipher vulnerability. The encryption uses a nonce based on the current system time, creating a system of linear congruences that can be solved using number theory.

---

## 🔎 Step-by-Step Analysis

### 1. The Vulnerability: Reversible Mixing
The server encrypts a known message using a key generated from a nonce (timestamp) and the secret flag. 
- The first 50 bits of the keystream are directly derived from the value $R = \text{Flag} \pmod{\text{Nonce} \times K}$.
- The mixing function used to produce these 50 bits is **reversible**, allowing us to recover the original $R$ for any given timestamp.

### 2. Data Collection
By making multiple requests (around 50), you receive 50 ciphertexts and their approximate timestamps. By XORing the ciphertext with your known plaintext, you recover the keystream and then reverse the mixer to find the remainders $R_i$.

### 3. The CRT Attack
You now have a system of modular equations:
$Flag \equiv R_0 \pmod{Nonce + 0}$
$Flag \equiv R_1 \pmod{Nonce + 1}$
...
Using the **Chinese Remainder Theorem (CRT)**, you can solve for the unique value of the Flag that satisfies all these remainders simultaneously.

### 4. Implementation
Since the nonce is based on the server's clock, you must brute-force a small range (e.g., +/- 30 seconds) around your local timestamp to find the exact starting nonce that the server used.

---

## 🛠️ Tools Used
- **Python / Pwntools**: To collect data from the server.
- **SageMath / Crypto.Util**: To implement the CRT solver.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
