nume = 2
deno = 500
soma = 0.0


n = int(input("Numero de termos: "))
while n < 1 or n > 50:
    n = int(input("invalido"))

i = 1

while i <= n:
    soma = soma + nume / deno
    deno = deno - 10
    if nume == 2:
        nume = -5
    else:
        nume = 2

print(soma)
