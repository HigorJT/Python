from test import menu, cabeçalho, leiaInt, linha
from time import sleep
while True:
    resposta = menu(['ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)
