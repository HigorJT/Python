class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse =self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print('ESTOU CIENTE!')

class ClienteVIP(Cliente):
    def falar(self):
        super().falar()
        print('Outra coisa qualquer')  

'''Super = está se referindo ao método falar da super CLASSE CLIENTE'''                
