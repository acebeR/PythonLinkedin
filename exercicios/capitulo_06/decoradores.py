# Função simples que imprime uma mensagem
def saudacao(nome):
    return f"Olá, {nome}!"

# Decorador para alterar o comportamento da função
def decorador(func):
    def wrapper(nome):
        # Modificando o comportamento da função
        mensagem = func(nome)
        return f"{mensagem} Como você está?"
    return wrapper

# Aplicando o decorador à função saudacao
saudacao = decorador(saudacao)

# Executando a função decorada
print(saudacao("Rebeca"))
