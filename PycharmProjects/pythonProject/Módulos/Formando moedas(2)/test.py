import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, True))}')
print(f'O dobro de é {moeda.moeda(p)} é {(moeda.dobro(p, True))}')
print(f'O aumentando 10%, temos {(moeda.aumentar(p, 10, True))}')





