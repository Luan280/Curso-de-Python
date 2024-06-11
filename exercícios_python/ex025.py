nome = str(input("Digite o seu nome completo e vamos ver se tem (SILVA): ")).strip().upper()
no = "SILVA" in nome
print("O nome {} é: {}".format(nome, no))
