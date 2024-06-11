def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print("\n\033[0;31mERRO: O usuário preferiu não digitar esse número.\033[m")
            return 0
        except (ValueError, TypeError):
            print(f"\033[0;31mERRO: por favor,  digite um número inteiro válido.\033[m")
        else:
            return n


def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 0
    for item in lista:
        c += 1
        print(F"\033[33m{c}\033[m - \033[34m{item}\033[m")
    print(linha())
    opcao = leiaInt("\033[32mSua opção: \033[m")
    return opcao


def ver_pessoas():
    arquivo = open("pessoas_cadastradas.txt", "r")
    for linha in arquivo:
        dado = linha.split(";")
        dado[1] = dado[1].replace('\n', "")
        print(f"{dado[0]:<30} {dado[1]:>3} anos")


def adicionar_pessoas():
    pessoas = list()
    nome = str(input("Nome: "))
    idade = input("Idade:")
    print(f"Novo registro de {nome} realizado com sucesso!")
    pessoas.append(nome)
    pessoas.append(idade)
    add_pessoas(pessoas)


def add_pessoas(lista):
    arquivo = open('pessoas_cadastradas.txt', 'a')
    arquivo.writelines(f"{lista[0]};{lista[1]} \n")
