palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for vogais in palavras:
    print(f'\nna palavra {vogais} temos', end=' ')
    for letra in vogais:
        if letra in 'aeiou':
            print(letra, end=' ')
