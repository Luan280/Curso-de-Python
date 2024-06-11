def metade(preco):
    total = preco / 2
    return total


def dobro(preco):
    total = preco * 2
    return total


def aumentando(preco, taxa):
    total = preco + (preco * taxa / 100)
    return total


def diminuindo(preco, taxa):
    total = preco - (preco * taxa / 100)
    return total


def moedas(valor, parametro=True):
    if parametro:
        return F"R${valor:.2f}"

