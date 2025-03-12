# - Crie um objeto iterável com 100 dados do tipo numérico 
# e imprima na tela a palavra 'Fizz' no lugar dos números divisíveis por 3, 
# 'Buzz' no lugar dos números divisíveis por 05 e 'FizBuzz' no lugar dos números 
# divisíveis por 3 e 5. Caso o número não atenda a nenhuma dessas condições, 
# imprima o próprio número."

lista = range(0,99)
i = 0
for i in lista:
    if(i % 3 == 0):
        print("Fizz")
    else:
        if(i % 5 == 0):
            print("Buzz")
        else:
            if(i % 3 == 0 and i % 5 == 0):
                print("FizBuzz")
            else: 
                print(i)
