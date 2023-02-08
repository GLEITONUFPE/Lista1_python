num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

result = num1 % num2

if result == 0:
    print(num1)
else:
    print(result**2)
    print(pow(result, 2))
