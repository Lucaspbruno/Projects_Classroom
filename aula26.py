"""
fatiamento de strings

metodo que destaca caracteres das strings onde voce pode acessar qualquer destes dentro dela.
Onde os characteres podem ser selecionados atraves de sua posiçao que vai de 0 a 9, assim como -9 a -1.
Em casos que se apresenta um erro como 'out of range' isso quer dizer que voce selecionou uma posiçao que
nao existe naquela string ou indice de numeros.
Tambem pode pegar partes da string atraves do metodo [posiçao de inicio : fim : quantas casas pular].
se preencher apenas a posicao inicial e nao a posicao final ele ira seguir da posiçao determinada ate o
final da string.


"""

a = 'Saemi'
print(a[2]) #exemplo de destacar um character usando numero de posiçao 0 a 9
print(a[-5]) #exemplo de destacar um character usando numero de posiçao -9 a -1
print(a[2:5]) #exemplo de destacar um characteres atraves do fatiamento de string
print(a[0:5:2]) #exemplo onde usa-se o numero de casas para pular quantas casas forem determinadas.
print(a[0:5:-1]) #exemplo onde usa-se o numero de casas para pular quantas casas forem determinadas.

"""

Funçao len - é uma funçao que mostra quantos characteres existem na string.
exemplo print(len()).
Atraves da funçao len tambem pode definir quantos characteres existem no fatiamento da string.

"""

print(len(a))

print(len(a[2])) #este exemplo mostra quantos charaters há na fatia de string que foi destacada.






