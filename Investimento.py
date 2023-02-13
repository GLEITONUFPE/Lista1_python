# investimento_inicial = float(
#     input("Informe o valor do investimento inicial: "))
# taxa_juros_trimestral = float(input("Qual taxa de juros trimestral: "))
# periodo_anos = int(input("Informe o período em anos: "))

# for i in range(periodo_anos * 4):
#     rendimento = investimento_inicial * taxa_juros_trimestral
#     investimento_inicial += rendimento
#     print("Rendimento: {:.2f} Montante: {:.2f}".format(
#         rendimento, investimento_inicial))

entrada = input().split()

investimento_inicial = float(entrada[0]) 
taxa_juros_trimestral = float(entrada[1]) 
periodo_anos = int(entrada[2])

for i in range(periodo_anos * 4):
    rendimento = investimento_inicial * taxa_juros_trimestral
    investimento_inicial += rendimento
    print("Rendimento: {:.2f} Montante: {:.2f}".format(
        rendimento, investimento_inicial))
