dados = dict()
lista = list()
total = 0
while True:
    dados["nome"] = str(input('Nome: '))
    while True:
        dados["sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if dados["sexo"] in "MF":
            break
        print("ERROU!, Digite apenas M ou F.")
    dados["idade"] = int(input("Idade: "))
    total += dados["idade"]
    lista.append(dados.copy())
    while True:
        continuar = str(input("Quer continuar [S/N]")).upper()[0]
        if continuar in "SN":
            break
        print("ERROU!, Digite apenas S ou N.")
    print("-=" * 10)
    if continuar == "N":
        break
media = total // len(lista)
print(lista)
print(f"O grupo tem {len(lista)} pessoas")
print(f"A média de idade é de {media} anos.")
print(f"As mulheres cadastradas foram:", end=" ")
for p in lista:
    if p["sexo"] == "F":
        print(f'{p["nome"]}', end=" ")
print()
print(f'lista das pessoasa que estão acima da média:')
for p in lista:
    if p["idade"] > media:
        print(F"{p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}")
        print()
print("ENCERRADO!!!")
