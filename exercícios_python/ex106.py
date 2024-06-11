def interactive():
    from time import sleep
    while True:
        sistema = "  SISTEMA DE AJUDA PyHELP  "
        print("\033[1;30;34m~" * len(sistema))
        print(sistema)
        print("~" * len(sistema))
        resposta = str(input("\033[mFunção ou bíblioteca > "))
        if resposta in "fim":
            print("\033[1;30;31m   ATÉ LOGO!\033[m")
            break
        acessando = f"  Acessando o manual do comando '{resposta}'  "
        print("\033[0;30;32m~" * len(acessando))
        print(f"{acessando}")
        print("~" * len(acessando))
        print("\033[m")
        sleep(2)
        print("\033[1;30;35m")
        print(help(resposta))
        print("\033[m")
        sleep(2)


interactive()
