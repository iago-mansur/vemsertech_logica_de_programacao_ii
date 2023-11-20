# Lista bidimensional
lista_exemplo = [[1,2,3], [1,3,4], [1,4,5]]

print("Fazendo o unpacking de uma lista de listas:\n")
for (a, b, c) in lista_exemplo:
  print(a, b, c)

print("\n\nCom tuplas podemos multiplicar a estutura por um valor para replicarmos aquela quantidade N vezes (neste caso, N = 4)\n", (2, 3) * 4)

## Trocando valores de lugar
a = 5
b = 2
print("\n\nNúmeros antes da troca (tradicional):", a, b)

# Jeito tradicional
aux = a
a = b
b = aux
print("\n\nNúmeros depois da troca (tradicional):", a, b)

a = 5
b = 2
print("\n\nNúmeros antes da troca (pythônico):", a, b)

# Jeito 'pythônico'
a,b = (b,a) # a,b = b,a
print("\n\nNúmeros depois da troca (pythônico):", a, b)

c = 2, 3, 4
print("\n\nChecando o tipo da variável criada:", type(c))
# c[0] = 5 -> NO PUEDE!! Tuplas são IMUTÁVEIS

# Forma de adicionar elementos a uma tupla
print("\n\nChecando o tipo da variável criada:", type(c))

# Aqui estamos adicionando um novo elemento à tupla, por meio de concatenação (ficar atento a este formato de uma tupla com um único elemento)
c += (5,)

num1, _, num2 = (4, 5, 6)
print("\n\nFazendo o unpacking de valores, pulando o segundo valor da tupla:", num1, num2)

# Tuplas no contexto de função retornando múltiplos valores
def separaNome(nome_completo):
  nome, sobrenome = nome_completo.split(" ")
  return nome, sobrenome

resultado = separaNome("Luís Bicalho")
print("O resultado da separação foi:", resultado)

# Fatiamento
print("\n\nFatiando a tupla:", c[:2])

print("\n\nAbaixo um exemplos de uso da função zip (listas de nomes e notas de alunos):")

# Exemplo de uso da função zip
lista_nomes = ["Tamira", "Iago", "Marco", "Luís"]
lista_notas = [9.7, 0.3, 9.2, 9.1]
for i in range(len(lista_nomes)):
  print(f"O aluno {lista_nomes[i]} tirou {lista_notas[i]} na prova")

# Adicionando um valor à lista de nomes, temos o seguinte comportamento
lista_nomes += ["Orlando"]
print("\n\nVamos ver o que o zip faz:", list(zip(lista_nomes, lista_notas)))
print()

# Se comentarmos a linha abaixo, o strict=True faz o zip dar um erro
lista_nomes = ["Tamira", "Iago", "Marco", "Luís"]
for nome, nota in zip(lista_nomes, lista_notas, strict=True):
  print(f"O aluno {nome} tirou {nota} na prova")

# Abaixo vamos fazer a questão envolvendo o zip, mas sem o zip (por enquanto)
'''
Em programação, podemos fazer uso de diferentes listas para armazenar nossos dados para, posteriormente, unir informações destas listas. Por exemplo, podemos guardar em uma lista os nomes de funcionários de uma empresa e, em outra lista, os cargos que estes funcionários ocupam.

funcionarios = ["Paulo", "Andrea", "Marta"]
profissao = ["cientista de dados", "engenheiro de dados", "desenvolvedor"]
Dado essas duas listas, podemos querer exibir as duas informações conjuntamente da seguinte forma:

[('Paulo', 'cientista de dados'), ('Andrea', 'engenheiro de dados'), ('Marta', 'desenvolvedor')]
Podemos fazer isto por meio da função zip que recebe as duas listas e retorna uma saída como exposta acima. Além de exibir os valores, podemos fazer uso da função zip para diversas funcionalidades. Sabendo disso, crie uma função ultimoElementoLista2D() que receba uma lista de duas dimensões (isto é, uma lista de listas, na forma de matriz) e utilize o zip para retornar o último elemento de cada sublista.

Por exemplo, se tivermos a lista abaixo:

[[192, 193, 194],
 [507, 508, 509],
 [526, 527, 528, 529],
 [560, 561],
 [635, 636, 637]]
Retorne [194, 509, 529, 561, 637].
'''
lista_valores = [
  [192, 193, 194],
  [507, 508, 509],
  [526, 527, 528, 529],
  [560, 561],
  [635, 636, 637]
]
# Mesmo o enunciado pedindo para fazermos com zip, melhor fazer sem o uso dele. Printamos o zip abaixo para ver o que aparecia, e não parece ser útil para este contexto.
# print(list(zip(lista_valores)))

lista_resultado = []
for sublista in lista_valores:
  lista_resultado.append(sublista[-1])

print(lista_resultado)