# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

n = int(input("[1]Domingo \n[2]Segunda \n[3]Terça \n[4]Quarta \n[5]Quinta \n[6]Sexta \n[7]Sábado \nHoje é qual dia: "))

if n == 1:
    print("Domingooo, uhuu, mais um dia de descanso")
elif n == 2:
    print("Poxa, hoje é segunda, triste")
elif n == 3:
    print("Hoje ainda é terça, a semana não passa nunca")
elif n == 4:
    print("Chegamos no meio da semana, quartinha")
elif n == 5:
    print("Cada vez mais perto da sexta, mas ainda é quinta")
elif n == 6:
    print("Finalmenteee, sextou!!")
elif n == 7:
    print("Sabadou!!!")
else:
    print("Valor inválido")