# - Importe as bibliotecas requests e csv\n"
import requests
import csv

# - Faça uma requisição do tipo 'get' para o link 'http://dados.recife.pe.gov.br/dataset/2676fd74-8b40-4248-a1da-0dc45f176b7b/resource/7c005351-2d14-46cf-b2f0-6622a5553b30/download/ocorrencias2022.csv'\n"
# URL do arquivo CSV
url = 'http://dados.recife.pe.gov.br/dataset/2676fd74-8b40-4248-a1da-0dc45f176b7b/resource/7c005351-2d14-46cf-b2f0-6622a5553b30/download/ocorrencias2022.csv'

# Realizando a requisição GET
response = requests.get(url)

# Imprimindo o código de status da requisição
print(f"Código de status da requisição: {response.status_code}")

# Verificando se a requisição foi bem-sucedida (status 200)
if response.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Houve um erro na requisição.")

# - Imprima na tela o código com o status da requisição- Imprima na tela os metadados do arquivo\n"
# Imprimindo os metadados da requisição
print("Metadados da requisição:")
print(f"Tipo de conteúdo: {response.headers['Content-Type']}")
print(f"Conteúdo (primeiros 500 caracteres): {response.text[:500]}")

# - Salve os dados em um arquivo csv, na pasta 'dados'\n"
# Salvando o conteúdo no arquivo CSV
arquivo_csv = 'dados/ocorrencias_2022.csv'

# Abrindo o arquivo para salvar o conteúdo
with open(arquivo_csv, 'wb') as f:
    f.write(response.content)

print(f"Dados salvos em: {arquivo_csv}")

# - Leia o arquivo csv em formato de dicionário e imprima na tela as 5 primeiras linhas\n"
# Lendo o arquivo CSV em formato de dicionário
with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    
    # Imprimindo as 5 primeiras linhas
    print("Primeiras 5 linhas do arquivo:")
    for i, linha in enumerate(leitor):
        if i < 5:
            print(linha)
        else:
            break

# - Filtre apenas as linhas cujo o valor da coluna 'municipio' corresponda a 'RECIFE' e a o valor da coluna 'data' corresponda a '2022-01-01'\n"
# Filtrando as linhas com 'municipio' == 'RECIFE' e 'data' == '2022-01-01'
ocorrencias_recife_2022 = []

with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    
    for linha in leitor:
        if linha['municipio'] == 'RECIFE' and linha['data'] == '2022-01-01':
            ocorrencias_recife_2022.append(linha)

# Imprimindo o total de ocorrências resultantes do filtro
print(f"Total de ocorrências em RECIFE no dia 2022-01-01: {len(ocorrencias_recife_2022)}")

# - Imprima na tela o total de ocorrências resultantes do filtro do item anterior\n"
# - Leia o arquivo \"dados/populacao_mundial.csv\" em formato de dicionário e imprima na tela\n"
# Lendo o arquivo 'dados/populacao_mundial.csv' em formato de dicionário
populacao_mundial_arquivo = 'dados/populacao_mundial.csv'

with open(populacao_mundial_arquivo, mode='r', newline='', encoding='utf-8') as file:
    leitor = csv.DictReader(file)
    
    # Imprimindo o conteúdo do arquivo
    print("Conteúdo do arquivo 'populacao_mundial.csv':")
    for linha in leitor:
        print(linha)
