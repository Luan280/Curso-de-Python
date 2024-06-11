salario = float(input('Qual o seu salário?: '))

novo = salario + (salario*10/100)
novo2 = salario + (salario*15/100)
if salario >= 1250:
    print('O seu salário de \033[1;32mR${:.2f}\033[m com um aumento de \033[1;34m10%\033[m: \033[1;32mR${:.2f}\033[m'.format(salario, novo))
else:
    print('O seu salário  \033[1;32mR${:.2f}\033[m com um aumento de \033[1;34m15%\033[m: \033[1;32m{:.2f}\033[m'.format(salario, novo2))