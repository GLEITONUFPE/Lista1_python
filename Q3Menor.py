num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

menor = num1

if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3


print("O menor número dos tres digitados é:", menor)
