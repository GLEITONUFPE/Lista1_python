numeros = []
num = int(input("Informe um número: "))
while num != 99:
    numeros.append(num)
    num = int(input("Informe um número: "))

numeros.sort()
print("O segundo maior número é:", numeros[-2])
