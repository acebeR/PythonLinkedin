# Definindo a classe Sala
class Sala:
    cor = "branca"  
    
    def __init__(self, tamanho, capacidade, cor):
        self.tamanho = tamanho  
        self.capacidade = capacidade  
        self.__cor = cor  

    def modificar_cor(self, nova_cor):
        self.__cor = nova_cor

    def obter_cor(self):
        return self.__cor
    
    def exibir_informacoes(self):
        print(f"Tamanho da sala: {self.tamanho} m²")
        print(f"Capacidade: {self.capacidade} pessoas")
        print(f"Cor da sala: {self.obter_cor()}")  # Acessando a variável privada

sala1 = Sala(50, 30, "azul")

print(f"Cor da sala (variável de classe): {Sala.cor}")

sala1.modificar_cor("verde")

sala1.exibir_informacoes()

print(f"Cor modificada da sala1 (instância): {sala1.obter_cor()}")
