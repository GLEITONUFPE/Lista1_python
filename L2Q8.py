
numeros = []

n = int(input("numero, negativo pára: "))

while n >= 0:
    if n > 9 and n < 100:  # condiçao pra pegar apenas numeros com dois digitos
        numeros.append(n)
    n = int(input("numero, negativo pára: "))

numeros.reverse()
print(numeros)
