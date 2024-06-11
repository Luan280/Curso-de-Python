def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("Contagem de 1 até 10 de 1 em 1.")
    for v in range(1, 10 + 1, 1):
        print(v, end=" ")
    print("FIM!\n", '-=' * 20)

    print("Contagem de 10 até 1 de 2 em 2.")
    for v in range(10, -1, -2):
        print(v, end=" ")
    print("FIM!\n", '-=' * 20)

    if i <= f:
        print(f"Contagem de {i} até {f} em {p} em {p}.")
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(F"{cont}", end=" ")
            cont -= p
        print("FIM!")


print("Sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input('Fim: '))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
