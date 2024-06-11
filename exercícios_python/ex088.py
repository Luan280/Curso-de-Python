from random import sample
from time import sleep


print("-" * 40)
print("          JOGA NA MEGA SENA")
print("-" * 40)
sorteio = int(input("Quantos números você quer sortear? "))
print(f"-=-=-= SORTEANDO {sorteio} JOGOS-=-=-=")
lista = []

for n in range(0, sorteio):
    numero = sample(range(0, 60), 6)
    lista.append(numero)

for valor in range(0, sorteio):
    print(f"JOGO {valor + 1}: {lista[valor]}")
    sleep(1)
print("")