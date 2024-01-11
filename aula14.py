"""
Input - é uma funçao usada para coletar dados do usuario como por exemplo nome.
Se apenas escrever a funçao input esta nao fara nadam porem se atrelada a uma variavel do tipo string,
ela executa o comando, guarda a informaçao e exibe quando solicitado, como no exemplo abaixo com a funçao
print(f'{nome}').



"""

nome = input('Qual o seu nome ? ')

print(f'o seu nome é {nome}') 

print(f'o seu nome e {nome=}') #o nome da variavel pode aparecer se voce colocar um sinal de '=' na frente.

"""
Se precisar adicionar numeros tambem atribua da mesma forma que foi feito anteriormente em forma de string.

para fazer a soma de dois numerais que sao strings basta fazer a conversao para uma variavel do tipo int.

Obs: nunca converta uma variavel do tipo string para int na mesma linha, crie primeiro uma varivel do tipo
string e depois crie uma variavel que converta o tipo string para esta pois fazendo isso pode-se evitar um
erro de codigo quando o usuario digitar dados futuramente.

"""

numero_1 = input('qual é o seu numero ?')

numero1 = int(numero_1)

print(f'o seu numero é {numero_1}')

