#Divisão:
# var1 = int( input("Digite um inteiro: ") )
# var2 = int( input("Digite outro inteiro: ") )

# divisao = var1 / var2

# print(divisao)

#Exponenciação:
# var1 = int( input("Digite um inteiro: ") )
# var2 = int( input("Digite outro inteiro: ") )
# exp = var1 ** var2
# print(exp)

# Exercício: Crie um programa em Python que peça dois números ao usuário.
# Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão,
# exponenciação e resto da divisão do primeiro número pelo segundo.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
divi = n1 / n2
exp = n1 ** n2
resto = n1 % n2
print(f"Soma: {n1} + {n2} = {soma}")
print(f"Subtração: {n1} - {n2} = {sub}")
print(f"Multiplicação: {n1} * {n2} = {multi}")
print(f"Divisão: {n1} / {n2} = {divi}")
print(f"Exponenciação: {n1} ** {n2} = {exp}")
print(f"Resto da divisão: {n1} % {n2} = {resto}")