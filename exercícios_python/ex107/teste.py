from ex107 import moeda

p = float(input("Digite um valor: R$"))
print(f"A metade de {p:.2f} é R${moeda.metade(p):.2f}")
print(f"O dobro de {p:.2f} é R${moeda.dobro(p):.2f}")
print(f"Aumentando 10%, temos R${moeda.aumentando(p, 10):.2f}")
print(f"Reduzindo 13%, temos R${moeda.diminuindo(p, 13):.2f}")