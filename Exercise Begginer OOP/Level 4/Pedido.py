
class Carrinho:
    
    def __init__(self):
        self.pedido = []
        self.cupom_discont = 0

    def total(self):

        soma = 0
        for p in self.pedido:
            soma += (p.preco * p.quantidade)
        # return sum([p.preco for p in self.pedido])
        return soma
    
    def add_items(self, *items):

        for item in items:
            self.pedido.append(item)

    def listar_item(self):

        
        qtde_itens = 0
        print(f'{'ITEM'.ljust(10)} | {'UN'.ljust(10)} | {'VL UN'.ljust(10)} | {'VL TOTAL'}')

        for item in self.pedido:
            print(f'{item.nome.ljust(10)} | {str(item.quantidade).ljust(10)} | {str(item.preco).ljust(10)} | R$:{item.quantidade * item.preco}')
            qtde_itens += item.quantidade

        print(f'{'QTDE TOTAL DE ITENS'.ljust(43)} {qtde_itens}')

        print(f'{'VALOR TOTAL':.<39}R$ {self.cupom}')

    @property
    def cupom(self):
        return self.cupom_discont
    
    @cupom.setter
    def cupom(self, valor):

        self.cupom_discont = self.total() - (self.total() * (valor / 100))
        return self.cupom_discont


class Item:

    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


item_1, item_2, item_3 = Item('Boné', 3, 50), Item('Tenis', 1, 400), Item('Meia', 2, 15)

pedido = Carrinho()

pedido.add_items(item_1, item_2, item_3)

pedido.cupom = 15

pedido.listar_item()