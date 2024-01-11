"""

Interpolaçao de Strings
Nada mais é do que outra forma de formatar strings usando simbolos para cada variavel ao inves do nome.
os simbolos são:
%s - string
%f - float
%i ou %d - int
%x ou %X - Hexadecimal(ABCDEF123456789) - combinaçao para mostrar um numero ou letra do teclado.


"""

nome = 'lucas'
idade = 28
profissao = 'engenheiro de software'

print('%s tem %d anos e trabalha como %s'%(nome,idade,profissao))

print('o numero equivalente a %d é %04x' %(28,28))
