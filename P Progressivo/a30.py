# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
# uma nota de 5 e quatro notas de 1.

valor = int(input("Informe o valor a ser sacado: "))

unidade = valor % 10
dezena = ((valor // 10) % 10)
centena = ((valor // 10) // 10)

if centena >= 100 or centena <= 600:
    print(f"{centena} notas de 100")

    if dezena == 5:
        print("1 nota de 50")
    elif dezena < 5:
        print(f"{dezena} notas de 10")
    elif dezena == 6:
        print(f"1 nota de 50 e \n1 nota de 10")
    elif dezena == 7:
        print(f"1 nota de 50 e \n2 notas de 10")
    elif dezena == 8:
        print(f"1 nota de 50 e \n3 notas de 10")
    elif dezena == 9:
        print(f"1 nota de 50 e \n4 notas de 10")

    if unidade == 5:
        print(f"{unidade} nota de 5")
    elif unidade < 5:
        print(f"{unidade} notas de 1")
    elif unidade == 6:
        print(f"1 nota de 5 e \n1 nota de 1")
    elif unidade == 7:
        print(f"1 nota de 5 e \n2 notas de 1")
    elif unidade == 8:
        print(f"1 nota de 5 e \n3 notas de 1")
    elif unidade == 9:
        print(f"1 nota de 5 e \n4 notas de 1")

