# Crie um programa em Python que peça seu nome, sua idade, sua altura, seu peso e True se for casado ou False para solteiro.
# Em seguida, ele deve armazenar todas essas informações numa lista chamada eu. Por fim, imprima essa lista na tela.

nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso= float(input("Peso: "))
while True:
    civil = input("Casado ou Solteiro? [C/S]: ").upper()
    if civil == "C":
        civil= True
        break
    elif civil == "S":
        civil = False
        break
    else:
        print("Digite um caractere válido.")
        continue

eu = [nome, idade,altura, peso, civil]

print(eu[1])