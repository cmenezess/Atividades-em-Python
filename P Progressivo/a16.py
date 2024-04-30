# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")


# Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2) / 2

if media < 7:
    print(f"Sua média foi {media}. Reprovado.")
elif media >= 7 and media <= 9.9:
    print(f"Sua média foi {media}. Aprovado.")
elif media == 10:
    print("Sua média foi {media}. Parabéns! Aprovado com distinção.")
else:
    print("Nota inválida")


# Faça um Programa que leia três números inteiros e mostre o maior deles.
n1 = int(input("Numero 1: ")) 
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} foi o maior valor")
elif n2 > n1 and n2 > n3:
    print(f"{n2} foi o maior valor")
elif n3 > n1 and n3 > n2:
    print(f"{n3} foi o maior valor")
else:
    print("Valores iguais")


# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
n1 = int(input("Numero 1: ")) 
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} foi o maior valor")
    if n2 > n3:
        print(f"{n3} foi o menor valor")
    elif n3 > n2:
        print(f"{n2} foi o menor valor")
    elif n2 == n3:
        print(f"{n2} e {n3} são iguais. Ambos são os menores valores")
elif n2 > n1 and n2 > n3:
    print(f"{n2} foi o maior valor")
    if n1 > n3:
        print(f"{n3} foi o menor valor")
    elif n3 > n1:
        print(f"{n1} foi o menor valor")
    elif n2 == n3:
        print(f"{n1} e {n3} são iguais. Ambos são os menores valores")
elif n3 > n1 and n3 > n2:
    print(f"{n3} foi o maior valor")
    if n1 > n2:
        print(f"{n2} foi o menor valor")
    elif n2 > n1:
        print(f"{n1} foi o menor valor")
    elif n2 == n3:
        print(f"{n2} e {n1} são iguais. Ambos são os menores valores")
else:
    print("Valores iguais")