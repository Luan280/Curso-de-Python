n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    print('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa''')
    opcao = int(input(">>>>> Qual é a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma de {} + {} é {}.".format(n1, n2, soma))

    elif opcao == 2:
        mult = n1 * n2
        print("O produto de {} * {} é {}.".format(n1, n2, mult))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o Maior número é {}.".format(n1, n2, maior))

    elif opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("FINALIZANDO...")
    else:
        print("Opção inválida. Tente novamente!!")
print("Fim do programa! Volte sempre!")
