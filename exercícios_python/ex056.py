somaidade = 0
mediaidade = 0
cont = 0
maior = 0
nomevelho = ""

for c in range(1, 5):
    print("-" * 5,  "{}º PESSOA".format(c), "-" * 5)
    nome = str(input("NOME: "))
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: "))
    somaidade += idade

    if c == 1 and sexo in "Mm":
        maior = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome

    if idade < 19:
        if sexo in "Ff":
            cont += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O home mais velho tem {} anos e se chama {}.'.format(maior, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))
