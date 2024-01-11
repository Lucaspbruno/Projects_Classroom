"""

Try / except 
Try - tentar executar um codigo
except - ocorreu um erro ao executar 
Quando se usa if, elif ou else apenas se verifica se é verdadeiro ou falso porem em Try / Except isso é 
diferente pois com a funçao try se testa o codigo e a funçao except executa se o codigo apresenta algum erro


"""

numero1 = input('Digite um numero:')





#if numero_convertido == int or float:
#   numero_convertido = int(numero1)
#   print(f'o dobro de {numero1} é {numero_convertido*2}')

#else:
#   print('não é um numero')    
# este é um exemplo claro de um erro onde tudo pode quebrar se digitar algo diferente de um numero.



try:
    numero_convertido = int(numero1)
    print(f'o dobro de {numero1} é {numero_convertido*2}')

except:
    print('não é um numero')


