import math

# Função que recebe dois números e uma operação matemática
def calculadora(*args, operacao):
    # Verificando a operação e realizando a ação
    if operacao == 'soma':
        resultado = sum(args)  # Soma todos os argumentos
    elif operacao == 'multiplicacao':
        resultado = math.prod(args)  # Multiplica todos os argumentos
    else:
        return "Operação não reconhecida"
    
    # Exibe o resultado
    return f"O resultado da {operacao} é: {resultado}"

# Chamando a função com soma
print(calculadora(2, 3, 5, operacao='soma'))

# Chamando a função com multiplicação
print(calculadora(2, 3, 4, operacao='multiplicacao'))

# Função com quantidade de argumentos variável (usando *args)
def imprimir_argumentos(*args):
    print("Argumentos recebidos:")
    for arg in args:
        print(arg)

# Chamando a função com vários argumentos
imprimir_argumentos(1, 2, 3, 4, 5, "Texto")

# Função lambda
soma_lambda = lambda x, y: x + y  # Função lambda para somar dois números
print(f"Soma com lambda: {soma_lambda(10, 5)}")

