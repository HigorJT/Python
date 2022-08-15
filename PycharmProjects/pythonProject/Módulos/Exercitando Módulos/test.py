import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de é R$ {p} é R$ {moeda.dobro(p)}')
print(f'O aumentando 10%, temos R% {moeda.aumentar(p, 10)}')

