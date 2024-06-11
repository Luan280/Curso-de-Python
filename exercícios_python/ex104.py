def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um valor inteiro.")
        if ok:
            return valor


# Programa princípal
n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o valor {n}")
