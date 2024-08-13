##Escribe un programa que imprima la tabla de multiplicar de un usuario ingrese como dato de entrada

numero = int(input(f'ingresa un numero\n')) #Solicita al usuario para generar una tabla de multiplicar 

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} * {i} = {resultado}') 
