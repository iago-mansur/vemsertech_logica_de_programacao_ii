# -*- coding: utf-8 -*-
"""Aula04_ListaDicionarios.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lOsnZMKN7ikFah9G-mlJySlIbkNc4qxJ

# Lista de dicionários e suas aplicações

Lista de dicionários representando múltiplos alunos e suas infos:
"""

lista_alunos = [
  {
    "Nome": "Luís",
    "Sobrenome": "Bicalho",
    "CR": 9.4,
    "Matrícula": 1111,
    "Matrícula Ativa": True,
    "Cursando": ["MAT123", "FIS567"]
  },
  {
    "Nome": "Myrna",
    "Sobrenome": "Martinelli",
    "CR": 9.4,
    "Matrícula": 2222,
    "Matrícula Ativa": False,
    "Cursando": ["MAT1234", "FIS5672", "INF1023"]
  },
  {
    "Nome": "Ronaldo",
    "Sobrenome": "Scarpate",
    "CR": 9.5,
    "Matrícula": 3333,
    "Matrícula Ativa": True,
    "Cursando": ["MAT123", "FIS567"]
  }
]
print(lista_alunos)

"""Mostrando cada propriedade e cada valor associado a ela, para cada aluno:"""

for aluno in lista_alunos:
  for prop, val in aluno.items():
    print(prop, val)
  print()

"""Criar uma função que extraia uma lista de nomes do dicionário recebido por parâmetro:"""

def getNomes(lista):
  lista_nomes = []
  for aluno in lista:
    lista_nomes.append(aluno["Nome"])
  return lista_nomes

print("Segue a lista de nomes solicitada:", getNomes(lista_alunos))

"""Percorrendo dicionários usando funções de alta ordem (passando funções por parâmetro):"""

def getNome(aluno):
  return aluno['Nome'] + ' ' + aluno["Sobrenome"]

# Esta é a implementação de como o map funciona por dentro (mais ou menos)
def mapNomes(getNome, lista):
  lista_nomes = []
  for aluno in lista:
    lista_nomes.append(getNome(aluno))
  return lista_nomes

print(list(mapNomes(getNome, lista_alunos)))
print(list(map(getNome, lista_alunos)))

"""Vamos olhar pra ver o que tem dentro da variável "getNome" (spoiler: ela guarda a referência para uma função)"""

getNome

"""Tem jeito mais bonito/elegante de fazer isso? Sim, com lambda functions (funções anônimas)!"""

# def nomedafuncao(x, y, z) -> lambda x, y, z:
# E tudo que é passado após os "dois pontos" é considerando como o retorno da função

print("\n", list(map(lambda a: a['Nome'] + ' ' + a["Sobrenome"], lista_alunos)))

# getNome = lambda a: a['Nome'] + ' ' + a["Sobrenome"]
# print(list(map(getNome, lista_alunos)))

"""Outras funções importantes (filter e reduce)"""

alunos_matriculados = list(filter(lambda a: a["Matrícula Ativa"], lista_alunos))
alunos_matriculados

list(map(lambda a: a["Nome"], alunos_matriculados))

"""Quero o nome de todos os alunos que estão cursando mais de duas matérias:"""

list(filter(lambda a: len(a["Cursando"]) > 2, lista_alunos))

"""Calcular o CR médio dos alunos:

Para utilizar o reduce, é necessário importar ele da biblioteca functools
"""

from functools import reduce

"""Agora um exemplo de uso do reduce: Como podemos obter a média dos CRs dos alunos?"""

# Forma de fazer sem lambda function
def funcao(soma, aluno):
  cr_atual = aluno["CR"]
  print(f"Soma atual: {soma} - CR Atual {cr_atual}")
  return soma + aluno["CR"]

# Obtendo a média dividindo a soma pela quantidade de alunos (len da lista)
print("Média:", reduce(funcao, lista_alunos, 0)/len(lista_alunos))

# Forma de fazer com lambda function
soma_CRs = reduce(lambda soma, aluno: soma + aluno["CR"], lista_alunos, 0)

# Obtendo a média dividindo a soma pela quantidade de alunos (len da lista)
print("Média:", soma_CRs/len(lista_alunos))

"""Mas e aquele tal de "list comprehension"?"""



"""Estes dicionários podem vir de arquivos!"""
