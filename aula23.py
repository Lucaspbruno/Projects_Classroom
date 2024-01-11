"""

Operador in e not in
O operador in é usado para indicar se o conteudo de uma variavel ou funçao esta contido em outra.
Exemplo: a = {1}  b = {1,2,3}, neste caso 'a' esta contido em 'b'.
O operador not in é o inverso onde este pode indicar que o conteudo de uma variavel ou funçao nao esta 
contido em outra mesmo estando

"""

a = input('Digite um numero:')
numero_a = int(a)
b = 1,2,3

if numero_a in b:
    print('o valor da espressao a esta contido na expressao b.')
    

else:
    print('o valor de a nao esta contido em b')