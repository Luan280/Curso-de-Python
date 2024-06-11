num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
décimo = num + (10 - 1) * razao

while cont <= 10:
    print("{} -".format(num), end=" ")
    num += razao
    cont += 1
print("ACABOU!!")
