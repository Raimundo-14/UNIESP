cadastrar = input('Deseja cadastrar (s/n): ').upper()


while cadastrar == 'S':
    peso = float(input('Digite o eso da pessoa em Kg: kg'))
    altura = float(input('Digite a altura da pessoa em metros: metros: '))

    imc = peso/(altura*altura)
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        print('Peso normal')
    else:
        print('Acima do peso')

    cadastrar = input('Deseja cadastrar (s/n): ').upper()
