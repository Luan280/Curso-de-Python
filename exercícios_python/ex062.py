num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
décimo = num + (10 - 1) * razao
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print("{} -".format(num), end=" ")
        num += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos vocÊ quer mostrar a mais? "))
print("Progressão finalizada {} termos mostrados".format(total))

