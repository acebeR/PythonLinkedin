# Classe Gata
class Gata:
    def __init__(self, **kwargs):
        self._patas = kwargs['patas']
        self._nome = kwargs['nome'] if 'nome' in kwargs else 'Nísia'
        self._cor = kwargs['cor']
        self._comprimento_pelagem = kwargs['comprimento_pelagem']
        self._idade = kwargs['idade'] if 'idade' in kwargs else 0 

    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self._idade

    def getCor(self):
        return self._cor

    def setCor(self, nova_cor='cinza'):
        if nova_cor:
            self._cor = nova_cor
        return self._cor
    
    def som(self):
        return f'{self._nome} é uma gata que mia.'

# Subclasse Siames (herdando de Gata)
class Siames(Gata):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        # Adiciona o valor de idade, caso não seja fornecido
        self._idade = kwargs['idade'] if 'idade' in kwargs else 0

    # Modificando o comportamento do método som
    def som(self):
        return f'Gatos da espécie siamesa miam pouco.'

# Instanciando objetos e testando
nisia = Gata(patas=3, cor='laranja', comprimento_pelagem='médio', nome='Nísia', idade=2)
print(nisia.getNome())  
print(nisia.getIdade())
print(nisia.som()) 

nisia_siamesa = Siames(patas=3, cor='branca', comprimento_pelagem='curto', nome='Luna', idade=3)
print(nisia_siamesa.getNome()) 
print(nisia_siamesa.getIdade()) 
print(nisia_siamesa.som())  
