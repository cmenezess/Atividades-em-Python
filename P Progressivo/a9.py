# Você foi contratado pela Caixa Econômica Federal para atualizar seu sistema.
# Como primeira tarefa,
# você vai criar um script que diga quanto cada ganhador da Mega-Sena vai receber, ao ter o prêmio dividido com outros ganhadores.

premio = float(input("Qual o valor do prêmio? R$"))
ganhadores = int(input("Quantas pessoas ganharam? "))

total = premio / ganhadores

print(f"Dividindo o prêmio para {ganhadores} ganhadores, ficará no valor de R${total:.2f}")