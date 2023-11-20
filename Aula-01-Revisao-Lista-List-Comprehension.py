# nota_orlando = 9.5
# nota_tamira = 9.6
# nota_iago_mansur = 4.6
# nota_luis_bicalho = 3.6

# lista_aluno = ["Luís", 9.4, 1111, True, ["MAT123", "FIS567"]]
# lista_notas = [9.5, 9.6, 4.6, 3.6]

# print(lista_notas)

# for nota in lista_notas:
#   print(nota)

# print(range(len(lista_notas)))
# for i in range(len(lista_notas)):
#   print(lista_notas[i])

# print("\n\nVisualizando o que tem 'dentro' do enumerate:\n")
# print(list(enumerate(lista_notas)))

# print("\n\nVisualizando cada valor dentro da tupla:\n")
# for (i, nota) in enumerate(lista_notas):
#   print(i, nota)

# print("\n\nVisualizando cada tupla:\n")
# for elem in enumerate(lista_notas):
#   print(elem)

# print("A nota do Iago é:", lista_notas[2])
# print("A nota do último aluno da lista é:", lista_notas[-1])

# print("Lista contendo as duas primeiras notas:", lista_notas[:2])

# inicio = 1
# fim = 3
# print("Lista contendo as duas notas do meio:", lista_notas[inicio:fim])
# print("Lista sem o primeiro aluno:", lista_notas[1:])
# print("Lista invertida:", lista_notas[::-1])


# ####### TUPLA
# lista_exemplo = [[1,2,3], [1,3,4], [1,4,5]]

# for (a, b, c) in lista_exemplo:
#   print(a, b, c)

# print((2, 3) * 4)

# # Trocando valores de lugar
# a = 5
# b = 2
# print(a, b)
# # aux = a
# # a = b
# # b = aux
# # print(a, b)

# a,b = (b,a) # a,b = b,a
# print(a, b)

# c = 2, 3, 4
# print(type(c))
# # c[0] = 5 -> NO PUEDE!!

# c += (5,)

# num1, _, num2 = (4, 5, 6)
# print(num1, num2)

# def separaNome(nome_completo):
#   nome, sobrenome = nome_completo.split(" ")
#   return nome, sobrenome

# resultado = separaNome("Luís Bicalho")
# print("O resultado da separação foi:", resultado)

# # Fatiamento
# print("\n\nFatiando a tupla:", c[:2])

# print()
# # Exemplo de uso da função zip
# lista_nomes = ["Tamira", "Iago", "Marco", "Luís"]
# lista_notas = [9.7, 0.3, 9.2, 9.1]
# for i in range(len(lista_nomes)):
#   print(f"O aluno {lista_nomes[i]} tirou {lista_notas[i]} na prova")

# # lista_nomes += ["Orlando"]
# print("\n\nVamos ver o que o zip faz:", list(zip(lista_nomes, lista_notas)))
# print()

# for nome, nota in zip(lista_nomes, lista_notas, strict=True):
#   print(f"O aluno {nome} tirou {nota} na prova")

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
# print(list(zip(lista_valores)))

lista_resultado = []
for sublista in lista_valores:
  lista_resultado.append(sublista[-1])

print(lista_resultado)