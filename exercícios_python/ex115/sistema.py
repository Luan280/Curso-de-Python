from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(["Ver pessoas cadastradas", 'Cadastrar nova pessoa', 'Encerrar o programa'])
    if resposta == 1:
        cabeçalho("PESSOAS CADASTRADAS")
        ver_pessoas()
    elif resposta == 2:
        cabeçalho("CADASTRANDO NOVA PESSOA")
        adicionar_pessoas()
    elif resposta == 3:
        cabeçalho("Saindo do sistema.... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite um opção válida!\033[m")
    sleep(2.5)
