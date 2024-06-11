dados = dict()

dados['nome'] = str(input("Nome:"))
dados['media'] = float(input(f"Média de {dados['nome']}: "))

print(f"Nome é igual a {dados['nome']}.")
print(f"Média é igual a {dados['media']}")
if dados["media"] >= 7:
    dados['situação'] = "APROVADO!"
else:
    dados['situação'] = "REPROVADO!"
print(f"Situação é igual a {dados['situação']}")
