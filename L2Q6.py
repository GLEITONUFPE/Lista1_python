
n = int(input("tamanho: "))

while n < 1:
    n = int(input("digite novamente: "))

v1 = [0]*n
par = [0]*n
imp = [0]*n

for i in range(n):
    v1[i] = n = int(input("v1 elemento" + str(i) + ": "))
    if v1[i] % 2 == 0:
        par[qp] = v1[i]
        qp = qp + 1
    else:
        imp[qi] = v1[i]
        qi = qi + 1
par = par[:qp]
imp = imp[:qi]

print("lidos: ", v1)
print("pares: ", par)
print("impares: ", imp)
