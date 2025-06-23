# - Faça uma função que receba um dicionário como acima e retorne um conjunto com quais estados estão representados.

def estados_representados(dicionario):
  return set(dicionario.values())

# - Faça uma função que receba dois dicionários como acima e retorne uma LISTA dos estados que estão nos dois dicionários, em ordem alfabética da sigla. Cada estado só deve aparecer uma vez na lista.

def estados_comuns(dicionario1, dicionario2):
  estados1 = set(dicionario1.values())
  estados2 = set(dicionario2.values())
  comuns = estados1.intersection(estados2)
  return sorted(list(comuns))

# - Exemplo: cidades = {'Osasco':'SP', 'Caldas':'MG', 'Uberaba':'MG', 'Vitória':'ES', 'Cláudio':'MG'}

cidades1 = {'Carapicuiba':'SP', 'Recife':'PE', 'Ubatuba':'SP', 'Vitória':'ES', 'Paraty':'RJ'}
cidades2 = {'Jandira':'SP', 'Manaus':'AM', 'Rio de Janeiro':'RJ', 'Curitiba':'PR', 'João Pessoa':'PB'}

print("Estados representados: ", estados_representados(cidades1))
print("Estados comuns: ", estados_comuns(cidades1, cidades2))