import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de é {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')






