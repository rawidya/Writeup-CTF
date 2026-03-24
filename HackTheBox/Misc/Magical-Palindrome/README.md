# HTB Write-up: Magical Palindrome

## 📝 Challenge Summary
**Magical Palindrome** is a Node.js web challenge that presents an impossible constraint via an Nginx reverse proxy. The backend requires a 1000-character palindrome, but Nginx limits the request body to just 75 bytes. The solution lies in exploiting **JavaScript Type Confusion** to bypass the length check within the body size limit.

---

## 🔎 Recon (The Proxy-Backend Conflict)
Analysis of the configuration files revealed the core bottleneck:
- **`nginx.conf`**: `client_max_body_size 75;`
- **`index.mjs`**: `if (string.length < 1000) return 'Tootus Shortus';`

Sending 1000 actual characters is impossible. However, the `IsPalinDrome` function does not verify the *type* of the input; it simply checks for the existence of a `.length` property.

---

## ⚙️ Strategy: Type Confusion Payload
In JavaScript, a string `length` property is a number. But when compared with another number, a string like `"1000"` is coerced into numeric `1000`.

### The Loop Bypass
The validation loop uses: `for (const i of Array(string.length).keys())`.
- If we pass `length: "1000"`, `Array("1000")` creates an array of size **1** (containing the string `"1000"`).
- This causes the entire 1000-character palindrome check to run exactly **once** (for `i=0`).

### Satisfying the Palindrome
For the single iteration (`i=0`), the function checks:
- `string[0]` must match `string[length - 0 - 1]`, which is `string[999]`.
- Both must be strings.

---

## 🚀 Final Payload
We send a JSON object that mimics the expected structure but with hijacked properties:
```json
{
  "palindrome": {
    "length": "1000",
    "0": "a",
    "999": "a"
  }
}
```
This payload is ~50 bytes, successfully bypassing the 75-byte Nginx limit while appearing as a 1000-character palindrome to the backend.

---

## ✅ Result
The type-confusion bypass triggers the flag release.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
