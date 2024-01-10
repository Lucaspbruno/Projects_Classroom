"""
Formataçao de strings

Usando o character 'f' (format) no inicio de uma string no comando print() é possivel adicionar variaveis apenas
colocando-as entre colchetes.

Para exibir um numero decimal com uma casa ou mais depois da virgula basta usar o comando ':.1f' depois da
variavel, sendo que basta mudar o numero que o numero de casas depois da virgula mudara tambem.

Se for preciso contar inumeras casas decimais antes do ponto basta usar o comando ':,.1f' depois da variavel


"""

#exemplo da aula anterior para formatar uma string com o character 'f'.

nome = 'Saemi'
altura = 1.54
peso = 132
imc = peso/(altura*altura)

dinheiro = 100000.54

linha_1 = (f'{nome} tem {altura:.2f} de altura') #exemplo de contar casas decimais.
linha_2 = (f'pesa: {peso} quilos e seu IMC é:')
linha_3 = (f'{imc:.2f}')

linha_4 = (f'{nome} tem {dinheiro:,.2f} de dinheiro') #exemplo de contar casas antes da virgula.


print(linha_1)
print(linha_2)
print(linha_3)
print(linha_4)