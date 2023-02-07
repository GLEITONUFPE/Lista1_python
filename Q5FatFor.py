num = int(input("Fatorial de: "))

result = 1
for i in range(1, num+1):
    result *= i

print("O fatorial de", num, "é:", result)
