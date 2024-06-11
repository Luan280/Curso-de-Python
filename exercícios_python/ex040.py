nota1 = float(input('Digite a primeira nota? '))
nota2 = float(input('Digite a segunda nota? '))

#calculo da média
media = (nota1 + nota2) / 2

print("A sua média foi \033[34m{}\033[m".format(media))

if media <= 5.0:
    print('Você está \033[1;31mREPROVADO!')
    print('Estude mais...')

elif media >= 5.0 and media <= 6.9:
    print('Você está de \033[1;32mRECUPERAÇÃO!')

elif media >= 7.0:
    print('Você está \033[1;33mAPROVADO!')
