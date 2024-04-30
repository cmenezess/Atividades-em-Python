# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:

#       Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0                      A
#       Entre 7.5 e 9.0                        B
#       Entre 6.0 e 7.5                        C
#       Entre 4.0 e 6.0                        D
#       Entre 4.0 e zero                      E
#     O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota = float(input("Digite sua nota: "))

if nota >= 0 and nota < 4:
    print("E - REPROVADO")
elif nota >= 4 and nota < 6:
    print("D - REPROVADO")
elif nota >= 6 and nota < 7.5:
    print("C - APROVADO")
elif nota >= 7.5 and nota < 9:
    print("B -APROVADO")
elif nota >= 9 and nota <= 10:
    print("A - APROVADO")
else:
    print("Valor inválido")