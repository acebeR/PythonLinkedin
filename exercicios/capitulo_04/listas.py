# - Crie um objeto iterável com a função range\n"
objeto = range(1,20)
# - Converta essa objeto para uma lista\n"
lista = list(objeto)
print(lista)
# - Imprima na tela 3 elementos dessa lista\n"
print(lista[0],lista[1]),lista[2]
# - Insira um item no final da lista\n"
lista.append(2)
print(lista)
# - Substitua o valor do item de índice 0\n"
lista[0] = 5
print(lista)
# - Remova um dos itens da lista\n"
lista.pop()
print(lista)
# - Copie a lista para outra variável"
lista2 = lista
print(lista2)
