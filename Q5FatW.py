num = int(input("Fatorial de: ") )

result = 1
count = 1

while count <= num:
    result *= count
    count += 1

print("O fatorial de", num, "é:", result)