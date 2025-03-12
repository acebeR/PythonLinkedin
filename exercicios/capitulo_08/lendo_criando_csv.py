import csv

# Abrindo o arquivo CSV e imprimindo as linhas
try:
    with open("dados/populacao_mundial.csv", mode="r") as arquivo:
        leitor = csv.reader(arquivo)
        
        # Imprimindo o conteúdo do arquivo
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("O arquivo 'populacao_mundial.csv' não foi encontrado!")
# Abrindo o arquivo CSV com delimitador '\t' e imprimindo as linhas
# Listas fornecidas
cabecalho = ['pais', 'ano', '%_crescimento_populacional']
populacao_pais = ['Chile', 'Chile', 'Chile', 'Chile', 'Chile']
populacao_ano = ['1955', '1960', '1965', '1970', '1975']
populacao_crescimento_populacional = ['1.3', '1.7', '2.05', '2.33', '2.58']

# Criação do novo arquivo CSV
with open("dados/populacao_chile.csv", mode="w", newline='') as arquivo:
    escritor = csv.writer(arquivo)
    
    # Escreve o cabeçalho
    escritor.writerow(cabecalho)
    
    # Escreve os dados linha por linha
    for i in range(len(populacao_pais)):
        escritor.writerow([populacao_pais[i], populacao_ano[i], populacao_crescimento_populacional[i]])

print("Arquivo 'populacao_chile.csv' criado com sucesso!")
