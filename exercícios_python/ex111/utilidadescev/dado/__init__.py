def leiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"ERRO: \"{entrada}\" é um preço inválido!")
        else:
            return float(entrada)
