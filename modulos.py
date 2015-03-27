#jaliscoCachipun: str -> str
#entrega la jugada ganadora del cachipun dada una entrada valida
#ejemplo: jaliscoCachipun('tijera') debe producir 'piedra'
def jaliscoCachipun(jugada):
 	if jugada == 'piedra':
 		return 'papel'
 	elif jugada == 'papel':
 		return 'tijera'
 	elif jugada == 'tijera':
 		return 'piedra'
#test:
assert jaliscoCachipun('tijera') == 'piedra'




# factorial: int->int
# calcula el factorial de n
# ejemplo: factorial(10) devuelve 3628800
def factorial(n):
	if n == 0:
		#caso base
		return 1
	else:
		#caso recursivo
		return n * factorial(n-1)
# test
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800




# Functions
# cerca : num num num --> bool
# retorna True si x es igual a y con precision epsilon
def cerca(x, y, epsilon):
 diferencia = x - y
 return abs(diferencia) < epsilon

import math
def calculoDistancia(puntoA, puntoB):
	return math.sqrt(((puntoA.coordenadaX-puntoB.coordenadaX)**2)+((puntoA.coordenadaY-puntoB.coordenadaY)**2)+((puntoA.coordenadaZ-puntoB.coordenadaZ)**2))
