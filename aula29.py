"""
Regras de boas praticas

Constantes
Sao variaveis que nunca vao mudar, ou seja, é uma variavel que nao pode ser mudada.
Podem ser criadas colocando letras maiusculas no nome da variavel.

Regras sobre if / else
Muitas condiçoes no mesmo if / else sao ruins pois estas complicam o entendimento de outro desenvolvedor
sobre o programa.

Complexidade do codigo
Codigos nao podem ser muito complexos, quanto mais claros e limpos sao melhores.

Limpeza de codigo
Sempre que ver um codigo que esteja muito poluido com condiçoes muito grande transforme estas em variaveis
e substitua-as no codigo fazendo assim ficar mais limpo.

"""

velocidade = 59 #velocidade do carro.
local_carro = 100 #posicao em que o carro esta na pista.

RADAR_1 = 60 #velocidade maxima do radar.
LOCAL_1 = 100 #local em que o radar esta.
RADAR_RANGE = 1 #alcance do radar.

#Cheque se a velocidade do carro é maior do que a velocidade maxima proposta pelo radar

velocidade_acima = velocidade > RADAR_1 #variavel para checar se o carro esta acima da velocidade ou nao
range_radar_99 = LOCAL_1-RADAR_RANGE #variavel que determina o range do radar 1 metro abaixo de 100
range_radar_101 = LOCAL_1+RADAR_RANGE #variavel que determina o range do radar 1 metro acima de 100

alcance_radar = local_carro >= range_radar_99 and local_carro <= range_radar_101 # expressao que mostra o alcance do radar
carro_acima_do_radar =  local_carro >= alcance_radar and velocidade_acima #expressao que mostra se o carro passou ou nao.


if velocidade_acima:
    print('A velocidade do carro é maior do que o limite de velocidade')

#cheque se o carro esta no alcance do radar

if carro_acima_do_radar:
    print('carro foi multado pelo radar')

else:
    print('o carro nao foi multado')