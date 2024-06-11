nome = str(input("Digite o seu nome completo:")).upper().strip()
print("O primeiro nome é {}.".format((nome.split()[0])))
print("O último nome é {}.".format(nome.split()[-1]))