# Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha

senha = 1234

conf = int(input("Digite a senha: "))

while conf != senha:
    conf = int(input("Digite a senha: "))
else:
    print("Bem-vindo(a)")