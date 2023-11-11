# Solicite ao usuário um número inteiro ou real e verifique se ele é maior ou menor que 10

num = float(input('Digite um número: '))
if num > 10:
    print(f'O número {num}, e maior que 10!! ')
elif num == 10:
    print('O número digitado e igual a 10')
else:
    print(f'O número {num}, e menor que 10')
