numeros = []
count = 0

n = int(input("Número, negativo para: "))

while n >= 0 and count < 1000:
    if n > 9 and n < 100:  # condição para pegar apenas números com dois dígitos
        numeros.append(n)
        count += 1
    n = int(input("Número, negativo para: "))

numeros.reverse()
print(numeros)
