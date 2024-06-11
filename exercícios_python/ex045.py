from time import sleep
from random import randint

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 20)
print('Computador escolheu: {}'.format(itens[computador]))
print('Jogador escolheu: {}'.format(itens[jogador]))
print('-=' * 20)

if computador == 0:# Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:#Computador jogou Papel
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    elif jogador == 0:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:#Computador jogou Tesoura
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
