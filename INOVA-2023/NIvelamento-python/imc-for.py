i = 0
cadastrar = int(input('Quantas vezes você quer cadadstrar? '))


for i in range(cadastrar):
    peso = float(input('Digite o eso da pessoa em Kg: '))
    altura = float(input('Digite a altura da pessoa em metros: metros: '))

    imc = peso/(altura*altura)
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        print('Peso normal')
    else:
        print('Acima do peso')
