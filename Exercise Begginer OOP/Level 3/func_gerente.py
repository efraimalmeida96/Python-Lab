class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario 
    
    def exibir_dados(self):
        print(f'Nome: {self.nome} | Salario: {self.salario} | ')


class Gerente(Funcionario):
    
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        super().exibir_dados() 
        print(f'Departamento: {self.departamento}')

    
f = Funcionario('Efraim', 3500)
g = Gerente('Efraim', 3500, 'TI')

f.exibir_dados()
g.exibir_dados()