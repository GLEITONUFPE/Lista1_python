
def para_romano(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    num_romano = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            num_romano += simb[i]
            num -= val[i]
        i += 1
    return num_romano


n = int(input("Digite quantos numeros quer converter em romanos: "))

for i in range(n):
    num = int(input("Digite um número inteiro positivo: "))
    print(para_romano(num))
