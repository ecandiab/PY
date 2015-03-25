# Programa

import estructura
from modulos import *
import math 

estructura.crear("Punto3D","coordenadaX coordenadaY coordenadaZ")

coordenadaXpuntoA = input("Punto A, coordenada x?: ")
coordenadaYpuntoA = input("Punto A, coordenada y?: ")
coordenadaZpuntoA = input("Punto A, coordenada z?: ")

coordenadaXpuntoB = input("Punto B, coordenada x?: ")
coordenadaYpuntoB = input("Punto B, coordenada y?: ")
coordenadaZpuntoB = input("Punto B, coordenada z?: ")

puntoA = punto3D(coordenadaXpuntoA, coordenadaYpuntoA, coordenadaZpuntoA)
puntoB = punto3D(coordenadaXpuntoB, coordenadaYpuntoB, coordenadaZpuntoB)


print "La distancia entre A y B es: " calculoDistancia(puntoA, puntoB)

#test
epsilon = 0.0001
puntoA = punto3D(0,0,0)
puntoB = punto3D(1,1,1)
assert cerca(calculoDistancia(puntoA, puntoB),1.73205080757,epsilon)
