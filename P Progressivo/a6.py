# Sua primeira tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.
# Você deve mostrar uma tabela contendo:
# Preço original do produto
# Valor do desconto em R$ (tipo 'Você ganho R$ xx,xx de desconto')
# Valor do produto com o desconto
preco_orig = float(input("Informe o valor do produto: R$"))

desconto = (preco_orig * 20) / 100
produto_desconto = preco_orig - desconto

print(f"Valor do produto: R${preco_orig}")
print(f"Você ganhou um desconto de R${desconto}")
print(f"O valor final do produto ficou R${produto_desconto}")


# A loja percebeu que não quer dar 20% em tudo.
# Quer dar 20% em algumas coisas, 10% em outra, nada em outro produto e até 30% em alguns outros produtos.
preco_orig = float(input("Informe o valor do produto: R$"))
desconto = int(input("Qual o valor do desconto? "))

desconto_tot = (preco_orig * desconto) / 100
produto_desconto = preco_orig - desconto_tot

print(f"Valor do produto: R${preco_orig}")
print(f"Você ganhou um desconto de R${desconto_tot}")
print(f"O valor final do produto ficou R${produto_desconto}")