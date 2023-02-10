
n = int(input("tamanho: "))

while n < 1:
    n = int(input("invalido, digite novamente: "))

v1 = [0]*n
v2 = [0]*n
vres = [0]*n

for i in range(n):
    v1[i] = n = int(input("v1 elemento" + str(i) + ": "))
for i in range(n):
    v2[i] = n = int(input("v2 elemento" + str(i) + ": "))
    vres[i] = v1[i] + v2[i]

print("v1= ", v1)
print("v2= ", v2)
print("soma= ", vres)
