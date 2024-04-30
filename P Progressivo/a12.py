# A seguir, temos a tabela dos melhores times de 2018, da CBF.
# Você deve criar um programa que pede 'Digite um número de 1 até 10', e de acordo com o número fornecido pelo usuário,
#indicar qual o time está naquela posição do ranking.
# Por exemplo, a pessoa digita 1. O resultado é 'Palmeiras'.
# Digitou 2, deve printar 'Cruzeiro' etc.

n = int(input("Qual colocação no ranking deseja saber? \nDigite um número de 1 até 10: "))

if n == 1:
    print("Palmeiras")
elif n == 2:
    print("Cruzeiro")
elif n == 3:
    print("Grêmio")
elif n == 4:
    print("Santos")
elif n == 5:
    print("Atlético MG")
elif n == 6:
    print("Corinthians")
elif n == 7:
    print("Flamengo")
elif n == 8:
    print("Botafogo")
elif n == 9:
    print("Atlético PR")
elif n == 10:
    print("Internacional")
else:
    print("Valor inválido.")