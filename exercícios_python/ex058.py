from random import randint


print("\033[1;32m -=-=-=-=-= O COMPUTADOR PENSOU EM UM NÚMERO DE\033[m \033[1;34m0\033[m \033[1;32mA\033[m \033[1;34m10\033[m \033[1;32m-=-=-=-=-=\033[m")
cont = 0
computador = randint(0, 10)
jogador = int(input("Tente ADIVINHAR: "))

while jogador != computador:
    jogador = int(input("Você \033[1;31mERROU!\033[m Tente novamente: "))
    cont += 1
print("Você \033[1;33mACERTOU!!\033[m")

if cont == 0:
    print("O computador Pensou em \033[1;34m{}\033[m e você acertou de PRIMEIRA!!.".format(computador, cont))
else:
    print("O computador Pensou em \033[1;34m{}\033[m e você Tentou adivinhar {} Vezes.".format(computador, cont))
