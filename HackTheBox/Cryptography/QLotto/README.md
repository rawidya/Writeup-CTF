# HTB Challenge: QLotto

## 📝 Challenge Summary
**QLotto** is a "quantum lottery" challenge. The dealer uses a "house card" (Qubit 0) and forbids you from interacting with it. The goal is to bypass this restriction and entangle your own qubits with the house card to predict the winning numbers.

---

## 🔎 Step-by-Step Analysis

### 1. Bypassing the House Check
The server code explicitly checks if any of your gate indices are `0` (`if p == 0: return False`). However, Python's list indexing supports **negative numbers**. Passing `-2` (which refers to the second-to-last qubit, or Qubit 0 in a 2-qubit system) bypasses the `== 0` check while still targeting the forbidden qubit.

### 2. Rigging the Lottery
To win, you need your draw (Qubit 1) to be perfectly anti-correlated with the house draw (Qubit 0).
- **Step 1**: `H:-2` (Reset the house card from its initial superposition to $|0\rangle$).
- **Step 2**: `RXX:90,-1,-2` (Entangle Qubit 0 and 1).
- **Step 3**: `H:-1;Z:-1;H:-1` (Apply a NOT operation to Qubit 1).

After these gates, if the dealer draws a bit $b$, your draw is guaranteed to be the opposite ($1-b$).

### 3. Calculating the Winning Numbers
The lottery uses 6 bits for each number. Since your bits are the inversion of the dealer's bits, your raw 6-bit value will be `63 - dealer_value`. The final logic applies a modulo 42 shift.
`Your_Number = (63 - (Dealer_Draw - 1)) % 42 + 1`

---

## 🛠️ Tools Used
- **Python**: To calculate the winning bets based on the dealer's output.
- **Negative Indexing**: The key bypass technique for the input validator.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
