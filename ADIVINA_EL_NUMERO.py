# Programa para analizar un numero entre el 1 y el 10 
from random import*

# input 
X = int(input("ingrese un numero entre el 1 y el 10: "))

# processing and ouput 
Y = randint (1,10)

if X == Y:
    print("has adivinado el numero",Y,)

elif X>Y:
    print("El numero ingresado",X,"es mayor elnumero a adivinar",Y,)

else:
    print("El numero ingresado",X,"es menor al adivinar",Y,)