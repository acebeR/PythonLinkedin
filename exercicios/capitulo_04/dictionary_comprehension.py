# - Crie uma lista\n"
lista = ["maçã", "banana", "kiwi", "morango", "abacaxi"]
print("Lista:", lista)
# - Usando o recurso dictionary comprehension, crie um dicionário cuja a chave é o comprimento do item e o valor, o próprio item da lista.\n"
dicionario_comprimento = {len(item): item for item in lista}
print("Dicionário com comprimento como chave:", dicionario_comprimento)
# - Crie uma lista de tuplas\n"
lista_tuplas = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
print("Lista de tuplas:", lista_tuplas)
# - Usando o recurso dictionary comprehension, crie um dicionário cuja a chave é o primeiro item da tupla e o valor, o segundo\n"
dicionario_tuplas = {tupla[0]: tupla[1] for tupla in lista_tuplas}
print("Dicionário a partir das tuplas:", dicionario_tuplas)
# - Crie um dicionário\n"
dicionario_original = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'
}
print("Dicionário original:", dicionario_original)
# - Usando o recurso dictionary comprehension, crie um novo dicionário cuja a chave é uma maniputação do valor\n"
dicionario_modificado = {chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in dicionario_original.items()}
print("Dicionário com valores manipulados:", dicionario_modificado)
# - Usando o recurso dictionary comprehension, crie um dicionário só com chaves com commprimento menor ou igual a 3\n"
dicionario_chaves_curta = {chave: valor for chave, valor in dicionario_original.items() if len(chave) <= 3}
print("Dicionário com chaves de comprimento <= 3:", dicionario_chaves_curta)