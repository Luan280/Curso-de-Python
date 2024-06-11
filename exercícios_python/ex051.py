num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = num + (10 - 1) * razao

for c in range(num, décimo + razao, razao):
    print('{}'.format(c), end="- ")
print('ACABOU!')
