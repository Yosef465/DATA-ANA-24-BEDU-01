## Ecribir diferentes formas de interpolar y formatear cadenas
# ejemplo 1 Formato literal 
nombre = 'Yosef'
edad = 24
print((f'Mi nombre es {nombre} y tengo {edad} años'))

#ejemplo 1 usando operador % 
print('Mi nombre es %s y tengo %d años' %(nombre,edad))

#ejemplo 2 Metdod str.format()
cadena3 = 'Mi nombre es {} y tengo {} años' .format(nombre,edad)
print(cadena3)

#ejemplo 3 