
class Pessoa:

    def __init__(self, nome, idade, profissao):
        
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def apressentar(self):

        print(f'Óla, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.')

p = Pessoa("Efraim", 29, "Engenheiro Mecânico")

p.apressentar()