# HTB Wayback - Time-Based Brute Force Template
# Brute-force the seed based on a specific timeframe (Dec 10-11, 2013).

import ctypes
import datetime

# --- Load libc for rand() ---
libc = ctypes.CDLL("libc.so.6") # Use "msvcrt" on Windows, but the binary is Linux ELF

def generate_seed(dt):
    # This formula must match the one decompiled in V1
    # Example: seed = (100000000 * (dt.month + 1)) + (1410065408 * dt.year) + (10000 * dt.hour)
    # Be careful with 32-bit integer overflow!
    pass

def solve():
    # Start: Dec 10, 2013 00:00:00
    # End: Dec 11, 2013 23:59:59
    start_time = datetime.datetime(2013, 12, 10, 0, 0, 0)
    end_time = datetime.datetime(2013, 12, 11, 23, 59, 59)
    
    current = start_time
    while current <= end_time:
        seed = generate_seed(current)
        # libc.srand(seed)
        # password = "".join([chr(libc.rand() % 72 + ASCII_START) for _ in range(20)])
        # Check if the generated password decrypts the flag file.
        current += datetime.timedelta(seconds=1)

if __name__ == "__main__":
    print("HTB Wayback Brute-Forcer Template.")
    print("Note: Use a C solver or Python with ctypes to match glibc's rand() behavior.")
