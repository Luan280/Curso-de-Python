def ficha(nome="<Desconhecido>", gol=0):
    if gol == "":
        gol = 0
    if nome in "":
        nome = "<DESCONHECIDO>"

    return print(f"O jogador {nome} fez {gol} gol(s) no campeonato.")


jogador = str(input("Nome do jogador: ")).capitalize()
gols = str(input("Número de gols: "))
ficha(jogador, gols)
