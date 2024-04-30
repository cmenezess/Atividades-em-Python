# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#     Se o usuário informar o valor de A igual a zero,
# a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;


#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# PS: digite 'import math' no início de seu script. Para achar a raiz quadrada da variável x, faça: math.sqrt(x)

import math
a = float(input("Informe o valor de a: "))

if a > 0:
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))

    delta = (b**2) - (4 * a * c)
    print(delta)
    if delta < 0:
        print("A equação não possui valores reais.")
    elif delta == 0:
        xlinha = (- b + (math.sqrt(delta))) / (2 * a)
        print(xlinha)
    else:
        xlinha = (- b + (math.sqrt(delta))) / (2 * a)
        print(xlinha)
        x_2_linha = (- b - (math.sqrt(delta))) / (2 * a)
        print(x_2_linha)
else:
    print("Não é uma equeção do segundo grau.")