#Exercicios aula 31

#Exercicio 1

numero = input('Digite um numero inteiro:')


if numero.isdigit():
    numero_inteiro = int(numero) 
    if ((numero_inteiro % 2) == 0):
        print('o numero é par')
    else:
        print('o numero é impar')    

else:
    print('este numero nao é um numero inteiro')

"""Para resolver uma funçao que pede um numero ao usuario e depois verifica se é um numero ou nao sempre 
use a funçao isdigit junto da variavel."""


  