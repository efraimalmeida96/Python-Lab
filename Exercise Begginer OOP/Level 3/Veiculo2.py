
class Veiculo:

    def __init__(self):
        print('VROOM')
    
    def mover(self):
        pass

class Carro(Veiculo):

    def __init__(self):
        super().__init__()
        print('Carro')

    def mover(self):
        print('Carro moveu')

    def __str__(self):
        return "Objeto do tipo Carro"


class Moto(Veiculo):

    def __init__(self):
        super().__init__()
        print('Moto')

    def mover(self):
        print('Moto moveu')
    
    def __str__(self):
        return "Objeto do tipo Carro"

carro = Carro()
print()
moto = Moto()
print()
carro.mover()
moto.mover()
print()


'''
class Veiculo:
    
    def mover(self):
        pass

class Carro(Veiculo):

    def mover(self):
        print('Carro moveu')

    def __str__(self):
        return "Objeto do tipo Carro"


class Moto(Veiculo):

    def mover(self):
        print('Moto moveu')
    
    def __str__(self):
        return "Objeto do tipo Carro"

c = Carro()
m = Moto()

lista_auto = [c, m]

for i in lista_auto:
    print(i)   # Usa a representação personalizada (__str__)
    i.mover()  # Executa o método sobrescrito mover()
'''