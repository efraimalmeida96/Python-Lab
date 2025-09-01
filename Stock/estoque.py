from pathlib import Path
import csv

class Estoque:

    lista_de_estoque = []

    def adicionar(self, nome, preco, qtde):

        self.lista_de_estoque.append({
            'nome': nome,
            'preco': preco,
            'qtde': qtde
        })

        CAMINHO_ARQUIVO = Path(__file__).parent / 'estoque.csv'

        with open(CAMINHO_ARQUIVO, 'a', newline='', encoding="utf-8") as file:
            nome_cols = self.lista_de_estoque[0].keys()

            escritor = csv.DictWriter(file, fieldnames=nome_cols)

            if file.tell() ==0:
                escritor.writeheader()

            escritor.writerow(self.lista_de_estoque[-1])


    def remover(self, nome):
        
        for _ in self.lista_de_estoque:

            if nome == _['nome']:
                self.lista_de_estoque.remove(_)

    def atualizar_qtde(self, nome, nova_qtde):
        
        if nova_qtde > 0:
            for _ in self.lista_de_estoque:
                if nome == _['nome']:
                    _['qtde'] = nova_qtde
        

# e = Estoque()
# e.adicionar('TV', 1500, 8)
# e.remover('TV')