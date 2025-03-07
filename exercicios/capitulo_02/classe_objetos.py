# - Crie uma classe com 3 atributos"
class Sala:
    def __init__(self,id,professor,qtdMaxAlunos):
        self.id = id
        self.professor = professor
        self.qtdMaxAlunos = qtdMaxAlunos
# - Defina um método para a classe"
    def imprime(self):
        print('===== Sala '+ str(self.id) +'=====')
        print('Professor: '+ str(self.professor))
        print('Quantidade Maxima de alunos: ' + str(self.qtdMaxAlunos))
        print('=======================')
# - Instancie a classe"
sala = Sala(1,'Ana Cecília Vieira',100)
# - Execute o método"
sala.imprime()
