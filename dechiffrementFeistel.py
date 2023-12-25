def permute(block, permutation):
    return ''.join(block[i] for i in permutation)

def inverse_permute(block, permutation):
    inverse = [''] * len(permutation)
    for i, p in enumerate(permutation):
        inverse[p] = block[i]
    return ''.join(inverse)

def split_block(block):
    return block[:4], block[4:]

def xor(b1, b2):
    return ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(b1, b2))

def or_op(b1, b2):
    return ''.join(str(int(bit1) | int(bit2)) for bit1, bit2 in zip(b1, b2))

def feistel_decryption(block, permutation, subkeys):
    block = permute(block, permutation)
    G2, D2 = split_block(block)
    for i in range(2):
        if i == 0:
            G1 = inverse_permute(xor(D2, subkeys[1]), [2, 0, 1, 3])
            D1 = xor(G2, or_op(G1, subkeys[1]))
        else:
            G0 = inverse_permute(xor(D1, subkeys[0]), [2, 0, 1, 3])
            D0 = xor(G1, or_op(G0, subkeys[0]))
    plain_text = inverse_permute(G0 + D0, permutation)
    return plain_text

# Test the function
block = input("Entrez un bloc de 8 bits : ")
permutation = list(map(int, input("Entrez une permutation de longueur 8 : ").split()))
subkeys = [input("Entrez la sous-clé k1 de 4 bits : "), input("Entrez la sous-clé k2 de 4 bits : ")]
print(feistel_decryption(block, permutation, subkeys))
