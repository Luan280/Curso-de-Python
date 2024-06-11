from datetime import date

sexo = str(input('Qual o seu sexo?: ')).upper()

if sexo == "FEMININO":
    print('Você não precisa do ALISTAMENTO MILITAR')

elif sexo == 'MASCULINO':
    nascimento = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))

    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")

    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        print('Seu alistamento será em {}.'.format(ano))

    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(ano))
