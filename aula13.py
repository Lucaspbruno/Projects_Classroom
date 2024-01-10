"""
para utilizar o comando format crie 3 variaveis e atribua cada uma delas a uma variavel diferente onde 
esta exibe o valor de cada uma delas de acordo com a ordem das variaveis.

Se inserir mais valores do que há isto causara um erro.

"""

a = 'A'
b = 'B'
c = 1.1
formato = 'a = {0} b = {1} c = {2:.2f}'.format(a,b,c) 

""" para atribuir posiçao a uma variavel basta numera-la dentro das chaves como no exemplo acima {0}.
    Isto é chamado de parametro que no caso é aquilo que indica a posiçao de algo.
    Quando se nomeia uma variavel esta passa a ser de argumento. exemplo 'nome1 = a'
"""

print(formato)

