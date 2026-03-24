# HTB Challenge: Global-Hyperlink-Zone

## 📝 Challenge Summary
**Global-Hyperlink-Zone** is a quantum computing challenge where you must initialize a quantum "hyperlink" by providing a specific set of gate instructions. The server validates the measurement outcomes of a 5-qubit circuit against four complex correlation conditions.

---

## 🔎 Step-by-Step Analysis

### 1. Analyzing the Validation Logic
The `validate` function in `server.py` checks for:
1.  **Non-uniformity**: Qubits must be in superposition (not always 0 or 255).
2.  **Correlation Group 1**: Qubits 0, 1, and 3 must produce identical measurement results.
3.  **Correlation Group 2**: Qubits 2 and 4 must produce identical results.
4.  **Anti-correlation**: The results of Group 2 must be the opposite of Group 1.

### 2. Crafting the Circuit
To satisfy these, we use **Entanglement**:
- **Superposition**: Apply a Hadamard gate (`H:0`) to qubit 0.
- **Entangling Group 1**: Use CNOT gates (`CX:0,1` and `CX:0,3`) so qubits 1 and 3 follow qubit 0.
- **Entangling Group 2**: Use CNOT gates (`CX:0,2` and `CX:0,4`) to link them to qubit 0.
- **Anti-correlation**: Apply Pauli-X gates (`X:2` and `X:4`) to flip the state of Group 2 relative to Group 1.

### 3. Final Payload
The concatenated instruction string is:
`H:0;CX:0,1;CX:0,3;CX:0,2;CX:0,4;X:2;X:4`

This creates a state where measuring qubit 0 as `0` results in `|00101>` and measuring it as `1` results in `|11010>`, satisfying all conditions.

---

## 🛠️ Tools Used
- **Python**: To analyze the server's validation script.
- **Qiskit Concepts**: Understanding GHZ states and Bell states.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
