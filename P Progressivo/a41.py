# Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada

tabuada = int(input("De qual número deseja fazer a tabuada de multiplicação: "))

for i in range(1, 11):
    print(f"{i} x {tabuada} = {i*tabuada}")


# Crie um programa que pergunte ao usuário o termo inicial e a razão de uma PA.
# Em seguida, pergunte a ele quantos elementos da PA ele deseja que seja impresso,
# e imprima todos os elementos dessa progressão Aritmética, do primeiro termo até o termo 'n' escolhido pelo usuário
# A sequência começa com o número inicial.
# O termo seguinte da sequência é o anterior, somado a razão. E assim sucessivamente.
#Progressão aritmética:
inicial = int(input("Qual o termo inicial: "))
razao = int(input("Qual a razão da PA: "))
qtd = int(input("Quantos elementos deseja que seja impresso: "))

for i in range(inicial, qtd+1):
    inicial += razao
    print(inicial)