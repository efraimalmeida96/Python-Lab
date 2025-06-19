import datetime 

class ContaCorrente:

    def __init__(self, saldo):
        self._saldo = saldo
        self.extrato_lista = []
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.extrato_lista.append({'depositar': valor,})
            return self._saldo
        else:
            return 'Não é posivel depositar valor negativo'
        
    def sacar(self, valor):

        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                self.extrato_lista.append({'saque': valor,})
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


    def extrato(self):
        
        print("-=" * 20)
        print(f'{'EXTRATO':^40}')
        print("-=" * 20)

        for extrato in self.extrato_lista:

                for acao in extrato:

                    if 'saque' in extrato:
                        print(f'{'SAQUE':.<32}R$ {extrato[acao]}')

                    if 'depositar' in extrato:
                        print(f'{'DEPOSITO':.<32}R$ {extrato[acao]}')

                
        print(f'{'SALDO':.<32}R$ {self.saldo}')

                # print(f"{listagem[i]:.<30}R$ {listagem[i + 1]:>7.2f}")

        
cliente = ContaCorrente(3000)
cliente.depositar(250)
cliente.sacar(50)
cliente.extrato()