lista = ('Palmeiras', 'Grêmio', 'Atlêtico-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
         'Internacional','Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthias', 'Cruzeiro', 'Vasco', 'Bahia',
         'Santos', 'Goiás', 'Coritiba', 'América-MG')


print(f'Lista de times do Brasileirão: {lista}')
print(f'Os 5 primeiros são {lista[:5]}')
print(f'Os 4 últimos são {lista[-4:]}')
print(f'Times em ordem alfabética: {sorted(lista)}')
print(f'O palmeiras está na {lista.index("Palmeiras")+1}º colocação.')

