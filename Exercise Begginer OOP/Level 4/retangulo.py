class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        area = self.largura * self.altura
        return area
    
    def perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return perimetro
    
r = Retangulo(5, 3)
print(r.area())
print(r.perimetro())
