

n = int(input("Digite a quantidade de cursos: "))

while n <= 0:
    n = int(input("O valor deve ser maior que zero: "))

dic = {}

for i in range(n):
    codC = int(input("Digite o codigo do curso: "))

    while codC <= 0:
        codC = int(input("Codigo invalido! digite valor maior que zero: "))
    nomeCurso = input("Digite o nome do curso: ")
    centroCurso = int(input("Digite o centro do curso: "))

dic[codC] = (nomeCurso, centroCurso)
print("dados cadastrados!")

codC = int(input("digite um codigo para busca. (negativo ou zero, para parar):"))

while codC > 0:
    if codC in dic:
        nomeCurso, centroCurso = dic[codC]
        print(codC, nomeCurso, centroCurso)
    else:
        print("codigo do curso nao existe!")

    codC = int(
        input("digite outro codigo para busca. (negativo ou zero, para parar):"))


print("FIM DA EXECUÇÃO!")
