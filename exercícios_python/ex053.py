frase = input("Digite uma  frase: ").upper()
frase2 = frase.replace(" ", "")

for c in range(2):
    if frase2 == frase2[::-1]:
        print('Essa frase é um POLINDROMA')
    else:
        print("Essa frase NÃO é um POLINDROMA")
