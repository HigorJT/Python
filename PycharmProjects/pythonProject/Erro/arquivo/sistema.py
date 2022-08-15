from test import menu, cabeçalho, leiaInt, linha
from arquivo import arquivoExiste, criarArquivo, lerArquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)
