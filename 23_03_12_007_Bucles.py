x = 0

while x <= 15:
	print(x)
	x += 5

x = 0

while x >= -100:
	print(x)
	x -= 20

x = 10

while x >= 0:
	print('El valor del bucle es de: ', x)
	x -= 1
#-------------------------------------------------
#bucle 2
x = 0

while x <= 30:
	x += 1
	if x == 4 or x == 6 or x ==10: 
		print('Se salto el valor', x , 'de x')
		continue
		

	if x == 15: 
		print('se rompio la ejecucion')
		break
		x += 1
	print(x)
#----------------------------------------------------
#bucle 3
colores = ('rojo','azul','verde','amarillo')
for x in colores:
	print('El color es: ' + x + '.')
#------------------------------------------------------------
#bucle 4
for x in range(7, 800, 100):
	print(x)