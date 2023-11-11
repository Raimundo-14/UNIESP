# ESTOQUE MILHO EM TONELADA

estoque = 20
estoque_max = 50
estoque_min = 10
produto = int(input('Informe a quantidade do produto: '))

adi_produto = estoque + produto

media_estoque = (estoque_max + estoque_min)/2
print(f'{estoque} ton. do produto em estoque')
print(
    f'Está será a nova quantidade do produto em estoque, {adi_produto} ton.')
if adi_produto >= media_estoque:
    print(
        f'Não será necessário adquirir o produto, média do estoque {media_estoque} já é suficiente')
    print(
        f'A quantidade {adi_produto} ton ultrapassa a capacidade máaxima de {estoque_max} ton e não pode ser adcionada pois ultrapassa a quantidade máxima de estoque.')

else:
    print(f'A quantidade adciona é {produto} poderá ser comprada!!')
