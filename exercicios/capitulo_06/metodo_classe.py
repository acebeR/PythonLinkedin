# - Crie uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    # Método get para acessar o nome
    def get_nome(self):
        return self.__nome

    # Método set para modificar o nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    # Método get para acessar a idade
    def get_idade(self):
        return self.__idade

    # Método set para modificar a idade
    def set_idade(self, nova_idade):
        self.__idade = nova_idade

# Instanciando a classe
pessoa1 = Pessoa("João", 30)

# Imprimindo os valores antes da modificação
print(f"Nome antes da modificação: {pessoa1.get_nome()}")
print(f"Idade antes da modificação: {pessoa1.get_idade()}")

# Modificando o nome e a idade
pessoa1.set_nome("Carlos")
pessoa1.set_idade(35)

# Imprimindo os valores após a modificação
print(f"Nome após a modificação: {pessoa1.get_nome()}")
print(f"Idade após a modificação: {pessoa1.get_idade()}")
