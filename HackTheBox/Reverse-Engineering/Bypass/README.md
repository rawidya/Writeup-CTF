# HTB Challenge: Bypass

## 📝 Challenge Summary
**Bypass** is a .NET reverse engineering challenge where the goal is to authenticate and read a hidden key. The binary uses client-side checks and resource encryption to hide its logic. The key to solving this is extracting the encrypted resources and patching the IL (Intermediate Language) code to bypass the "impossible" checks.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying the Platform
Initial inspection reveals that the executable is a .NET assembly. While tools like IDA Pro can handle it, **dnSpy** or **ILSpy** are much better suited for .NET reversing as they can show the original C# source code.

### 2. Analyzing the Logic
Opening the binary in dnSpy shows that most strings are obfuscated. There is an embedded resource named "0" which contains the encrypted prompts and the target password.

The program has a two-stage check:
- **Check 1**: Located in the method `'0'::'1'`, this check is hardcoded to return `false` regardless of the input.
- **Check 2**: A standard password comparison against a decrypted value from the resource.

### 3. Decrypting Resources
The resource decryption uses a standard AES (RijndaelManaged) algorithm. You can extract the decryption key from the `__.cctor` (static constructor) and write a Python script to decrypt the "0" resource. This will reveal the password needed for the second check.

### 4. Patching the Binary (The "Bypass")
To pass the first check:
1.  Open the method `'0'::'1'` in dnSpy.
2.  Right-click and select "Edit Method (C#)".
3.  Change `return false;` to `return true;`.
4.  Compile and save the module.

Now, when you run the patched executable and enter the password extracted from the resource, you will get the flag.

---

## 🛠️ Tools Used
- **dnSpy**: For decompiling and patching .NET code.
- **Python**: To write a decryption script for the embedded resource.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
