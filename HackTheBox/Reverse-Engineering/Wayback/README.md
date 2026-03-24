# HTB Write-up: Wayback

## 📝 Challenge Summary
**Wayback** is a time-based reverse engineering challenge. You are given an encrypted Bitcoin wallet and a binary (`V1`) that generates passwords. The core vulnerability is the use of a predictable time-based seed for the random number generator. By pinpointing the exact timeframe mentioned in the challenge description, we can brute-force the password and recover the flag.

---

## 🔎 Recon (The Seed Generation)
The challenge provides a timeframe: **December 10th-11th, 2013**.
Static analysis of the `V1` binary reveals that the `srand()` seed is generated using a combination of the current date and time:
```c
seed = (month * 10^8) + (year * MAGIC_CONSTANT) + (hour * 10000) + ...
```
Because the `rand()` function in `glibc` is a Pseudo-Random Number Generator (PRNG), supplying the same seed will always produce the same "random" 20-character password string.

---

## ⚙️ Strategy: Brute-Force the Clock
The search space is small: 2 days $\times$ 24 hours $\times$ 3600 seconds = **172,800 possible seeds**.
Our strategy involves:
1.  Re-implementing the seed formula in a high-performance C script.
2.  Iterating through every second in the December 10-11, 2013 window.
3.  Generating the candidate 20-character password for each seed.
4.  Attempting to decrypt the fixed ciphertext using each candidate as the AES-256-CBC key.

---

## 🚀 The Solve Script (High-Level Logic)
We use a C program with the `OpenSSL` library for maximum speed.
- **Charset**: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_+0123456789`
- **Verification**: We check the decrypted output for printable ASCII characters and the "HTB" prefix.

```c
// Core loop logic
for (int day = 10; day <= 11; day++) {
    for (int sec = 0; sec < 86400; sec++) {
        unsigned int seed = calculate_seed(2013, 12, day, sec);
        srand(seed);
        generate_password(password, 20, charset);
        if (try_aes_decrypt(ciphertext, password)) {
            printf("Found Flag: %s\n", decrypted_text);
            return 0;
        }
    }
}
```

---

## ✅ Result
The brute-force completes in seconds. The correct seed corresponds to a specific timestamp on December 11th, revealing the password and the flag.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
