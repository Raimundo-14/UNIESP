nota1 = int(input('Informe sua 1° nota:'))
nota2 = int(input('Informe sua 2° nota: '))
soma = nota1 + nota2
media = soma/2
if media >= 6:
    print(f'Sua média foi, {media}')
    print('Parabéns, você foi aprovado')
else:
    print(f'Sua média foi, {media}')
    print('Infelizmente você não foi reprovado')
