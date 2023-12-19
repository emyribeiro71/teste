# teste

import random
 
# gerar o numero aleatorio para o jogo
numero_secreto = random.randint (1,10)  

#Iniciar a varialvel que guarda o n escolhido pelo utilizador
numero_escolhido=0

#iniciar o nº de tentativas
nTentativas=5

#definir o nivel do jogo

print('Qual nivel que quer jogar?\n 1-Iniciante\n2 - Experiente\n3 - Pro player')
Nivel=int(input('Opção:'))
if(Nivel==1): 
    n_tentivas=15
elif(Nivel==2):
    n_tentivas=10
elif(Nivel==2):
     n_tentivas=5
else:
    print('Opção incorreta')

#Ciclo de repetição que acabe quando o utilizador adivinhar o nº secreto

while (numero_secreto != numero_escolhido):
    numero_escolhido=int(input('Qual é o seu palpite para o numero secreto? '))
    nTentativas-=1
    if(numero_escolhido==numero_secreto):
        print('Parabens! Acertaste o numero.')
        break
    else:
        if (numero_escolhido>numero_secreto):
            print(f'O numero secreto é menor.\n Faltam {nTentativas} tentativas')
        else:
            print(f'o numero secreto é maior.\n Faltam {nTentativas} tentativas')
if (nTentativas==0):
    print(f'o numero de secreto era {numero_secreto}')
