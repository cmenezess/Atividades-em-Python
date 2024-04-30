# Calculando a média em Python - Precedência de Operadores
# Você tem uma tia professora línguas.
# Ela é tão fera, que é professora tanto de Português e Inglês.

# Mas ela tem uma turma muito grande, e dá muito trabalho ficar somando e dividindo por 2, pois geralmente fica número quebrado no meio.

# Vamos ajudar sua tia?
# Crie um script que pede a nota de Português e a de Inglês, e forneça a média das duas notas.


np = float(input("Nota de português: "))
ni = float(input("Nota de inglês: "))
nm = float(input("Nota de matemática: "))
media = (np + ni + nm) / 3
print(f"A média do aluno é {media:.2f}") #:.2f determina quantas casas decimais terá