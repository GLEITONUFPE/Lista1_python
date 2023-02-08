import math

# numero = int(input("Digite um numero inteiro: "))
# primo = True
# for i in range(2, numero):
#     if numero % i == 0:
#         primo = False
#         print(numero, "não é primo!")

# if primo:
#     print(numero, "é primo!")

num = int(input("numero: "))
raiz = int(math.sqrt(num))
d = 2

while d <= raiz and num % d != 0:
    d = d + 1

if d > raiz:
    print("primo")
else:
    print("nao e primo")
