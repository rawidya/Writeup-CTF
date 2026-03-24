# HTB Challenge: Magical-Palindrome

## 📝 Challenge Summary
**Magical-Palindrome** is a web-based logic challenge involving a Node.js backend protected by an Nginx reverse proxy. The core of the challenge is a conflict between path validation rules: a length requirement of 1000 characters and a body size limit of 75 bytes.

---

## 🔎 Step-by-Step Analysis

### 1. Identifying the Conflict
- **Nginx**: `client_max_body_size 75;`
- **Node.js**: `if (string.length < 1000) return 'Tootus Shortus';`

Sending 1000 characters is impossible due to Nginx. We must find a way to make a small payload appear long.

### 2. JavaScript Type Confusion
The `IsPalinDrome` function doesn't check the type of its input. In JavaScript, an object with a `.length` property can masquerade as a string or array.
If we send `length: "1000"`, the check `string.length < 1000` evaluates to `1000 < 1000`, which is **false**. The check is bypassed.

### 3. Bypassing the Loop
The function iterates using `Array(string.length).keys()`. 
- If `length` is the string `"1000"`, `Array("1000")` creates an array of length 1 (containing the single element `"1000"`).
- The loop will only run once for `i = 0`.

### 4. Exploitation
For `i = 0`, the palindrome check compares:
- `original = string[0]`
- `reverse = string[string.length - 1]` (which is `string[999]`)

Our payload just needs an object with `length: "1000"` and identical values at indices `0` and `999`.

### 5. Final Payload
```json
{"palindrome": {"length": "1000", "0": "a", "999": "a"}}
```
This payload is ~50 bytes, fitting well within the 75-byte Nginx limit.

---

## 🛠️ Tools Used
- **JSON Payload**: To trigger type confusion.
- **Curl**: To send the malicious request.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
