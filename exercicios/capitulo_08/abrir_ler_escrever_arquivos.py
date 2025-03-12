# - Abra o arquivo \"dados/a_luta_carmen_dolores_trecho.txt\" em modo leitura\n"
# Abrindo um arquivo para leitura
try:
    arquivo = open("dados/a_luta_carmen_dolores_trecho.txt", 'r')
    conteudo = arquivo.read()  
    print(conteudo)  
    arquivo.close()  
except FileNotFoundError:
    print("O arquivo não foi encontrado!")


# - Abra o arquivo \"dados/a_luta_carmen_dolores_trecho.txt\" em modo leitura usando a palavra 
# reservada \"with\"\n"
# Abrindo um arquivo para escrita (vai criar ou sobrescrever o arquivo)
arquivo = open("dados/a_luta_carmen_dolores_trecho.txt", "w")
arquivo.write("Teste Rebeca\n")
arquivo.close()

# - Crie uma lista com as linhas do arquivo e imprima na tela\n"
# Abrindo o arquivo e lendo as linhas em uma lista
try:
    with open("dados/a_luta_carmen_dolores_trecho.txt", "r") as arquivo:
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e as armazena em uma lista

    # Imprimindo as linhas na tela
    print("Linhas do arquivo:")
    for linha in linhas:
        print(linha.strip()) 
except FileNotFoundError:
    print("O arquivo não foi encontrado!")

# - Abra o arquivo \"dados/a_luta_carmen_dolores_trecho.txt\" em modo append e adicione 
# uma nova linha em seu conteúdo\n"
# Caminho do arquivo
caminho_arquivo = "dados/a_luta_carmen_dolores_trecho.txt"

# Abrindo o arquivo em modo append
try:
    with open(caminho_arquivo, "a") as arquivo:
        # Escrevendo uma nova linha no final do arquivo
        arquivo.write("\nEsta é uma nova linha adicionada ao final do arquivo.")

    print("Nova linha adicionada com sucesso!")
except FileNotFoundError:
    print(f"O arquivo {caminho_arquivo} não foi encontrado!")

# - Copie o conteúdo do arquivo \"dados/a_luta_carmen_dolores_trecho.txt\" para um 
# novo arquivo\n"
# Caminho do arquivo de origem e do arquivo de destino
caminho_arquivo_origem = "dados/a_luta_carmen_dolores_trecho.txt"
caminho_arquivo_destino = "dados/copia_a_luta_carmen_dolores_trecho.txt"

try:
    # Abrindo o arquivo de origem para leitura e o arquivo de destino para escrita
    with open(caminho_arquivo_origem, "r") as origem:
        conteudo = origem.read()  # Lê todo o conteúdo do arquivo de origem
    
    with open(caminho_arquivo_destino, "w") as destino:
        destino.write(conteudo)  # Escreve o conteúdo no arquivo de destino
    
    print("Conteúdo copiado com sucesso!")
except FileNotFoundError:
    print(f"O arquivo {caminho_arquivo_origem} não foi encontrado!")
except IOError as e:
    print(f"Ocorreu um erro ao manipular os arquivos: {e}")
