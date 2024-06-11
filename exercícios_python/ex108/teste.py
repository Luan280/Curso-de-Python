from ex108 import moeda

p = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.moedas(p)} é {moeda.moedas(moeda.metade(p))}")
print(f"O dobro de {moeda.moedas(p)} é {moeda.moedas(moeda.dobro(p))}")
print(f"Aumentando 10%, temos {moeda.moedas(moeda.aumentando(p, 10))}")
print(f"Reduzindo 13%, temos {moeda.moedas(moeda.diminuindo(p, 13))}")
