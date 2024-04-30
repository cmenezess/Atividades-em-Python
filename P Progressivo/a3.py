# Exercício 01:
# Crie um programa que exiba na tela seu nome completo, sua cidade, estado e data de nascimento.
# Para cada dado desse, crie uma variável apropriada. Use nomes que façam sentido
# ('cidade', 'estado' etc, nada de ficar criando variáveis com nomes 'a', 'b', 'x' ou 'y' - isso é um péssimo hábito entre programadores).
# Exiba tudo na tela, bonitinho e organizado.
nome = "Catarina Melo Menezes"
cidade = "Salvador"
estado = "Bahia"
data_nasc = "18/02/2000"
print(f"Nome: {nome} \nCidade: {cidade} \nEstado: {estado} \nData de nascimento: {data_nasc}")

print('-----------------------------------------------------------------------------------')
# Exercício 02:
# Crie um programa que exiba na tela o texto 'A melhor banda do mundo é [nome da banda] e a melhor música é [nome da música]'.
# O nome da banda e o nome da música devem estar declarados em duas variáveis diferentes.
banda = "Pearl Jam"
musica = "Black"
print(f"A melhor banda do mundo é {banda} e a melhor música é {musica}")

print('------------------------------------------------------------------------------------')
# Exercício: O seguinte código imprime todas as palavras reservadas (keywords) do Python, rode ele.
# import keyword
# print(keyword.kwlist)
import keyword
print(keyword.kwlist)