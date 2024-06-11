from random import randint
from time import sleep

print('\033[1;33m>\033[m' * 60)
print('\033[1;31mCOMPUTADOR\033[m:Pensei em um número de \033[1;34m0 a 5\033[m. Tente adivinhar.....')
print('\033[1;33m<\033[m' * 60)

# "Pensamento" do computador
computador = randint(0, 5)

# jogador tenta adivinhar
numero = int(input('Que número você acha que é: '))

# Função que faz o computador esperar alguns segundos
print("\033[1;33mPROCESSANDO.....\033[m")
sleep(2)

if numero == computador:
    print('\033[1;35mPARABÉNS!, Você conseguiu me vencer!.\033[m')
else:
    print('O \033[1;31mCOMPUTADOR VENCEU!\033[m, Eu pensei no número \033[1;34m{}\033[m e não no número \033[1;34m{}\033[1;34m.'.format(computador, numero))
