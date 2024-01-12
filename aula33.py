#Exercicio 2

hora = input('Que horas sao agora ?')


bom_dia = [0,1,2,3,4,5,6,7,8,9,10,11]
boa_tarde = [12,13,14,15,16,17]
boa_noite = [18,19,20,21,22,23]

try:
    hora_1 = int(hora) #Obs: sempre converta uma varivel em um numero dentro de uma expressao com try ou if.

    if hora_1 in bom_dia:
        print('Bom dia')

    elif hora_1 in boa_tarde:
        print('Boa Tarde')

    elif hora_1 in boa_noite:
        print('Boa noite')  

except:
    print('isto nao é um numero')    


"""Obs: é importante que use try / except ao inves de if / else porque se o usuario digitar algo diferente de
o codigo pode quebrar."""