def metade(preco, parametro=0):
    total = preco / 2
    if parametro:
        return f"R${total:.2f}".replace(".", ",")
    else:
        return f"{total}"


def dobro(preco, parametro=0):
    total = preco * 2
    if parametro:
        return f"R${total:.2f}".replace(".", ",")
    else:
        return f"{total}"


def aumentando(preco, taxa, parametro=0):
    total = preco + (preco * taxa / 100)
    if parametro:
        return f"R${total:.2f}".replace(".", ",")
    else:
        return f"{total}"


def diminuindo(preco, taxa, parametro=0):
    total = preco - (preco * taxa / 100)
    if parametro:
        return f"R${total:.2f}".replace(".", ",")
    else:
        return f"{total}"


def moedas(valor):
    return F"R${valor:.2f}".replace(".", ",")


def resumo(valor, aumento=0, redução=0):
    print("-" * 30)
    print("       RESUMO DO VALOR")
    print("-" * 30)
    print(f"preço analisado: {moedas(valor)}")
    print(f"Dobro do preço: {dobro(valor, True):5>}")
    print(f"Metade do preço: {metade(valor, True):5>}")
    print(f"{aumento}% de aumento: {aumentando(valor, aumento, True):5>}")
    print(f"{redução}% de redução: {diminuindo(valor, redução, True):5>}")
    print("-" * 30)