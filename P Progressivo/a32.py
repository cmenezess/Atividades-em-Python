# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal.

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
op = int(input("[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \n[5] Exponenciação \nQual operação você deseja fazer: "))

if op == 1:
    res = n1 + n2
    if res % 2 == 0:
        print(f"{res} é par")
    else:
        print(f"{res} é ímpar")
    if res > 0:
        print(f"{res} é positivo")
    elif res == 0:
        print(f"{res} é zero")
    else:
        print(f"{res} é negativo")

if op == 2:
    res = n1 - n2
    if res % 2 == 0:
        print(f"{res} é par")
    else:
        print(f"{res} é ímpar")
    if res > 0:
        print(f"{res} é positivo")
    elif res == 0:
        print(f"{res} é zero")
    else:
        print(f"{res} é negativo")

if op == 3:
    res = n1 * n2
    if res % 2 == 0:
        print(f"{res} é par")
    else:
        print(f"{res} é ímpar")
    if res > 0:
        print(f"{res} é positivo")
    elif res == 0:
        print(f"{res} é zero")
    else:
        print(f"{res} é negativo")

if op == 4:
    res = n1 / n2
    if res % 2 == 0:
        print(f"{res} é par")
    else:
        print(f"{res} é ímpar")
    if res > 0:
        print(f"{res} é positivo")
    elif res == 0:
        print(f"{res} é zero")
    else:
        print(f"{res} é negativo")

if op == 5:
    res = n1 ** 5
    if res % 2 == 0:
        print(f"{res} é par")
    else:
        print(f"{res} é ímpar")
    if res > 0:
        print(f"{res} é positivo")
    elif res == 0:
        print(f"{res} é zero")
    else:
        print(f"{res} é negativo")