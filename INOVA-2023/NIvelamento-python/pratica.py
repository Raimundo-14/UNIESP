produto = input('Deseja comprar algum produto?(s/n): ').upper()


while produto == 'S':
    nome = input('Digite o nome no produto: ')
    preco = float(input('Digite o valor do produto: R$'))
    quantidade = float(input('Digite o quantidade: '))
    valor = float(input('Digite o valor pago no caixa: R$'))

    total = preco * quantidade
    troco = valor - total

    if preco < valor:
        print('O total da sua compra é de:R$, {} reais!'.format(
            total), 'Seu troco é de: R$ {} reais!'.format(troco))
    elif preco > valor:
        print('Valor insuficiente para compra!')
    else:
        print('Você nao possui troco!')

    produto = input('Deseja comprar mais algum produto?(s/n): ').upper()
