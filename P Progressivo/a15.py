# Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante.
# Escreva um programa que pergunta a situação do usuário
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não.

# prio = input("Qual a sua situação: Idoso, gestante, cadeirante ou nenhum? ").lower()

# if prio == "idoso" or prio == "gestante" or prio == "cadeirante":
#     print("Você tem acesso a fila de prioridade.")
# else:
#     print("Você não tem acesso a fila de prioridade.")


print("-----------------------------------------------------------------------------")
prio = int(input("[1] Idoso \n[2] Gestante \n[3] Cadeirante \n[4] Nenhum destes \nInforme sua opção: "))

if prio == 1 or prio == 2 or prio == 3:
    print("Você tem acesso à fila de prioridade.")
elif prio == 4:
    print("Você não tem acesso à fila de prioridade.")
else:
    print("Valor inválido")