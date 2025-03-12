# - Crie uma lista
lista = range(1, 10)

# - Crie um for loop para imprimir na tela todos os elementos da lista
print("Imprimindo todos os elementos da lista:")
for i in lista:
    print(i)

# - Crie um for loop usando o recurso "continue"
print("\nFor loop com 'continue':")
for i in lista:
    if i == 5:
        continue  # Ignora o número 5 e vai para a próxima iteração
    print(i)

# - Crie um for loop usando o recurso "break"
print("\nFor loop com 'break':")
for i in lista:
    if i == 7:
        break  # Interrompe o loop quando encontrar o número 7
    print(i)

# - Crie um for loop usando o "else"
print("\nFor loop com 'else':")
for i in lista:
    print(i)
else:
    print("O loop foi concluído sem interrupções.")
