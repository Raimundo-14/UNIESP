num1 = int(input('Informe um número:'))
num2 = int(input('Informe outro número: '))
a = num1 > num2
b = num1 < num2
c = num1 == num2
if a > b:
    print(f' O número informado {num1} é maior que {num2}.')
elif b > a:
    print(f' O número informado {num2} é maior que {num1}.')
else:
    print(f' Os números informados, {num1} é {num2}, são iguais')
