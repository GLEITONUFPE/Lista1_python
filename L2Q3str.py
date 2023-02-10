
proc = input("proc: ")
texto = input("texto: ")
cont = 0

pos = texto.find(proc)

while pos != -1:
    cont = cont + 1
    pos = texto.find(proc, pos + 1)
print(cont)
# print(texto.count(proc))
