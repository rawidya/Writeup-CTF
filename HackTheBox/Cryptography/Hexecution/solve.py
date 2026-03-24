# HTB Hexecution - Unshuffle Solver
# Reverse the custom assembly shuffling pattern.

def unshuffle_block(block):
    # Forward: [0, 1, 2, 3] -> [2, 1, 3, 0]
    # To Unshuffle (Reverse):
    # Orig[0] = Shuffled[3]
    # Orig[1] = Shuffled[1]
    # Orig[2] = Shuffled[0]
    # Orig[3] = Shuffled[2]
    return block[3] + block[1] + block[0] + block[2]

def solve():
    # Character indices reconstructed from the LADDER instructions
    shuffled_str = "5U1c_mI0_4a5_deNLu4M01ntr43_Ufn_"
    
    flag_parts = []
    for i in range(0, len(shuffled_str), 4):
        block = shuffled_str[i:i+4]
        flag_parts.append(unshuffle_block(block))
        
    print(f"Shuffled: {shuffled_str}")
    print(f"Flag: HTB{{{''.join(flag_parts)}}}")

if __name__ == "__main__":
    solve()
