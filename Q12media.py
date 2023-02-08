
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

# soma = 0
# qtd = 0
# num = float(input("numero: "))

# while num<0:
#    num = float(input("invalido, Digite numero positivo:"))
# while num >= 0:
#     soma = soma + num
#     qtd = qtd + 1
#     num = float(input("numero: "))
# if qtd > 0:
#     soma = soma/qtd
#     print("resultado", soma)
# else:
#     print("nenhum numero valido digitado")
