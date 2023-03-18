num1 = 15
num2 = 20

if num1 < num2:
	print('Se ejecuta el if.')


num1 = 1450
num2 = 60

if num1 > num2:
	print('Se ejecuta el if.')


num1 = 1450
num2 = 1450

if num1 != num2:
	print('Se ejecuta el if.')
	
#-----------------------------------------------------
#condicionales 2
color = 'rojo'

if color == 'rojo':
	print('El color es rojo.')
else: 
	print('El color no es rojo.')
#--------------------------------------------------------
#condicionales 3

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres señor.')
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
elif edad > 100 and edad <= 120:
	print('Tas muerto')
else:
	print('Edad no válida.')
#--------------------------------------------------------------------
#condicionales 4
entrada = input('Introduce cualquier color:\n')
colores = ['verde', 'rojo', 'azul', 'amarillo']
if entrada in colores[0]:
    print('El color verde esta admitido.')
elif entrada in colores[1]:
    print('El color rojo esta admitido.')
elif entrada in colores[2]:
    print('El color azul esta admitido.')
elif entrada in colores[3]:
    print('El color amarillo esta admitido.')
else:
    print('El color no esta admitido.')
