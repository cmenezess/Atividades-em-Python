# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

if n1 > n2 and n1 > n3:
    print(n1)
    if n2 > n3:
        print(n2)
        print(n3)
    elif n3 > n2:
        print(n3)
        print(n2)
    elif n2 == n3:
        print(f"{n2} e {n3} possuem valores iguais.")

elif n2 > n1 and n2 > n3:
    print(n2)
    if n1 > n3:
        print(n1)
        print(n3)
    elif n3 > n1:
        print(n3)
        print(n1)
    elif n3 == n1:
        print(f"{n3} e {n1} possuem valores iguais.")

elif n3 > n1 and n3 > n2:
    print(n3)
    if n1 > n2:
        print(n1)
        print(n2)
    elif n2 > n1:
        print(n2)
        print(n1)
    elif n2 == n1:
        print(f"{n2} e {n1} possuem valores iguais.")

else:
    print("Todos os valores são iguais.")