soma = 0
n1 = int(input())
n2 = int(input())

if n2 > n1:
    n1, n2 = n2, n1

if n1 % 2 == 0:
    aux = n1+1
else:
    aux = n1
for i in range(aux, n2+1, 2):
    soma = soma+i
print("resultado", soma, "para", n1, "e", n2)
