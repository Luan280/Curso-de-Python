lista = []

while True:
    nome = str(input("Nome: ")).upper()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input("Quer continuar? [S/N]: "))
    if continuar in "Nn":
        break
print("-=" * 15)

print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 30)
for valor in lista:
    print(f"{lista.index(valor):<4}     {valor[0]:<10}    {valor[2]}:>8.1f")
print("-" * 30)
while True:
    aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if aluno == 999:
        break
    print(f'As notas de {lista[aluno][0]} foram {lista[aluno][1]}')
    print(f"-=" * 15)
print("FINALIZANDO..........\n <<<VOLTE SEMPRE!!>>>")
