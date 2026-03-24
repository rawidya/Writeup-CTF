# HTB Write-up: QLotto

## 📝 Challenge Summary
**QLotto** is a quantum-themed cryptography challenge where you must "beat the house" in a lottery. The server uses a quantum circuit to generate the winning numbers, but a flaw in the input validation and a predictable correlation between qubits allow us to rig the results.

---

## 🔎 Recon (The House Rules)
The server source code contains a safety check designed to prevent users from manipulating the "house card" (Qubit 0):
```python
if any(p == 0 for p in params):
    print("[Dealer] Hey, don't tamper with the house card — that's forbidden.")
```
However, the system uses Python-style lists for qubit indexing. We can bypass the `p == 0` check by using **negative indexing**.
- **`-2`** refers to the first qubit (0), but satisfies the condition `-2 != 0`.

---

## ⚙️ Strategy: Rigging the Draw
Our goal is to create a state where the lottery result (Qubit 0) is perfectly anti-correlated with our "draw" qubit (Qubit 1).

### 1. Quantum Manipulation
1.  **Reset**: Apply a Hadamard to the first qubit (`H:-2`) to collapse its initial $|+\rangle$ state to $|0\rangle$.
2.  **Entangle**: Apply an Ising **RXX** gate (`RXX:90,-1,-2`) to create a correlated Bell state $\frac{|00\rangle - i|11\rangle}{\\sqrt{2}}$.
3.  **Flip**: Apply an **X (NOT)** transformation to Qubit 1 using the sequence `H:-1;Z:-1;H:-1`.
   - The final state is $\frac{|01\rangle - i|10\rangle}{\sqrt{2}}$, ensuring that if we measure $B$, the house measures $1-B$.

### 2. The Winning Formula
The lottery numbers are derived from 6-bit values. Since our bits are always the inverse of the house bits, the sum of our raw value and the house's value is always **63** ($111111_2$).
To find the required bet for a given draw `D`:
- **`Bet = (63 - (D - 1)) % 42 + 1`**

---

## 🚀 Exploitation Flow
1.  Send the quantum payload: `H:-2;RXX:90,-1,-2;H:-1;Z:-1;H:-1`.
2.  Receive the dealer's draws.
3.  Apply the transformation formula to calculate the 6 winning bets.
4.  Submit the bets and collect the jackpot.

---

## ✅ Result
Cracking the QLotto logic grants access to the flag.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
