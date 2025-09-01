
class ContaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return self._saldo
        else:
            return 'Não é posivel depositar valor negativo'
    
    def sacar(self, valor):

        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                return self._saldo
            else:
                return 'Saldo insuficiente'
        else:
            return 'Valor inválido para saque'
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self._saldo = valor
            print(f'SALDO R$:{self._saldo}')
        else:
            print('Valor inválido')

conta = ContaBancaria('Efraim')

# conta.saldo = - 100
