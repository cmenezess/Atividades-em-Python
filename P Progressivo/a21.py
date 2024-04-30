# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#     Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#     Salário Bruto: (5 * 220)        : R$ 1100,00
#     (-) IR (5%)                     : R$   55,00 
#     (-) INSS ( 10%)                 : R$  110,00
#     FGTS (11%)                      : R$  121,00
#     Total de descontos              : R$  165,00
#     Salário Liquido                 : R$  935,00

horas = float(input("Quanto vale a hora trabalhada? R$"))
quantidade = int(input("Informe quantas horas você trabalhou no mês: "))

total = horas * quantidade

if total <= 900:
    inss = (total * 10) / 100
    fgts = (total * 11) / 100
    total_descontos = inss + fgts
    sal_liquido = total - total_descontos
    print(f"Salário bruto: R${total} \nINSS: R${inss} \nFGTS: R${fgts} \nTotal de descontos: R${total_descontos} \nSalário líquio: R${sal_liquido}")

elif total > 900 and total <= 1500:
    inss = (total * 10) / 100
    fgts = (total * 11) / 100
    imposto = (total * 5) / 100
    total_descontos = inss + imposto
    sal_liquido = total - total_descontos
    print(f"Salário bruto: R${total} \nImposto de renda: R${imposto} \nINSS: R${inss} \nFGTS: R${fgts} \nTotal de descontos: R${total_descontos} \nSalário líquio: R${sal_liquido}")

elif total > 1500 and total <= 2500:
    inss = (total * 10) / 100
    fgts = (total * 11) / 100
    imposto = (total * 10) / 100
    total_descontos = inss + imposto
    sal_liquido = total - total_descontos
    print(f"Salário bruto: R${total} \nImposto de renda: R${imposto} \nINSS: R${inss} \nFGTS: R${fgts} \nTotal de descontos: R${total_descontos} \nSalário líquio: R${sal_liquido}")

else:
    inss = (total * 10) / 100
    fgts = (total * 11) / 100
    imposto = (total * 20) / 100
    total_descontos = inss + imposto
    sal_liquido = total - total_descontos
    print(f"Salário bruto: R${total} \nImposto de renda: R${imposto} \nINSS: R${inss} \nFGTS: R${fgts} \nTotal de descontos: R${total_descontos} \nSalário líquio: R${sal_liquido}")
