# - Crie uma lista com 30 dados do tipo numérico\n"
lista = range(1,30)
# - Dentro de um for loop, crie uma estrutura condicional que imprima na tela o número, 
# caso ele seja maior do que 20. Se o número for 20, imprima 'Esse número é igual a 20.’ 
# e se for maior do que 20, imprima ‘Esse número é maior do que 20.’\n"
i = 1
for i in lista:
    if(i > 20):
        print('Esse número é maior do que 20',i)
    else:
        if(i == 20):
            print("Esse número é igual a 20", i)
        else:
            print(i)
# - Crie as seguintes variáveis contendo listas vazias: ate_12, entre_13_e_20, maior_21"
ate_12 = []
entre_13_e_20 = []
maior_21 = []
i = 0
# - Dentro de um for loop, crie uma estrutura condicional que distribua em cada lista os 
# números seguindo as condições abaixo: \n",
#     "1. se o número for menor do que 12, armazene-o na lista ate_12\n",
#     "2. se o número estiver entre 13 e 20, amazene-o na lista entre_13_e_20\n",
#     "3. se o número for maior do 21, armazene-o na lista maior_21\n",
for i in lista:
    if(i <= 12):
        ate_12.append(i)
    if(i > 12 and i <= 20):
        entre_13_e_20.append(i)
    if(i >= 21):
        maior_21.append(i)

print('ate_12: ', ate_12)
print('entre_13_e_20: ' ,entre_13_e_20)
print('maior_21: ' ,maior_21)