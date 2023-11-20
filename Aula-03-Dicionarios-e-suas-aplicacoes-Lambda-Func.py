# Exemplo com duas listas
lista_nomes = ["Tamira", "Iago", "Marco", "Luís"]
lista_notas = [9.7, 0.3, 9.2, 9.1]
indice_marco = lista_nomes.index("Marco")
print("É desta maneira que acessaríamos a nota do Marco:", lista_notas[indice_marco])

# Como podemos representar isso usando dicionários, será que fica melhor?
dict_alunos = {
  "Tamira": 9.7,
  "Iago": 1.2,
  "Marco": 9.2,
  "Luís": 9.1,
  "Eduardo": 8.9,
}

print("\n\nDicionário de alunos:\n", dict_alunos)

dicionario_maluco = {
  "olá": "oi",
  1111: "Luís Fernando",
  (60, 100): "Melhor idade",
}
print("\n\nDicionário loucaço:\n", dicionario_maluco)

# Podemos criar um dicionário a partir da junção das duas listas usando zip (conversão para dict)?
print("\n\nDicionario a partir de um zip:", dict(zip(lista_nomes, lista_notas)))

# Com isso podemos acessar a nota usando o nome como indexador/chave
print("\n\nAcessando a nota do Luís do dicionário:", dict_alunos["Luís"])

# "Mas Luís, dicionários são imutáveis igual às tuplas?!"
# Não, eu posso criar chaves novas, desde que eu atribua um valor a ela
# dict_alunos["Orlando"] = 9.6

# Uma das formas de checar se uma chave já existe no meu dicionário
if "Orlando" in dict_alunos:
  print("\n\nAcessando a nota do Orlando do dicionário (get):", dict_alunos["Orlando"])

nota_orlando = dict_alunos.get("Orlando", -1)
print("\n\nAcessando a nota do Orlando do dicionário (get):", nota_orlando)

# Percorrendo dicionários:
print("\n\nPercorrendo usando for-in-keys:\n")
for key in dict_alunos.keys():
  print(key, dict_alunos[key])

print("\n\nPercorrendo usando for-in-dict:\n")
for key in dict_alunos:
  print(key, dict_alunos[key])

print("\nO que tem dentro do dict.keys()?", list(dict_alunos.keys()))

print("\n\nPercorrendo usando for-in-values:\n")
for value in dict_alunos.values():
  print(value)

print("O que tem dentro do dict.values()?", list(dict_alunos.values()))

print("\n\nPercorrendo usando for-in-items:\n")
for key, value in dict_alunos.items():
  print(key, value)

print("O que tem dentro do dict.items()?", list(dict_alunos.items()))

# Voltando para a lista representando um aluno, como podemos representar ela em formato de dicionário?
lista_aluno = ["Luís", 9.4, 1111, True, ["MAT123", "FIS567"]]
print("\n\nLista representando um aluno e suas infos:\n", lista_aluno)

dict_aluno = {
  "Nome": "Luís",
  "CR": 9.4,
  "Matrícula": 1111,
  "Matrícula Ativa": True,
  "Cursando": ["MAT123", "FIS567"]
}
print("\n\nDicionário representando um aluno e suas infos:\n", dict_aluno)

# Adicionando uma nova disciplina no DE-PARA
dict_aluno["Cursando"].append("INF124")
print("\n\nAdicionando disciplina no DE-PARA:", dict_aluno["Cursando"])

# Nome do aluno está incompleto, vamos alterar
dict_aluno["Nome"] = "Luís Fernando Teixeira Bicalho"
print("\n\nAtualizando nome do aluno:", dict_aluno["Nome"])

# Atualizando um dicionário já existente (update)
dict_aluno.update({
  "Notas Período Corrente": [8.1, 2.3, 5.8],
  "Período Atual": 5,
  "CPF": "123.456.789-00",
})
print("\n\nAdicionando novas prpriedades ao dicionário que representa um aluno:", dict_aluno)

# Removendo uma chave de um dicionário
# del dict_aluno["CPF"]
dict_aluno.pop("CPF")
print("\n\nRemovendo a chave CPF do meu dicionário:", dict_aluno)

# E se fossem mútiplos alunos?
lista_alunos = [
  {
    "Nome": "Luís",
    "CR": 9.4,
    "Matrícula": 1111,
    "Matrícula Ativa": True,
    "Cursando": ["MAT123", "FIS567"]
  },
  {
    "Nome": "Myrna",
    "CR": 9.4,
    "Matrícula": 2222,
    "Matrícula Ativa": False,
    "Cursando": ["MAT1234", "FIS5672", "INF1023"]
  },
  {
    "Nome": "Ronaldo",
    "CR": 9.5,
    "Matrícula": 3333,
    "Matrícula Ativa": True,
    "Cursando": ["MAT123", "FIS567"]
  }
]

print("\n\nLista de dicionários representando múltiplos alunos e suas infos:\n", lista_alunos)

print("\n\nAcessando o nome do segundo aluno:", lista_alunos[1]["Nome"])