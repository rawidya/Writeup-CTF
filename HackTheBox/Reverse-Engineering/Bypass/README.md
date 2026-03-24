# HTB Write-up: Bypass

## 📝 Challenge Summary
**Bypass** is a .NET reverse engineering challenge that presents a client-side authentication screen. The application is obfuscated and contains an "impossible" check that always returns false. To solve it, we must extract encrypted resources and patch the binary Flow to skip the security gates.

---

## 🔎 Recon (Initial Analysis)
The provided file is a 9KB .NET assembly. Loading it into IDA Pro initially shows confusing, obfuscated names like `_0__0` and `_0__1`. Because it's a managed .NET application, **dnSpy** is a much more effective tool for analysis than traditional disassemblers.

### The Obfuscation Scheme
The application hides all its strings (passwords, status messages, etc.) in an embedded resource named **"0"**. At runtime, it uses the `RijndaelManaged` (AES) class to decrypt this resource. 

### The Impossible Gate
Analysis of the `main` method reveals a multi-stage check. The first check calls a method that is hardcoded in Intermediate Language (IL) to always load a zero (`ldc.i4.0`) before returning. This makes the check impossible to pass without modification.

---

## ⚙️ Strategy: Bypassing the Protection
Our attack involves two phases: extracting the secrets and patching the code logic.

### 1. Resource Decryption
We extract the encrypted resource "0" using dnSpy. The decryption key and IV are also stored within the binary. We use a Python script to decrypt the resource and recover the plaintext password used for the final stage.

### 2. IL Patching
Using dnSpy's "Edit IL Instructions" feature, we locate the `brfalse.s` instruction responsible for the failure message.
- **Goal**: Change the conditional branch to a `nop` (No-op) or a direct jump.
- **Pitfall**: Manual hex patching often breaks the method signature or the JIT compiler. Using dnSpy to handle the instruction re-encoding is the safest method.

---

## 🚀 Exploitation Steps
1.  **Extract**: Identify resource "0" and save it to disk.
2.  **Decrypt**: Use a script to reverse the AES-CBC encryption, revealing the password: `ThisIsAReallyReallySecureKey...`
3.  **Patch**: Open the binary in dnSpy, find the entry point, and replace the `brfalse.s` instruction with a `pop` or `nop` to bypass the `flag == false` condition.
4.  **Execute**: Run the patched binary, provide the recovered password, and the program will print the flag.

---

## ✅ Result
After patching, the final barrier is cleared.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
