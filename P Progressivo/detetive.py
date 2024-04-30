#  Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

total = 0
print("-------DETETIVE-------")
tel = int(input("Telefonou para a vítima? [1]SIM [2]NÃO: "))
if tel == 1:
    total += 1
local = int(input("Esteve no local do crime? [1]SIM [2]NÃO: "))
if local == 1:
    total += 1
mora = int(input("Mora perto da vítima? [1]SIM [2]NÃO: "))
if mora == 1:
    total += 1
devia = int(input("Devia para vítima? [1]SIM [2]NÃO: "))
if devia == 1:
    total += 1
trab = int(input("Já trabalhou com a vítima? [1]SIM [2]NÃO: "))
if trab == 1:
    total += 1

if total < 2:
    print("Você é inocente.")
elif total == 2:
    print("Você é suspeito(a).")
elif total == 3 or total == 4:
    print("Você foi cúmplice do crime.")
elif total == 5:
    print("Você é o assassino! ")