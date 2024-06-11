dados = dict()
lista = list()
partidas = list()
soma = 0
while True:
    partidas.clear()
    dados["nome"] = str(input("Nome do jogador: "))
    dados["partidas"] = int(input(f"Quantas partidas {dados["nome"]} jogou?:"))
    for j in range(1, dados["partidas"] + 1):
        partidas.append(int(input(f"Quantos gols na {j}º partida?: ")))
    dados['gols'] = partidas[:]
    dados["total"] = sum(partidas)
    lista.append(dados.copy())

    while True:
        continuar = str(input(f"Quer continuar [S/N]?: ")).upper()
        if continuar in "SN":
            break
        print("ERROU!! Digite apenas S ou N.")
    print("-=" * 15)
    if continuar in "N":
        break
print('-' * 40)
print(f"{'COD':<5} {'NOME':<10} {'GOLS':<15} {'TOTAL'}")
print('-' * 40)
for i, j in enumerate(lista):
    print(f"{str(i):<5} {str(j['nome']):<10} {str(j['gols']):<15} {str(j['total'])}")
while True:
    mostrar = int(input(f"Mostrar dados de qual jogador? (999 para parar): "))
    if mostrar == 999:
        break
    if mostrar >= len(lista):
        print(f"ERRO! Não existe jogador com código {mostrar}!")
    else:
        print(f"--LEVANTAMENTO DO JOGADOR {lista[mostrar]['nome']}")
        for i, g in enumerate(lista[mostrar]['gols']):
            print(f"No {i + 1}º jogo {lista[mostrar]['nome']} fez {g}")
    print('-' * 30)
print('<<VOLTE SEMPRE!! >>')
