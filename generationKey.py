def permute(cle, permutation):
    return ''.join(cle[i] for i in permutation)

def divise_cle(cle):
    return cle[:4], cle[4:]

def xor(k1, k2):
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(k1, k2))

def decal_gauche(k, ordre):
    return k[ordre:] + k[:ordre]

def decal_droite(k, ordre):
    return k[len(k) - ordre:] + k[:len(k) - ordre]

def generate_subkeys(cle, permutation, nbr_position):
    cle = permute(cle, permutation)
    k1, k2 = divise_cle(cle)
    k1 = xor(k1, k2)
    k1 = decal_gauche(k1, nbr_position)
    k2 = decal_droite(k2, nbr_position)
    return k1, k2

# Test the function
cle = input("Entrez une clé de longueur 8 : ")
permutation = list(map(int, input("Entrez une permutation de longueur 8 : ").split()))
nbr_position = int(input("Entrez l'ordre de décalage : "))
print(generate_subkeys(cle, permutation, nbr_position))
