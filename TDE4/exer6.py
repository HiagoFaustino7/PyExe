# 6. Estoque de Produtos:
# Implemente um sistema simples de controle de estoque de produtos. O programa
# deve permitir ao usuário adicionar novos produtos ao estoque, atualizar a
# quantidade de produtos existentes e exibir o estoque atualizado. Use um dicionário
# onde as chaves são os nomes dos produtos e os valores são as quantidades
# disponíveis.

def add(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade


def att(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto] = quantidade
    else:
        print('Produto não encontrado no estoque.')


def exi(estoque):
    print('Estoque atual: ')
    for produto, quantidade in estoque.items():
        print(f'{produto}: {quantidade}')


def linha():
    print('-' * 30)


estoque = {}

while True:
    linha()
    opcao = int(input(
        '-Escolha a opção desejada-\n(1) Adicionar Produto\n(2) Atualizar Quantidade de Produtos\n(3) Exibir o Estoque atual\n(4) Fechar o Programa\n -'))
    linha()
    if opcao == 1:
        linha()
        produto = str(input('Digite o nome do produto: '))
        quantidade = int(input('Digite a quantidade do protudo: '))
        add(estoque, produto, quantidade)
        linha()

    elif opcao == 2:
        linha()
        produto = str(input('Atualize o nome do produto: '))
        quantidade = int(input("Atualize a quantidade do produto: "))
        att(estoque, produto, quantidade)
        linha()

    elif opcao == 3:
        linha()
        exi(estoque)
        linha()

    elif opcao == 4:
        linha()
        print('Saindo........')
        linha()
        break


