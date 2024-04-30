# 4! = 4 x 3 x 2 x 1 = 24
#Fatorial:
n = int(input("Fatorial de: "))
total = 1
cont = 1
while cont <= n:
    total *= cont
    cont += 1
    print(total)

#Fatorial usando for:
n = int(input("Fatorial de: "))
cont = 1
for i in range(1, n+1):
    cont *= i
    print(cont)

