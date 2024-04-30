# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.
# Dica: utilize o operador módulo (resto da divisão): %

n= int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print("O número digitado é par")
else:
    print("O número digitado é ímpar")