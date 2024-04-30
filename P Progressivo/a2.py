#Os números binários começam com '0b' no início, octal com '0o' (zero e letra o) e os hexadecimais com '0x' no início.

#Números binários (zero e b):
n1 = 0b10
print(n1)

#Números octal(zero e o):
n2 = 0o21
print(n2)

#Números hexadecimais (zero e x):
n3 = 0x12
print(n3)

#Já se quiser saber quanto vale um número decimal em binário, digite bin(x), onde x é o número que deseja saber.
#Para octal, oct(x) e hexadecimal hex(x).
x = int(input("Informe o valor a ser convertido: "))
n4 = bin(x)
n5 = oct(x)
n6 = hex(x)

#ATIVIDADE: nos comentários, escreva sua idade no sistema binário, octal e hexadecimal.
n4 = bin(24)
print(n4)

n5 = oct(24)
print(n5)

n6 = hex(24)
print(n6)

#Calcule a soma de dois números complexos no Python:
#(1+2j) + (3 + 4j)
res = (1 + 2j) + (3 + 4j)
print(res)

#Booleano:
print(1 > 2) #Vai aparecer False, pois 1 não é maior que 2
print(3 > 2) #Vai aparecer True, pois 3 é maior que 2

#Variáveis:
idade = 24
print(idade)
texto = "Curso Python Progressivo"
print(texto)
print(idade, texto)

idade=18
nome='Maria Joaquina de Amaral Pereira Goes'
print('Nome:', nome)
print('Idade:', idade)

