maca = int(input('Digite o número de maças que você deseja comprar: '))
a = maca*1.0
b = maca*1.3
if maca >= 12:
    print(
        f'A quantidade de maças foi de, {maca}, o valor de cada maça é de R$ 1,00, o total da sua compra foi de {a:.2f}.')
else:
    print(
        f'A quantidade de maças foi de, {maca}, o valor de cada maça é de R$ 1,30, o total da sua compra é de {b:.2f}.')
