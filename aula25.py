"""
formataçao de f-strings

é uma formataçao de strings um pouco mais simples e moderna do que a interpolaçao, geralmente a mais usada
nos dias atuais.

os simbolos são:
%s - string
%f - float
%i ou %d - int
%x ou %X - Hexadecimal(ABCDEF123456789) - combinaçao para mostrar um numero ou letra do teclado.

sinas para preencher quantidade da caracteres restantes

> - preenche a quantidade de caracteres predefinidos do lado esquerdo da string
< - preenche a quantidade de caracteres predefinidos do lado direito da string
^ - preenche a quantidade de caracteres predefinidos em ambos lados da string igualmente.

a formataçao de f-strings pode ser definida de outra forma quando a numero decimais (float), atraves dos
sinais '-' ou '+', alem de destas poderem ser formatads para conter apenas 1 casa ou mais depois da virgula
atraves do ',.1f' onde este 1 pode ser substituido por qualquer outro numero.


"""


a = 'abc'

print(f'{a:0>10}') #lado esquerdo da string preenchido por caracteres pre definidos
print(f'{a:0<10}') #lado direito da string preenchido por caracteres pre definidos
print(f'{a:0^10}') #ambos lados da string preenchidos por caracteres pre definidos

numeral = 13.233456

print(f'{numeral:,.2f}') #exemplo de formatacao de numero decimal em f-strings
print(f'{numeral:,.1f}') #exemplo de formatacao de numero decimal antes da virgula 
print(f'{numeral:-,.2f}') #este exemplo ira evidenciar no resultado um numero negativo se houver na variavel.
print(f'{numeral:10,.1f}') #exemplo de formatacao que preenche com caracteres numeros decimais antes da virgula

print(f'o valor hexadecimal de 17 é {17:04x}') #exemplo que mostra formataçao de numero hexadecimal em f-string


