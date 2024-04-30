# Faça um programa que peça dois números e imprima o maior deles.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

if n1 > n2:
    print(f"{n1} é maior do que {n2}")
elif n2 > n1:
    print(f"{n2} é maior do que {n1}")
else:
    print("Valores são iguais.")

# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.
n3 = float(input("Digite um valor: "))

if n3 > 0:
    print(f"{n3} é positivo")
elif n3 < 0:
    print(f"{n3} é negativo")
else:
    print("O valor digitado foi 0.")


# Crie um programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Informe seu sexo: \n[F]Feminino \n[M]Masculino \nDigite a opção: ")

if sexo == "F":
    print("Você é do sexo feminino.")
elif sexo == "M":
    print("Você é do sexo masculino.")
else:
    print("Sexo inválido.")