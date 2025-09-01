from estoque import Estoque
import os 
import time

def main():
    display()

    e = Estoque()

    while True:
        
        try:
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            print('Por favor digite um numero do menu.')

        if opcao == 1:
            limpa_tela()

            # Tratamento de Erro caso o usuario não digite nada !!!!!!!!!!! Fazer para todas as oções
            nome_produto = input('Digite o nome do produto: ').strip()
            prec_produto = int(input('Digite o preco do produto: '))
            qtde_produto = int(input('Digite o quantidade do produto: '))

            if nome_produto not in e.lista_de_estoque:
                e.adicionar(nome_produto, prec_produto, qtde_produto)
                print(f'\nProduto *{nome_produto.upper()}* adicionado com SUCESSO!')
                print(f'Valor Unitário R$: {round(prec_produto, 2)}')
                print(f'Quantidade: {qtde_produto}')
            else:
                print('Produto já ADICIONADO')
            
            menu_principal()
            

        elif opcao == 2:
            limpa_tela()
            nome_produto = input('Digite o nome do produto: ')
            
            # VEREFICA A EXISTENCIA 
            if verificar_produto(nome_produto) == True:
                e.remover(nome_produto)

            else:
                print(f'Produto [{nome_produto}] não existe')

            menu_principal()

        elif opcao == 3:
            limpa_tela()
            nome_produto = input('Digite o nome do produto: ')
            nova_qtde_produto = int(input('Digite o quantidade do produto: '))
            
            # VEREFICA A EXISTENCIA 
            if verificar_produto(nome_produto) == True:
                e.atualizar_qtde(nome_produto, nova_qtde_produto)
            else:
                print(f'Produto [{nome_produto}] não existe')
            
            menu_principal()

        elif opcao == 4:

            print(f'{'PRODUTO'.ljust(25)} | {'PREÇO'.ljust(25)} | {'UNIDADE'}')

            for produto in e.lista_de_estoque:

                print(f'{produto['nome'].ljust(25)} | {str(produto['preco']).ljust(25)} | {str(produto['qtde']).ljust(25)}')

            menu_principal()

        elif opcao == 5:

            soma_total = 0
            soma_produto = 0
            
            for preco in e.lista_de_estoque:

                soma_produto += (preco['preco'] * preco['qtde'])

                soma_total += soma_produto

            print(f'VALOR TOTAL DO ESTOQUE: R$ {soma_total}')

            menu_principal()

        elif opcao == 6:
            print('DESLIGANDO', end='')
            for o in range(3):
                print('.', end='')
                time.sleep(0.5)
            break

        else:
            print('Opção inválida. Tente novamente')
        
        # time.sleep(5)
        limpa_tela()
        display()

        def verificar_produto(nome):

            for l in e.lista_de_estoque:

                if nome == l['nome']:
                    return True
                else:
                    return False

def display():

    display = {
        1: 'Adicionar Produto',
        2: 'Remover Produto',
        3: 'Atualizar Quantidade',
        4: 'Listar Produtos',
        5: 'Calcular Valor Total do Estoque',
        6: 'Sair'
    }

    for k, v in display.items():
        print(f'{v:.<40} [{k}]')


def limpa_tela():
    return os.system('cls')


def menu_principal():

    voltar = input('Pressione ENTER para voltar ao menu Principal. ')
    return voltar

if __name__ == '__main__':
    main()
