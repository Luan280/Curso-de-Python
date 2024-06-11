from random import randint
from time import sleep
from operator import itemgetter

ranking = ()
print("VALORES SORTEADOS:")
jogo = {"jogador1": randint(1, 6),
        'jogador2': randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6)}
for nome, numero in jogo.items():
    print(f"  O {nome} tirou {numero} nos dados")
    sleep(1)
print("-=" * 15)
print("==RANKING DE JOGADORES:==")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"  {i+1}º lugar {v[0]} com {v[1]}")
    sleep(1)
