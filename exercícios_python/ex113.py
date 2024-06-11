def leiaInt():
    while True:
        try:
            n1 = int(input("Digite um número Inteiro: "))
        except KeyboardInterrupt:
            n1 = 0
            print("\n\033[0;31mERRO: O usuário preferiu não digitar esse número.\033[m")
            break
        except ValueError:
            print(f"\033[0;31mERRO: por favor,  digite um número inteiro válido.\033[m")
        else:
            break

    while True:
        try:
            n2 = float(input("Digite um número Real: "))
        except KeyboardInterrupt:
            n2 = 0
            print("\n\033[0;31mERRO: O usuário preferiu não digitar esse número.\033[m")
            break
        except ValueError:
            print(f"\033[0;31mERRO: por favor, digite número Real válido.\033[m")
        else:
            break

    print(f"O VALOR INTEIRO DIGITADO É {n1} E O REAL FOI {n2} ")


leiaInt()
