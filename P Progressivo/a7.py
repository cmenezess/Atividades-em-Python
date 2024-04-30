# Sua primeira tarefa é criar um programa envolvendo a poupança.
# Você vai perguntar o valor inicial investido na poupança, a rentabilidade mensal,
# quantos meses o cliente deseja deixar o dinheiro investido e mostrar o valor final na conta do cliente do banco.

montante_inicial = float(input("Qual o montante inicial que vai ser investido? R$"))
rentabilidade_mensal = float(input("Qual a sua rentabilidade mensal, em porcentagem? "))
meses = int(input("Quantos meses que a aplicação vai ficar rendendo? "))

rent_men = rentabilidade_mensal / 100

valor_final = montante_inicial * (1 + rent_men)**meses

print(f"O valor final será de R${valor_final:.2f}")


# Um cliente pediu que o sistema do banco tivesse a seguinte função:
# Dizer o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha um valor 'vf',
# supondo que este dinheiro esteja rendendo uma rentabilidade 'i' mensal, em porcentagem esse 'i'.
# Faça um programa que pede o valor final, o tanto de meses que vai ficar aplicado, a rentabilidade
# e o script mostre o valor inicial que ele deve investir para atingir tal objetivo.

valor_obter = float(input("Qual valor final você deseja obter? R$"))
meses = int(input("Quantos meses ficará aplicado? R$"))
rentabilidade_mensal = float(input("Qual a sua rentabilidade mensal, em porcentagem? "))

rent_men = rentabilidade_mensal / 100

valor_inicial = valor_obter / (1 + rent_men) ** meses

print(f"O valor inicial que você deve investir para atingir seu objetivo é de R${valor_inicial}")