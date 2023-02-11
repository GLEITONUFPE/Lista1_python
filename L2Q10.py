
m = int(input("Digite o número de linhas da matriz (M <= 4): "))
n = int(input("Digite o número de colunas da matriz (N <= 8): "))


matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(int(input("Digite o elemento ({},{}): ".format(i, j))))
    matriz.append(linha)


multiplos_6 = []


for j in range(n):
    for i in range(m):
        elemento = matriz[i][j]
        if elemento % 6 == 0:
            multiplos_6.append(elemento)


print("Matriz:")
for linha in matriz:
    print(linha)


print("\nElementos múltiplos de 6:")
print(multiplos_6)
