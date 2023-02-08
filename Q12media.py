
quant = 0
soma = 0
resp = 's'

while resp == 's':
    num = float(input("Digite um número: "))

    if num > 0:
        quant += 1
        soma += num

        resp = input("Digite s para continuar: ")

    else:
        print("A média dos números é:", soma/quant)
