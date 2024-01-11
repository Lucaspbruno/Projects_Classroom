"""
Operador logico 'and'- é usado quando é necessario que se cumpra 2 ou mais condiçoes para que uma açao
(if, elif ou else) seja executada e apresente o valor determinado.

se todos os valores forem verdadeiros ele exibira o valor correspondente porem se algum valor for falso
ele igorara o restante e exibira apenas a segunda opçao.
"""

numero1 = input('digite um numero:')
numero2 = input('digite outro numero:') 
numero3 = input('digite outro valor:')



if numero1 and numero2 <= numero3:
    print('as variaveis sao iguais')

else:
    print('as variaveis sao diferentes')
