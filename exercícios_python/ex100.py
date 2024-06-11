from random import randint
from time import sleep


def sorteia(lista):
    for valor in range(0, 5):
        lista.append(randint(0, 10))

    print(f"Sorteando 5 valores da lista :", end=" ")
    for valor in lista:
        print(f"{valor}", end=" ")
        sleep(0.5)
    print("FIM!")


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}.")


numero = list()
sorteia(numero)
somapar(numero)
