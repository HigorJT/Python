def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31musuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31musuário preferiu não digitar esse número. \033[m')
        else:
            return n

n1 = leiaInt('Digite um número: ')
n2 = leiafloat('Digite um real: ')
print(f'O inteiro digitado foi {n1} e o real foi {n2} ')








