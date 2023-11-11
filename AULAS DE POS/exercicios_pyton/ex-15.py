carros = ['ford', 'fiat', 'chevrolet']
carros[1] = 'volvo'
carros.insert(0, 'dodge')
carros.insert(2, 'ferrari')
del carros[2]
for carro in carros:
    print(carro.title())
print(carros[1])
