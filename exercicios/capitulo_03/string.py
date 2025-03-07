# - Declare uma variável do tipo string"
nome = "Rebeca Carvalhedo"
# - Imprima apenas os primeiros 3 caracteres da sua string"
i = 0
for i in range(3):
    print(nome[i] + '\n')
    i += i
# - Converta toda a string para letras minúsculas\n"
print(nome.upper())
# - Converta toda a string para letras maiúsculas\n"
print(nome.lower())
# - Formate a string para que tenha apenas a primeira letra maiúscula\n"

def formataNome(nome):
    aux = nome[1:]
    primeira = nome[0]
    aux = primeira.upper() + aux
    return aux
print(formataNome(nome))
# - Formate a string para que a primeira letra de cada palavra seja maiúscula\n"

def formataPalavraPorPalavra(lista):
    lista_de_linhas = lista.split()
    retorno = ""
    for palavra in lista_de_linhas:
        retorno = retorno + formataNome(palavra) + " "
    return retorno
texto = "estou aprendendo python."
textoForma = formataPalavraPorPalavra(texto)
print(textoForma)
# - Inverta o case de todas as letras da string\n"
texto = "Estou APRENDENDO Python."
texto_invertido = texto.swapcase()

print(texto_invertido)  # Saída: eSTOU aprendendo pYTHON.

# - Formate uma string usando string format"
nome = "Rebeca"
idade = 26
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)

print(mensagem)
