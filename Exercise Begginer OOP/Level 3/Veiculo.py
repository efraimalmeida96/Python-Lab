
class Veiculo:

    def __init__(self):
        self.contador = 0

    def mover(self):
        pass

class Carro(Veiculo):

    def mover(self):
        self.contador += 1
        print('Carro moveu')


class Moto(Veiculo):

    def mover(self):
        self.contador += 1
        print('Moto moveu')


carro = Carro()
moto = Moto()
carro.mover()
moto.mover()
carro.mover()