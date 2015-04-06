#Distancia puntos 3D

# calculoDstancia: Punto3D Punto3D -> Float
# Calcula la distancia entre 2 puntos 3D 
# Ejemplo: calculaDistancia(Punto3D(0,0,0), Punto3D(1,1,1))
# Devuelve: 1.73205080757


import estructura
from modulos import *
from cerca import *

estructura.crear("punto3D","coordenadaX coordenadaY coordenadaZ")

coordenadaXpuntoA = input("Punto A, coordenada x?: ")
coordenadaYpuntoA = input("Punto A, coordenada y?: ") 
coordenadaZpuntoA = input("Punto A, coordenada z?: ")

coordenadaXpuntoB = input("Punto B, coordenada x?: ")
coordenadaYpuntoB = input("Punto B, coordenada y?: ")
coordenadaZpuntoB = input("Punto B, coordenada z?: ")

puntoA = punto3D(coordenadaXpuntoA, coordenadaYpuntoA, coordenadaZpuntoA)
puntoB = punto3D(coordenadaXpuntoB, coordenadaYpuntoB, coordenadaZpuntoB)


print "La distancia entre A y B es: "+str(calculoDistancia(puntoA, puntoB))



 
# Test 1 usando la funcion cerca
epsilon = 0.0001
puntoA = punto3D(0,0,0)
puntoB = punto3D(1,1,1)
assert cerca(calculoDistancia(puntoA, puntoB),1.73205080757,epsilon)

# Test 2 usando la funcion cerca
epsilon = 0.0001
puntoA = punto3D(1,2,3)
puntoB = punto3D(4,4,4)
assert cerca(calculoDistancia(puntoA, puntoB),3.7416573867739413,epsilon)

# Test 3 usando la funcion cerca
epsilon = 0.0001
puntoA = punto3D(3,2,1)
puntoB = punto3D(6,6,6)
assert cerca(calculoDistancia(puntoA, puntoB),7.0710678118654755,epsilon)

