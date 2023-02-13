import math

# x1 = float(input("Informe x1: "))
# y1 = float(input("Informe y1: "))
# z1 = float(input("Informe z1: "))
# x2 = float(input("Informe x2: "))
# y2 = float(input("Informe y2: "))
# z2 = float(input("Informe z2: "))
entrada = input().split()
x1 = float(entrada[0])
y1 = float(entrada[1])
z1 = float(entrada[2])

entrada2 = input().split()
x2 = float(entrada2[0])
y2 = float(entrada2[1])
z2 = float(entrada2[2])

delta_x = x2 - x1
delta_y = y2 - y1
delta_z = z2 - z1

distancia = math.sqrt(delta_x**2 + delta_y**2 + delta_z**2)

print("A distância entre os pontos é {:.2f}".format(distancia))
