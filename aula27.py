#exercicios aula 26
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')



if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[-1:-6:-1]}')
    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome contem 0 espaços')    
    
    print(f'seu nome contem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpe voce deixou campos vazios')