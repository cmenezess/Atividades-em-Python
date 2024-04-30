n = int(input("Informe um número inteiro: "))
#Colar um número ao lado do outro ao invés de um abaixo do outro:
n1 = 0
while n1 <= n:
    n1 += 1
    if n1 % 2 == 0:
        print(n1, end=" ")