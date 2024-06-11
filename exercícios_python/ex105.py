def notas(*nota, sit=False):
    dicionário = dict()
    dicionário['total'] = len(nota)
    dicionário['maior'] = max(nota)
    dicionário['menor'] = min(nota)
    dicionário['média'] = sum(nota) / len(nota)
    if sit:
        if dicionário['média'] > 7:
            dicionário["situacao"] = "BOA"
        if dicionário['média'] < 6:
            dicionário['situacao'] = "RUIM"
        if 6 < dicionário['média'] < 7:
            dicionário['situacao'] = "RAZOÁVEL"
    return dicionário


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
