# tabuada

tabuada = int(input('Digite a tabuada desejada:'))


for count in range(10):
    # print(f'{nun1} x {nun2} = {num1 * num2}')
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
