from operator import itemgetter

dados = dict()
gols = []
dados['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
for n in range(1, partidas + 1):
    gols.append(int(input(f"Quantos gols na {n}º partida? ")))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print("-=" * 15)
print(dados)
print("-=" * 15)
print(f"O campo nome tem o valor {dados['nome']}")
print(f"O campo gols tem o valor {dados['gols']}")
print(f"O campo total tem o valor {dados['total']}")
print("-=" * 15)
print(f"O jogador {dados['nome']} jogou {partidas} partidas.")
ranking = sorted(dados.items(), key=itemgetter(0), reverse=True)
for i, v in enumerate(dados['gols']):
    print(f"  => Na partida {i + 1}, fez {v}")
print(f"Foi um total de {dados['total']}")
