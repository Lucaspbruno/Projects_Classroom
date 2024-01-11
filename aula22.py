"""
Operador Logico not

é um operador que nega uma afirmaçao verdadeira ou falsa, transformando ela no inverso.
pode ser usado em conjunto com if e elif, exceto else pois esta é a funçao que apresenta o que foi definido
caso os outros nao cumpram os requisitos.

"""
senha = input('Digite uma senha:')

if senha == 1234:
    print('a senha esta certa')

elif not senha:
    print('voce nao digitou nada')    

else:
    print('a senha esta incorreta')

