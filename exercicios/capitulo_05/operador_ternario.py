# - Reescreva a estrutura condicional do exercício do arquivo \"if_elif_else.ipynb\" 
# usando operador ternário\n"
lista = range(1,30)
ate_12 = []
entre_13_e_20 = []
maior_21 = []
for i in lista:
    ate_12.append(i) if i <= 12 else entre_13_e_20.append(i) if i <= 20 else maior_21.append(i)


print('ate_12: ', ate_12)
print('entre_13_e_20: ' ,entre_13_e_20)
print('maior_21: ' ,maior_21)