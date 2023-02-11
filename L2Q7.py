n = int(input("Digite o número de alunos: "))

notas = []
soma = 0

for i in range(n):
    nota = float(input("Digite a nota final do aluno {}: ".format(i + 1)))
    notas.append(nota)
    soma += nota

media = soma / n

print("A média das notas é: {:.2f}".format(media))

print("As notas acima da média são:")

for nota in notas:
    if nota > media:
        print(nota)
