def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    return imc


peso = float(input('Digite o peso da pessoa em Kg: '))
altura = float(input('Digite a altura em metros: '))

imc = calcular_imc(peso, altura)
imc2 = calcular_imc(peso, altura)
if imc < 18.5:
    print('Abaixo do peso', imc)
elif 18.5 <= imc < 24.9:
    print('Peso normal', imc)
else:
    print('Acima do peso', imc)
