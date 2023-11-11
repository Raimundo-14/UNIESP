saldo = float(input('Informe seu saldo: '))
debito = float(input('Informe seu débito: '))
credito = float(input('Informe seu crédito: '))
saldo_atual = (saldo - debito) + credito
print(f'Sua saldo hoje é de: {saldo:.2f}')
print(f'Seu débito hoje: {debito:.2f}')
print(f'Seu crédito: {credito:.2f}')
print(f'Seu saldo hoje é de {saldo_atual:.2f}')
if saldo_atual >= 0:
    print('Seu saldo e positivo')
else:
    print('Seu saldo é negativo')
