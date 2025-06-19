
class Empresa:

    def __init__(self):
        self.funcionarios = [f1, f2, f3]

    def add_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def pagamento_total(self):
        
        total = 0
        for funcionario in self.funcionarios:
            total += funcionario.salario
        return total

    def demitir(self, nome):

        for funcionario in self.funcionarios:

            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                return self.funcionarios
            
    def __str__(self):

        str_vazia = ''
        for i in self.funcionarios:
            str_vazia += f'{i}\n'
        
        return str_vazia

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def __str__(self):
        return f'{self.nome}, {self.salario}'

f1 = Funcionario('Zé', 3000)
f2 = Funcionario('Jão', 2750)
f3 = Funcionario('Maria', 2500)

f4 = Funcionario('Ludi', 3500)

empresa = Empresa()

empresa.add_funcionario(f4)

empresa.demitir('Jão')

print(empresa)

print(empresa.pagamento_total())