# Para votar, você deve ter entre 18 anos e menos de 65 anos.
# Escreva um programa que pergunte sua idade e diga se você é obrigado a votar ou não.

# Temos dois testes:
# Testar se tem 18 anos ou mais
# Testar se tem 65 ou menos

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inexistente.")
elif idade >= 0 and idade <= 17:
    print("Você ainda não pode votar.")
elif idade >= 18 and idade <= 65:
    print("Você já pode votar!")
else:
    print("Você não é obrigado a votar.")
