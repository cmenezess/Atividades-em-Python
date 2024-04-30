# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

sal = float(input("Informe teu salário: R$"))

if sal < 280:
    novo_sal = (sal * 20) / 100
    novo_sal1 = sal + novo_sal
    print(f"Salário antes do reajuste: R${sal} \nAumento percentual: 20% \nValor do aumento: R${novo_sal} \nNovo salário:R${novo_sal1}")

elif sal >= 280 and sal < 700:
    novo_sal = (sal * 15) / 100
    novo_sal1 = sal + novo_sal
    print(f"Salário antes do reajuste: R${sal} \nAumento percentual: 15% \nValor do aumento: R${novo_sal} \nNovo salário:R${novo_sal1}")

elif sal >= 700 and sal < 1500:
    novo_sal = (sal * 10) / 100
    novo_sal1 = sal + novo_sal
    print(f"Salário antes do reajuste: R${sal} \nAumento percentual: 10% \nValor do aumento: R${novo_sal} \nNovo salário:R${novo_sal1}")

else:
    novo_sal = (sal * 5) / 100
    novo_sal1 = sal + novo_sal
    print(f"Salário antes do reajuste: R${sal} \nAumento percentual: 5% \nValor do aumento: R${novo_sal} \nNovo salário:R${novo_sal1}")

