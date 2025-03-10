# - Crie um dicionário\n"
dicionario = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'
}
# - Faza uma lista com as chaves do dicionário criado\n"
chaves = list(dicionario.keys())
print("Chaves do dicionário:", chaves)
# - Faça um objeto iterável com os valores do dicionário criado\n"
valores = dicionario.values()
print("Valores do dicionário:", list(valores))
# - Localize o valor correspondente a uma chave do dicionário\n"
chave_procurada = 'idade'
valor_correspondente = dicionario.get(chave_procurada, "Chave não encontrada")
print(f"Valor correspondente à chave '{chave_procurada}': {valor_correspondente}")
# - Insira um novo par de chave-valor no dicionário\n"
dicionario['profissão'] = 'Engenheiro'
print("Dicionário após inserção de novo par chave-valor:", dicionario)
# - Usando o módulo collections, crie um dicionário cujos o valor padrão serão listas\n"
from collections import defaultdict

dicionario_de_listas = defaultdict(list)
# - Adicione um novo par de chave-valor no dicionário de listas\n"
dicionario_de_listas['frutas'].append('maçã')
dicionario_de_listas['frutas'].append('banana')
dicionario_de_listas['vegetais'].append('cenoura')

print("Dicionário de listas:", dict(dicionario_de_listas))
# - Localize um valor da lista correspondente a uma chave do dicionário de listas"
chave_lista_procurada = 'frutas'
valores_lista = dicionario_de_listas.get(chave_lista_procurada, "Chave não encontrada")
print(f"Valores da lista correspondente à chave '{chave_lista_procurada}': {valores_lista}")
 