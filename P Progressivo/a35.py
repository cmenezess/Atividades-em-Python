# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                           Até 5 Kg               Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra           R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha          R$ 6,90 por Kg          R$ 7,80 por Kg
#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo = int(input("[1]Filé duplo \n[2]Alcatra \n[3]Picanha \nInforme o tipo de carne que deseja: "))
quantidade = float(input("Informe a quantidade desejada (kg): "))
pag = int(input("[1]Dinheiro \n[2]Cartão de crédito \n[3]Cartão de débito \n[4]Pix \n[5]Cartão Tabajara \nInforme a forma de pagamento: "))


if tipo == 1 and quantidade <= 5 and pag != 5:
    total = quantidade * 4.90
    print(f"Tipo: Filé duplo. Quantidade: {quantidade}. Preço: R${total}. Pagamento: {pag}. ")
elif tipo == 1 and quantidade > 5 and pag == 5:
    total = quantidade * 5.80
    desc = (5 * total) / 100
    total_final = total - desc
    print(f"Tipo: Filé duplo. Quantidade: {quantidade}. Preço: R${total}. Pagamento: {pag}. Desconto: R${desc}. Total final: R${total_final}")


if tipo == 2 and quantidade <= 5 and pag != 5:
    total = quantidade * 5.90
    print(f"Tipo: Alcatra. Quantidade: {quantidade}. Preço: R${total}. Pagamento: {pag}. ")
elif tipo == 2 and quantidade > 5 and pag == 5:
    total = quantidade * 6.80
    desc = (5 * total) / 100
    total_final = total - desc
    print(f"Tipo: Alcatra. Quantidade: {quantidade}. Preço: R${total}. Pagamento: {pag}. R$Desconto: {desc}. Total final: R${total_final}")


if tipo == 3 and quantidade <= 5 and pag != 5:
    total = quantidade * 5.90
    print(f"Tipo: Picanha. Quantidade: {quantidade}. Preço: R${total}. Pagamento: {pag}. ")
elif tipo == 3 and quantidade > 5 and pag == 5:
    total = quantidade * 6.80
    desc = (5 * total) / 100
    total_final = total - desc
    print(f"Tipo: Picanha. Quantidade: {quantidade}. Preço: R${total}. Pagamento: {pag}. Desconto: R${desc}. Total final: R${total_final}")
