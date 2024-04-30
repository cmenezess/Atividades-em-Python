# Vamos ver na prática o uso da função input. Programe o seguinte código:
# variavel=input('Digite algo: ')
variavel = input("Digite algo: ")

print('----------------------------------------------')
# Exercício com a função input() do Python
# "Faça um programa que pergunte a idade do usuário, e a armazene em uma variável.
# Em seguida, pergunte o nome da pessoa e armazene esse dado em outra variável.
# Por fim, exiba uma mensagem de boas vindas ao curso Python Progressivo, dizendo nome e idade da pessoa".
nome = (input('Informe seu nome: '))
idade = int(input("Informe tua idade: "))
print(f"Bem vindo(a), {nome}. Sua idade é de {idade} anos.")

print('-----------------------------------------------------------------------')
# Nosso script:
var1=input("Digite um decimal: ")
print( type(var1) )

var2=float(var1)
print( type(var2) )

var3=2112
var4=float(var3)

print( type(var4) )

print(var4)
#Xablau! Transformamos uma string em float, e depois o inteiro 2112 em um float.
#Imprimimos até var4 para vermos que 2112 se transformou em 2112.0 , um decimal!