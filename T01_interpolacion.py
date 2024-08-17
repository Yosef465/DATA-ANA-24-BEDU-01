## Ecribir diferentes formas de interpolar y formatear cadenas
## Crear variables
nombre = 'Yosef'
edad = 22

# ejemplo 1 Formato literal 
print((f'Mi nombre es {nombre} y tengo {edad} años'))

#ejemplo 1 usando operador % 
print('Mi nombre es %s y tengo %d años' %(nombre,edad))

#ejemplo 2 Metdod str.format()
print('Mi nombre es {} y tengo {} años' .format(nombre,edad))

#ejemplo 3 Formato especifico 
valor = 3.14159     #variable con 5 decimales
print(f"El vlor de pi es aproximadamente {valor:.2f}")