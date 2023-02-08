

n = int(input("Digite o valor de n: "))

soma = 0
  
for divisor in range(1,n):
        if n % divisor == 0:
            soma = soma + divisor 

if n == soma:
        print("O numero",n, "é perfeito")
else: 
        print("O numero",n, "NÃO é perfeito!")