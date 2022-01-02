#Programa para calcular el IMC

print('\nA continuacion se ejecutara el programa que le ayudara a calcular su IMC')

peso = input('Ingrese su peso en Kg por favor: ')

altura = input('Ingrese su altura en Metros por favor: ')

altura2 = float(altura) * float(altura)

IMC = int(peso) / float(altura2)

print('Su IMC es de: '), IMC

if IMC < 18.5:
    print('Su Peso es Bajo')
elif IMC >= 18.5 and IMC < 24.9:
    print('Su Peso es Normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Usted tiene sobrepeso')
else:
    print('Usted sufre de Obesidad')