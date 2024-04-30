# Crie um programa que pergunta se o usuário deseja adicionar uma nova banda na Lista ou exibir a lista.

bandas = []

while True:
    bnd = input("Qual banda você deseja adicionar na lista? ")
    bandas.append(bnd)
    cont = input("Deseja adicionar outra? [s/n]: ").lower()
    if cont == "s":
        continue
    elif cont == "n":
        print(bandas)
        break
    elif cont != "s" or cont != "n":
        print("Digite um caractere válido.")