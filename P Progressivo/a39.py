# Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha,
# seu único script serve para todos os casos


alunos = int(input("Informe o número de alunos na turma: "))

soma = 1
nota = 0
while soma <= alunos:
    n = float(input("Nota do aluno: "))
    soma += 1
    nota += n
    media = nota / alunos
    print(f"A média dos alunos é {media}")