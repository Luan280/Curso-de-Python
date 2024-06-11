def voto(ano):
    from datetime import date
    ano = date.today().year
    atual = ano - ano
    if atual < 16:
        return f"Com {atual} anos: Voto NEGADO!"
    elif 16 <= atual < 18 or atual > 65:
        return f"Com {atual} anos: Voto OPCIONAL."
    else:
        return f"Com {atual} anos: Voto OBRIGATÓRIO!"


# Programa princípal
nascimento = int(input("Em que ano você nasceu?: "))
voto(nascimento)
