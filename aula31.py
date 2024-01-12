"""

Flag(bandeira) - basicamente é um marcador que serve para sinalizar algum ponto no programa,
é usado principalmente para mostrar se o compilador passou por aquele caminho ou nao.

Em algumas variaveis que nao pode ser definido o valor delas, é colocado o valor None (vazio),
onde este é mudado depois de certas condiçoes no codigo serem cumpridas.
Quando se utiliza o None, sempre usa-se 'is' ou 'is not' em conjunto para definir condiçoes de mudança.

is - é o que determina se o valor de none é o mesmo.
is not - é a inversao deste valor.

"""

condicao = True

passou_dentro_do_if = None

if condicao:
    passou_dentro_do_if = True
    print('A condiçao e verdadeira')

else:
    print('A condiçao e falsa')

if passou_dentro_do_if is None:
    print('Nao passou no if')

if passou_dentro_do_if is not None:
    print('passou no if')            