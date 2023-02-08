

"""n = int(input("Digite o valor de n (n > 0): "))
m = int(input("Digite o valor de m (m > 0): "))

mdc = n
while n % mdc != 0 or m % mdc != 0:
    mdc = mdc - 1

print("MDC", mdc)"""

num1 = int(input("numero1 "))
num2 = int(input("numero2 "))

if num1 < num2:
    mdc = num1
else:
    mdc = num2

while num1 % mdc != 0 or num2 % mdc != 0:
    mdc + mdc - 1
print(mdc)
