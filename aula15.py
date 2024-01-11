"""
if , elif , else

If / else sao executados quando há duas possibilidades no seu codigo, onde um é exibido se a primeira 
condiçao for cumprida, porem se esta nao for concluida a segunda condiçao entrara em vigor.

elif é usado quando é necessario colocar uma alternativa a mais entre if e else.


"""

entrada = input('voce quer entrar ou sair?')

if entrada == 'entrar':
    print('voce entrou no sistema')

elif entrada == 'espere':
    print('o sistema esta em espera')

else:
    print('voce saiu do sistema')