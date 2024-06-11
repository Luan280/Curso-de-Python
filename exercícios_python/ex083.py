lista = []
count = 0
expressao = str(input("Digite um expressão: ")).upper()
lista.append(expressao)

for i in range(0, len(lista)):
    if lista[i].count("(") == lista[i].count(")"):
        print("A expressão está válida.")
    else:
        print("A expressão está inválida.")
