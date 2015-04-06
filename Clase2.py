# Resumen Clase 2.

numero = input(" Ingrese un numero ")
doble  = numero * 2
print doble
# 20

numero = raw_input('Ingrese un numero ')
doble  = numero * 2
print doble
# '1010'

# Modulos
#----------
# triangulo.py
import math
# perimetro: num num num -> num
# calcula el perimetro de un triangulo de lados a, b y c
# ejemplo: perimetro(2, 3, 2) devuelve 7
def perimetro(a,b,c):
	return a + b + c

# Test
assert perimetro(2, 3, 2) == 7

# area: num num num -> float
# calcula el area de un triangulo de lados a, b y c
# ejemplo area(3, 4, 5) devuelve 6
def area(a, b, c):
	semi = perimetro(a,b,c) / 2.0
	area = math.sqrt(semi * (semi - a) * (semi - b) * (semi - c))
	return area
	
# Test
assert area(3,4,5) == 6

# ejemplo de uso del modulo triangulo.py
#import triangulo

print 'Calcular en area y perimetro de un triangulo'
lado1 = input('Ingrese el largo del primer lado: ')
lado2 = input('Ingrese el largo del segundo lado: ')
lado3 = input('Ingrese el largo del tercer lado: ')
print 'El perimetro del triangulo es: ', perimetro(lado1,lado2,lado3)
print 'El area del triangulo es: ', area(lado1, lado2, lado3)


if random.randinit(1,2) == 1:
	print "cara"
else
	print "sello"
	
# jaliscoCachipun: str -> str
# entrega la jugada ganadora del cachipun dad una entrada valida
# ejemplo: jaliscoCachipun('tijera') debe producir 'piedra'
def aliscoCachipun(jugada):
	if jugada == 'piedra':
		return 'papel'
	elif jugada == 'papel':
		return 'tijera'
	elif jugada == 'tijera':
		return 'piedra'
		
# test
assert aliscoCachipun('tijera') == 'piedra'

# Funciones Recursivas
#-----------------------

# potencia: num int -> num
# calcular la potencia de base elevado a exp (entero positivo)
# ejemplo potencia(2, 4) devuelve 16
def potencia(base, exp):
	if exp == 0:
		# caso base
		return 1
	else:
		# caso recursivo
		return base * potencia(base, exp - 1)
		
#Test
assert potencia(2, 4) == 16
assert potencia(-1, 5) == -1
assert potencia(3, 0) == 1

# factorial: int -> int
# calcula el factorial de n
# ejemplo: factorial(10) devuelve 3628800
def factorial(n):
	if n == 0:
		# caso base
		return 1
	else 
		# caso recursivo
		return n * factorial(n - 1)
		
#Test
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800

# sumaFracciones: int int int int -> float
# calcula la suma entre dos feacciones a/b y c/d
# ejemplo : sumaFracciones(1,2,3,4) devuelve 1.25
def sumaFracciones(a,b,c,d):
	return (a + b c + d) * 1.0 /b * d
	
# Test (usa la funcion cerca)
epsilon = 0.000001
assert cerca(sumaFracciones(1,2,3,4), 1.25, epsilon)


# Datos compuestos struct
#..........................
import estructura

# fraccion: numerador (int) denominador (int)
estructura.crear("fraccion", "numerador denominador")

# sumaFracciones: fraccion fraccion -> fraccion
# crear una nueva fraccion que corresponda a la suma de dos fracciones f1 y f2
# ejemplo: sumaFracciones(fraccion(1,2), fraccion(3,4))
# devuelve fraccion(10,8)
def sumaFracciones(f1, f2):
	num = f1.numerador * f2.denominador + f1.denominador * f2.numerador
	den = f1.denominador * f2.denominador
	return fraccion(num, den)
	
#Test
 f12 = fraccion(1,2)
 f34 = fraccion(3,4)
 assert sumaFracciones(f12, f34) == fraccion(10, 8)