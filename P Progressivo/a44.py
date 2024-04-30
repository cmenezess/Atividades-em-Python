# Seu professor de Matemática, cansado de ficar fazendo multiplicações para achar o fatorial,
# te encomendou um script em Python (obviamente pagou, pois você possui um certificado do curso de Python).

# Porém, ele quer fazer vários e vários cálculos.
# Nos exemplos anteriores a gente pede o número uma vez, mostra o fatorial e fecha o script.

# Ele não, ele quer um looping infinito, que só acabe quando ele fornecer o número 0 como entrada.

n = int(input("Fatorial de: "))

cont = 1
total = 1
while cont <= n:
    total *= cont
    cont += 1
    print(total)

    