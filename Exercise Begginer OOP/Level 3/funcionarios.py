
class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_pagamento(self):
        return self.salario


class Gerente(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_pagamento(self):
        salario = (1.15 * self.salario)
        return salario
    
class Estagiario(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_pagamento(self):
        salario = (0.5 * self.salario)
        return salario
    

func = Funcionario('Zé', 3000)
geren = Gerente('Jão', 3000)
estag = Estagiario('Tio', 3000)

print(func.calcular_pagamento())
print(geren.calcular_pagamento())
print(estag.calcular_pagamento())