# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                           Até 5 Kg                 Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg
#     Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
# escreva o valor a ser pago pelo cliente.

soma = 0
morangos = int(input("Quantos kg de morangos você comprou: "))
soma += morangos
macas = int(input("Quantos kg de maças você comprou: "))
soma += macas
print(soma)
if morangos <= 5:
    morango_total = morangos * 2.50
elif morangos > 5:
    morango_total = morangos * 2.20

if macas <= 5:
    macas_total = macas * 1.80
elif macas > 5:
    macas_total = macas * 1.50

total = morango_total + macas_total


if soma <= 8 and total <= 25:
    print(f"Você pagará R${total} reais")
else:
    desc = (total * 10) / 100
    total_final = total - desc
    print(f"Com o desconto de 10% aplicado, você pagará R${total_final:.2f} reais")


