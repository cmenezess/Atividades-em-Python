# Crie um programa que imprima na tela os números 1 até o 10, usando o laço while

n = 1
while n <= 10:
    print(n)
    n += 1

print("---------------------------------------------")
# Faça um programa que peça um número maior que 1 ao usuário.
# Em seguida, imprima todos os números, de 1 até o número que o usuário informou

n = int(input("Informe um número maior do que 1: "))

n1 = 0
while n1 <= n:
    print(n1)
    n1 += 1

print("---------------------------------------------------------------")
# Escreva um programa que repita pra sempre, na tela, a mensagem 'Curso Python Progressivo
while True:
    print("Curso Python Progressivo")
    break