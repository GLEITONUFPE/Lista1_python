def data_valida(dia, mes, ano):
    if ano >= 1900 and ano <= 2100:
        if mes >= 1 and mes <= 12:
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                if dia >= 1 and dia <= 31:
                    return True
            elif mes in [4, 6, 9, 11]:
                if dia >= 1 and dia <= 30:
                    return True
            elif mes == 2:
                if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
                    if dia >= 1 and dia <= 29:
                        return True
                else:
                    if dia >= 1 and dia <= 28:
                        return True
    return False

entrada = input().split()

dia = int(entrada[0])
mes = int(entrada[1])
ano = int(entrada[2])

if data_valida(dia, mes, ano):
    print("valida")
else:
    print("invalida")
