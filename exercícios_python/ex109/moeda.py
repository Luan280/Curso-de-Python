def metade(preco, parametro=0):
    total = preco / 2
    if parametro:
        return f"R${total:.2f}"
    else:
        return f"{total}"


def dobro(preco, parametro=0):
    total = preco * 2
    if parametro:
        return f"R${total:.2f}"
    else:
        return f"{total}"


def aumentando(preco, taxa, parametro=0):
    total = preco + (preco * taxa / 100)
    if parametro:
        return f"R${total:.2f}"
    else:
        return f"{total}"


def diminuindo(preco, taxa, parametro=0):
    total = preco - (preco * taxa / 100)
    if parametro:
        return f"R${total:.2f}"
    else:
        return f"{total}"


def moedas(valor):
    return F"R${valor:.2f}"
