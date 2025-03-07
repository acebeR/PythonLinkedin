# - Crie um conjunto\n"
numeros = {1,2,3}
# - Converta uma lista em um conjunto\n"
lista = [1,2,3,3,3]
conjunto = set(lista)
lista = list(conjunto)
print(lista)
# - Insira novos valores no conjunto\n"
conjunto.add(5)
print(conjunto)
# - Remova um elemento do conjunto\n"
conjunto.remove(3)
print(conjunto)
# - Verifique se um elemento está contino no conjunto"
print(2 in conjunto)
# - Crie uma tupla\n"
tupla = (2,3)
# - Imprima na tela um elemento da tupla\n"
print(tupla[0])
# - Crie uma função que retorne mais de um elemento\n"
def retorna_multiplos():
    nome = "João"
    idade = 25
    return nome, idade
# - Atribua cada elemento da função em uma variável"
nome,idade = retorna_multiplos()
print(nome, idade)