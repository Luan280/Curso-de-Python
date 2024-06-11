def area(la, co):
    total = la*co
    print(f"A área de um terreno {la}x{co} é de {total}M²")


print("         CONTROLE DE TERRENOS")
print("-" * 40)
largura = float(input("LARGURA (M): "))
comprimento = float(input("COMPRIMENTO (M): "))
area(largura, comprimento)
