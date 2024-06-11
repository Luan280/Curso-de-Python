valor = 10

while valor >= -0:
    print("-" * 40)
    valor = int(input("Quer ver a tabuada de qual valor?: "))
    print("-" * 40)

    if valor <= -0:
        print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
        break
    print(f'''{valor} x 1 = {valor * 1}
{valor} x 2 = {valor * 2}
{valor} x 3 = {valor * 3}
{valor} x 4 = {valor * 4}
{valor} x 5 = {valor * 5}
{valor} x 6 = {valor * 6}
{valor} x 7 = {valor * 7}
{valor} x 8 = {valor * 8}
{valor} x 9 = {valor * 9}
{valor} x 10 = {valor * 10}''')
