def square_and_multiply(x, b, n):
    b = bin(b)[2:]  # Convertir b en binaire
    r = 1
    for i in b:
        r = (r**2) % n
        if i == '1':
            r = (r * x) % n
    return r

# Test de la fonction
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))
print(square_and_multiply(x, b, n))
