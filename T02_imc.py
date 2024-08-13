## Escribir un programa que calcule de IMC de una persona, el programa debe solicitar el peso y la altura ( AKA datos de entrada)

peso = float(input('Cual es tu peso?\n'))
altura = float(input('Cual es tu altura?\n'))

imc = peso / altura**2 ## Calcula el indice de masa corporal 
print(f'Tu indice de masa corporal es {imc:2f}')

if imc < 18.5:
    print('Estas bajo de peso')
elif 18.5 <= imc < 24.9:
    print('Tienes un peso normal')
elif 25 <= imc < 29.9:
    print('Tienes sobrepeso')
else:
    print('Tienes obesidad')
    
    
    