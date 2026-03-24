# HTB Challenge: Micro Storage

## 📝 Challenge Summary
**Micro Storage** is a web/service challenge that exploits a common vulnerability in how Linux commands handle wildcards. By uploading files with specific names, we can "inject" arguments into a back-end `tar` command to execute arbitrary code.

---

## 🔎 Step-by-Step Analysis

### 1. The Vulnerability: Wildcard Injection
The service offers an option to "Compress all files." This likely executes a command like `tar -cf backup.tar *`. 
In Linux, the `*` expansion is handled by the shell. If a file exists with a name starting with `--`, the `tar` command interprets it as a command-line flag rather than a filename.

### 2. The Tar "Checkpoint" Exploit
The `tar` command has a feature called "checkpoints" which can execute a script after processing a certain number of files. We can exploit this by uploading two files:
1. `--checkpoint=1`: Tells tar to trigger a checkpoint every 1 file.
2. `--checkpoint-action=exec=sh a`: Tells tar to execute the shell script `a` when the checkpoint is reached.

### 3. Execution
1.  Upload a file named `a` containing the command to leak the flag (e.g., `cp /flag.txt pwn.sh`).
2.  Upload the two "flag" files mentioned above.
3.  Select the "Compress" option.
4.  The system runs `tar *`, the exploit triggers, and `pwn.sh` is overwritten with the content of the flag.
5.  Read the `pwn.sh` file to retrieve the flag.

---

## 🛠️ Tools Used
- **Tar Wildcard Injection**: A classic Linux privilege escalation/escape technique.
- **Basic Shell Scripting**: To craft the payload.

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
