# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90.

litros = float(input("Quantos litros você deseja? "))
tipo = input("[A]Álcool \n[G]Gasolina \nDigite a opção desejada: ").upper()

if litros <= 20 and tipo == "A":
    total = litros * 1.90
    desc = litros * 3
    paga = (desc * total) / 100
    print(f"Sabendo que o preço do litro do álcool é R$1,90, e aplicando {desc}% de desconto, você pagará R${paga}")
elif litros > 20 and tipo == "A":
    total = litros * 1.90
    desc = litros * 5
    paga = (desc * total) / 100
    print(f"Sabendo que o preço do litro do álcool é R$1,90, e aplicando {desc}% de desconto, você pagará R${paga}")

if litros <= 20 and tipo == "G":
    total = litros * 2.50
    desc = litros * 4
    paga = (desc * total) / 100
    print(f"Sabendo que o preço do litro da gasolina é R$ 2,50, e aplicando {desc}% de desconto, você pagará R${paga}")
elif litros > 20 and tipo == "G":
    total = litros * 2.50
    desc = litros * 6
    paga = (desc * total) / 100
    print(f"Sabendo que o preço do litro da gasolina é R$ 2,50, e aplicando {desc}% de desconto, você pagará R${paga}")

