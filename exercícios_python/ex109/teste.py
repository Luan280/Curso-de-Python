from ex0109 import moeda

p = float(input(f"Digite o preço: R$"))
print(f"A metade de {moeda.moedas(p)} é {moeda.metade(p, False)}")
print(f"O dobro de {moeda.moedas(p)} é {moeda.dobro(p, False)}")
print(f"Aumentando 10% de {moeda.moedas(p)}, temos {moeda.aumentando(p, 10, False)}")
print(f"Diminuindo 13% de {moeda.moedas(p)}. temos {moeda.diminuindo(p, 13, False)}")
