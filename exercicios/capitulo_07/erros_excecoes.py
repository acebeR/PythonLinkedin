def dividir(a, b):
    try:
        # Tentando realizar a divisão
        resultado = a / b
    except ZeroDivisionError:
        # Captura a exceção ZeroDivisionError se tentar dividir por zero
        print("Erro: Não é possível dividir por zero.")
    except TypeError:
        # Captura a exceção TypeError se os tipos não forem compatíveis para a operação
        print("Erro: Tipo de dado inválido. Certifique-se de fornecer números.")
    else:
        # Caso a operação seja bem-sucedida
        print(f"O resultado da divisão é: {resultado}")
    finally:
        # O código dentro do finally é sempre executado, independentemente de uma exceção ocorrer ou não
        print("Operação de divisão concluída.")

# Testando com diferentes entradas
dividir(10, 2)  # Caso normal
dividir(10, 0)  # Tentando dividir por zero
dividir(10, 'a')  # Passando tipo inválido
