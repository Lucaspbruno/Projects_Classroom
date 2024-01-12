#Exercicio 3


nome = input('Diga um nome:')

char_nome = len(nome)

if char_nome <= 4:
    print('o nome é curto')

elif char_nome >= 5 and char_nome <= 6:
    print('O nome tem tamanho normal')

elif char_nome > 6:
    print('O nome é muito grande')        