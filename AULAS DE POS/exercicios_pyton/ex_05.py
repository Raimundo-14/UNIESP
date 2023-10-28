# Solicitar ao usuário um número
numero = float(input("Digite um número: "))

# Realizar as operações e verificar se o resultado é 8
resultado_adicao = numero + (8 - numero)
resultado_subtracao = numero - (numero - 8)
resultado_multiplicacao = numero * (8 / numero)
resultado_divisao = numero / (numero / 8)

# Imprimir os resultados
print(f"Adição: {numero} + ({8} - {numero}) = {resultado_adicao}")
print(f"Subtração: {numero} - ({numero} - {8}) = {resultado_subtracao}")
print(
    f"Multiplicação: {numero} * ({8} / {numero}) = {resultado_multiplicacao}")
print(f"Divisão: {numero} / ({numero} / {8}) = {resultado_divisao}")
