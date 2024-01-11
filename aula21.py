"""
operador logico or
é usado para exibir um valor quando um dos requisitos impostos em uma condiçao onde ha mais de um requisito
definido.
se nenhum requisito for preenchido ele exibira o valor correspondente ao else.

Obs: Existem duas expressoes que sao comumente usadas que se chamam Truthy e Falsy, onde Truthy é um valor
que nao é exatamente verdadeiro mas é considerado como se fosse e Falsy que é um valor que nao é exatamente
falso mas é considerado como se fosse falso.

"""

numero1 = input('digite um numero:')
numero2 = input('digite outro numero:')
numero3 = input('digite outro numero:')

if (numero1 or numero2) == numero3:
    print('esta tudo certo')

else:
    print('nao atende os requisitos')
