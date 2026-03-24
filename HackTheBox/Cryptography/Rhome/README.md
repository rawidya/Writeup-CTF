# HTB Challenge: Rhome

## 📝 Challenge Summary
**Rhome** is a Cryptography challenge based on the Diffie-Hellman key exchange. The vulnerability lies in the use of a "Small Subgroup" for the generator `g`, which significantly reduces the search space for the discrete logarithm problem.

---

## 🔎 Step-by-Step Analysis

### 1. Analyzing Parameter Generation
The server generates a large prime $p$ of the form $p = 2 \cdot q \cdot r + 1$. Crucially, the generator $g$ is defined as $g = h^{2r} \pmod p$.
This means that $g^q = h^{2qr} = h^{p-1} \equiv 1 \pmod p$ (by Fermat's Little Theorem).
The order of $g$ is therefore $q$, which is only a **42-bit prime**.

### 2. The Small Subgroup Attack
In a standard Diffie-Hellman exchange, the search space for the private key is the size of the whole group (typically 2048 bits). Here, because $g$ is in a subgroup of order $q$, the effective search space for the private key $a \pmod q$ is only $2^{42}$. This is small enough to solve using the **Baby-step Giant-step (BSGS)** algorithm or Pollard's Rho.

### 3. Exploitation Steps
1.  Connect to the server and receive the public keys $A$, $B$, and the prime $p$.
2.  Find the small prime $q$ by factoring $(p-1)/2$.
3.  Solve the Discrete Logarithm Problem: $g^a \equiv A \pmod p$ in the subgroup of order $q$.
4.  Once you have the private key fragment $a$, calculate the shared secret: $SS = B^a \pmod p$.
5.  Derive the AES key from the shared secret and decrypt the flag.

---

## 🛠️ Tools Used
- **Sagemath**: Excellent for solving Discrete Logarithms in subgroups.
- **Python / PyCryptodome**: To perform the final AES decryption.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
