colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
print(colores)

mensaje = 'En la posicion 3 esta el amarillo' + ', el rojo "0" y el rosa "7"'
print(mensaje)

colores = ["tres", "dos", "cinco", "cuatro", "uno"]
print(colores)
#--------------------------------------------------------------------
#listas 2
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

print(colores[-1])
print(colores[-7])
print(colores[-5])
print(colores[-2])
print(colores[-10])
#--------------------------------------------------------------
#listas 3
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

del colores[1] 
del colores[3] 
del colores[4] 
del colores[-3]

print(colores)
#------------------------------------------------------------------------------
#listas 4
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.remove('amarillo')
colores.remove('rojo')
print(colores)
#---------------------------------------------------------------------------
#listas 5
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

valor1 = colores.pop(1)
valor2 = colores.pop(7)

print('Nueva lista:', valor1 , 'y', valor2 )
#-----------------------------------------------------------------
#listas 6 
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.append('fuxia')
colores.append('celeste')
print(colores)
#--------------------------------------------------------------
#listas 7
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-4,'magenta')
colores.insert(-1,'turquesa')
print(colores)

#----------------------------------------------------------
#listas 8
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón',
          'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.sort(reverse=True)
print(colores)
