# Exercício com teste condicional IF em Python
# Escreva um programa que pede a idade do usuário.
# Se ele for maior de idade, exibimos uma mensagem dizendo que já pode dirigir.

idade = int(input('Informe tua idade: '))

if idade >= 18:
    print('Já pode dirigir.')


# Faça um programa que pergunta o gênero da pessoa. Se ela for mulher, digite 1. Se for homem, digite 2. Outro, 3.
# Para cada um, ele deve exibir uma mensagem dizendo o gênero escolhido.

genero = int(input("Qual seu gênero? \n[1] Mulher; \n[2] Homem; \n[3] Outro; \nInforme um valor: "))

if genero == 1:
    print("Mulher")
elif genero == 2:
    print("Homem")
elif genero == 3:
    print("Outro")
else:
    print("Número inválido")

# Escreva um código que exiba o nome de dois times, em seguida pergunta ao usuário qual deles é o melhor.
time = int(input("Qual o melhor time? \n[1]Bahia \n[2]Vitória \n[3]Outro \nSelecione uma opção: "))

if time == 1:
    print("MELHOR ESCOLHA, MELHOR TIME!!!!")
elif time == 2:
    print("Vitória nem é time, an an")
elif time == 3:
    outro = input("Qual time você torce? ")
    print(f"Então você torce para o {outro}, interessante!")
else:
    print("Opção inválida.")