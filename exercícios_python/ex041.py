from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

print('Você tem \033[1;31m{}\033[m anos.'.format(idade))

if idade <= 9:
    print('Você é da categoria: \033[1;34mMIRIM\033[m')

elif idade <= 14:
    print('\033[mVocê é da categoria:\033[1;34mINFANTIL\033[m')

elif idade <= 19:
    print('Você é da categoria: \033[1;34mJUNIOR\033[m')

elif idade <= 25:
    print('Você é da categoria:\033[1;34mSÊNIOR\033[m')

else:
    print('Você é da categoria:\033[1;34mMASTER\033[m')


