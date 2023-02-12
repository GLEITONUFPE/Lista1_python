total_multa = 0
total_casas = 0
veiculos = int(input("Informe a quantidade de veículos da residência: "))

while veiculos != 999:
    if veiculos > 2:
        multa = (veiculos - 2) * 12.89
        total_multa += multa
        total_casas += 1
    veiculos = int(input("Informe a quantidade de veículos da residência: "))

print("O total mensal arrecadado com as multas é de R$ {:.2f}".format(
    total_multa))
print("A quantidade de casas multadas é de {}".format(total_casas))
