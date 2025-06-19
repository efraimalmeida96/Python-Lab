
class Temperatura:

    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fah(self):
        fahrenheit = (self._celsius * 1.8) + 32
        return fahrenheit
    
    @property
    def kelvin(self):
        kelvin = self._celsius + 273.15
        return kelvin
    
    @property # GETTER
    def ajuste(self):
        return self._celsius

    @ajuste.setter
    def ajuste(self, valor):

        if valor  == 0:
            print('Digite um valor positivo ou negativo')
        else:
            if valor > 0:
                self._celsius += valor
            else:
                self._celsius -= valor


temp = Temperatura(25)
temp.ajuste = 10 # chamando o SETTER

print(temp.ajuste) # chamando o GETTER