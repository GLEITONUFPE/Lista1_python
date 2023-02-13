# def bourrier_series(N):
#     result = 0
#     for n in range(0, N):
#         result += ((-1)**n) / (2*n + 1)
#     result *= 4
#     return result

# N = int(input("Insira o valor de N: "))
# print(bourrier_series(N))

# S = pi*(N-1)/2+2*(N**2)+((N-3)*pi)/8+4*(N**4)+((N-5)*pi)/32

import math

def bourrier_series(N):
    PI = 3.14
    S = PI * (N - 1) / 2 + 2 * (N**2) + ((N - 3) * PI) / 8 + 4 * (N**4) + ((N - 5) * PI) / 32
    return S

# exemplo de uso
N = 3
print("Série de Bourrier para N =", N, "é igual a", bourrier_series(N))
