
resp = 1
menor = 0
quant = 0

while resp != 0:
    num1 = int(input("Digite um número: "))
    quant += 1
    
    if quant == 1:
        menor = num1
    else:
        if num1 < menor:
            menor = num1

    
    resp = int(input("Digite 1 para continuar e 0 para sair do programa: "))
    
   

print("O menor número é:", menor)







