# HTB Write-up: Micro Storage

## 📝 Challenge Summary
**Micro Storage** is a web/misc challenge involving a temporary file storage service. The vulnerability lies in the use of unsanitized wildcards in a backup script, leading to a **Wildcard Injection (RCE)** attack on the `tar` command.

---

## 🔎 Recon (Identifying the Backup Flaw)
The service allows users to upload, list, and compress files. When "Compress" is selected, the server executes a shell command similar to:
`tar -cf backup.tar *`
The asterisk (`*`) is expanded by the shell to include all filenames in the directory. In Linux, if a filename starts with a hyphen (e.g., `--version`), `tar` interprets it as an argument rather than a literal filename.

---

## ⚙️ Strategy: Tar Wildcard Injection
We use this behavior to trick `tar` into executing arbitrary code when it reaches a specific "checkpoint."

### 1. Bypassing Filename Limitations
The server limits the length of uploaded filenames. We cannot directly upload a long payload like `--checkpoint-action=exec=...`. Instead, we use a two-file approach:
- **`a`**: A short filename containing our script: `cp /flag.txt target_storage`.
- **`--checkpoint=1`**: A file that triggers a checkpoint after every 1 file processed.
- **`--checkpoint-action=exec=sh a`**: A file that tells `tar` to run `sh a` at the checkpoint.

### 2. Payload Persistence
Since we cannot list files the server didn't expect, we must overwrite an existing, known file (like `pwn.sh`) with the contents of the flag to read it later.

---

## 🚀 Exploitation Workflow
1.  **Upload** a known file: `pwn.sh`.
2.  **Upload** the payload script `a`: `cp /flag.txt pwn.sh`.
3.  **Upload** the triggers: `--checkpoint=1` and `--checkpoint-action=exec=sh a`.
4.  **Compress**: Select the compression option to trigger the `tar *` command.
5.  **Leak**: Print the contents of the now-overwritten `pwn.sh` to retrieve the flag.

---

## ✅ Result
The flag effectively "replaces" our uploaded file, bypassing the storage isolation.
**Flag**: `HTB{...}`

---
*Disclaimer: This guide is a rephrased summary for educational purposes.*
