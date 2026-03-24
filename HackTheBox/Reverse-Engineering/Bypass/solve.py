# HTB Bypass - Resource Decrypter
# This script decrypts the "0" resource from the .NET binary.

from Crypto.Cipher import AES
import base64

# --- Configuration (Extracted from dnSpy) ---
# Note: You must find the actual Key and IV from the binary's __cctor or Decrypt method.
# This is a sample template based on the RijndaelManaged implementation.
KEY = b"REPLACE_WITH_32_BYTE_KEY" 
IV  = b"REPLACE_WITH_16_BYTE_IV"

def decrypt_resource(data):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted = cipher.decrypt(data)
    # Remove padding (standard PKCS7)
    padding_len = decrypted[-1]
    return decrypted[:-padding_len]

# --- Usage ---
# 1. Extract resource "0" as a binary file using dnSpy.
# 2. Run this script.
# with open('resource_0.bin', 'rb') as f:
#     data = f.read()
#     print(decrypt_resource(data).decode('utf-8'))

print("HTB Bypass Solver Template Ready.")
print("Ensure you extract the KEY and IV from the __cctor method in dnSpy.")
