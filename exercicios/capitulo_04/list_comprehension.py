# - Crie uma lista com tipos de dados numérico\n"
lista = range(1, 101)
# - Usando list comprehension, multiplique cada item por 2 e armazene-os em uma nova lista\n"
nova_lista = [item * 2 for item in lista]
print(nova_lista)
# - Usando list comprehension, crie uma lista apenas com os itens divisíveis por 20\n"
nova_lista2 = [item for item in lista if item % 20 == 0]

print(nova_lista2)
# - Crie uma string\n"
# - Crie uma função que substitua as vírgulas da string por uma 'string vazia' e transforme o case das letras para minúscula\n"
def substituiCaracter(texto,caracterAnt,caracterNovo):
    return texto.replace(caracterAnt, caracterNovo).lower()

texto = 'Teste, teste teste,teste.'
texto = substituiCaracter(texto,',',' ')
# - Usando list comprehension, crie uma lista com as palavras normalizadas a partir da função do item acima\n"
lista_normalizada = [substituiCaracter(palavra, ',', '') for palavra in texto.split()]
print(lista_normalizada)