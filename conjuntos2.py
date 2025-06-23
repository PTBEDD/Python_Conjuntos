# - Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# • os elementos que não mudaram
# • os novos elementos
# • os elementos que foram removidos

def comparar_listas(lista_ini, lista_alt):
  conj_ini = set(lista_ini)
  conj_alt = set(lista_alt)

  elementos_iguais = conj_ini.intersection(conj_alt)
  novos_elementos = conj_alt.difference(conj_ini)
  elementos_removidos = conj_ini.difference(conj_alt)

  print("Elementos que não mudaram: ", elementos_iguais)
  print("Novos elementos: ", novos_elementos)
  print("Elementos removidos: ", elementos_removidos)


lista1 = ['a', 'b', 'c', 'd', 'e']
lista2 = ['b', 'c', 'd', 'f', 'g']

comparar_listas(lista1, lista2)