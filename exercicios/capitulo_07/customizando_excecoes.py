# Definindo uma exceção personalizada para o servidor
class ServidorWebErro(Exception):
    def __init__(self, mensagem, codigo_erro):
        super().__init__(mensagem)
        self.codigo_erro = codigo_erro

# Função simulando um servidor web simples
def processar_requisicao(url):
    try:
        if url == "/erro":
            raise ServidorWebErro("Erro interno do servidor!", 500)
        elif url == "/pagina_nao_encontrada":
            raise ServidorWebErro("Página não encontrada!", 404)
        elif url == "/sucesso":
            return "Página carregada com sucesso!"
        else:
            raise ServidorWebErro("URL desconhecida!", 400)
    except ServidorWebErro as e:
        return f"Erro {e.codigo_erro}: {e}"

# Testando as requisições
print(processar_requisicao("/sucesso")) 
print(processar_requisicao("/erro"))  
print(processar_requisicao("/pagina_nao_encontrada")) 
print(processar_requisicao("/outro_endereco")) 
