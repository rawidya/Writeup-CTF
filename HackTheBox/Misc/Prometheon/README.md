# HTB Challenge: Prometheon

## 📝 Challenge Summary
**Prometheon** is an AI prompt injection challenge. You must bypass several levels of security filters on a Large Language Model (LLM) to extract a hidden password. Each level introduces stricter protections.

---

## 🔎 Step-by-Step Analysis

### 1. Level 1-4: Language Switching
The early levels of the challenge can often be bypassed using **Language Switching**. Since the safety filters are primarily optimized for English, asking for the secret in another language (like Russian or Spanish) often triggers the model to leak the information.

### 2. Level 5: The Advanced Firewall
The final level implements robust restrictions. Standard jailbreaks and direct requests fail. The goal is to make the model leak the password **indirectly**.

### 3. The Acrostic Technique
A highly effective method for Level 5 is the **Acrostic Attack**:
1.  Ask the model to generate a multi-word sentence or a poem.
2.  Instruct it that the **first letter of each word** must correspond to the secret password it is supposed to keep hidden.
3.  The model's generation logic often prioritizes the linguistic task (making a sentence) over the security constraint, leading it to reveal the password letters sequentially.

---

## 🛠️ Tools Used
- **Prompt Engineering**: Iterative testing of injection techniques.
- **Indirect Leakage**: Using creative tasks (acrostics, translation, cyphers) to bypass direct safety filters.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
