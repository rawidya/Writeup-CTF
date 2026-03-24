# HTB BinCrypt-Breaker - XOR Decrypter
# Stage 1: XOR file.bin with 0xAB to get the hidden executable.

def decrypt_loader(input_file, output_file):
    XOR_KEY = 0xAB
    with open(input_file, 'rb') as f:
        data = f.read()
    
    decrypted = bytearray(b ^ XOR_KEY for b in data)
    
    with open(output_file, 'wb') as f:
        f.write(decrypted)
    
    print(f"Successfully decrypted {input_file} to {output_file}")

if __name__ == "__main__":
    # decrypt_loader('file.bin', 'decrypted_binary')
    print("Stage 1 Extractor Ready.")
