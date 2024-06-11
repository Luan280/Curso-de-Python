from datetime import date

data = date.today().year

dados = dict()
dados["nome"] = str(input("Nome:"))
nasc = int(input("Ano de Nascimento:"))
dados["idade"] = data - nasc
dados["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if dados['ctps'] != 0:
    dados["contrato"] = int(input("Ano de contratação: "))
    dados["salário"] = float(input("Salário: "))
    dados['aposentadoria'] = dados['contrato'] + nasc - (dados['contrato'] + 65)
    print(f"nome tem o valor {dados['nome']}")
    print(f"idade tem o valor {dados['idade']}")
    print(f"ctps tem o valor {dados['ctps']}")
    print(f"contratação tem o valor {dados['contrato']}")
    print(f"Salário tem o valor R$ {dados['salário']:.2f}")
    print(f"aposentadoria tem o valor {dados['aposentadoria']}")
else:
    print(dados)
    print(f'nome tem o valor {dados["nome"]}')
    print(f"idade tem o valor {dados['idade']}")
    print(f"ctps tem o valor {dados['ctps']}")


