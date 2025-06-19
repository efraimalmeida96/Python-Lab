class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):

        total = self.preco * self.quantidade
        return total
    
    def desconto(self):

        desconto = 0.1
        self.preco = self.preco - (self.preco * desconto)
        return self.preco
    

cafe = Produto('Café', 35, 3)

print(cafe.valor_total())