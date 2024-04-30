# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        print(f"Data válida. {dia}/{mes}/{ano}")
    else:
        print("Data inválida.")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        print(f"Data válida. {dia}/{mes}/{ano}")
    else:
        print("Data inválida.")

elif mes == 2:
    if dia <= 28 or dia <= 29:
        print(f"Data válida. {dia}/{mes}/{ano}")
    else:
        print("Data inválida.")
        