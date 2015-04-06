#Clase 4-5

#campos:
#numerador: int
#denominador: int
Class Fraccion:

# Constructor
def __init_(self, numerador = 0, denominador = 1):
	# inicializacion de campos
	self.numerador   = numerador
	self.denominador = denominador
	
# suma : Fraccion -> Fraccion
# devuelve la suma de la fraccion con otra fraccion
def suma(self, fraccion):
	num = self.numerador * fraccion.denominador + fraccion.numerador * self.denominador
	den = self.denominador + fraccion.denominador
	return Fraccion(num, den)
	
# getNumerador: None -> int
# devuelve el valor del campo numerador
def getNumerador(self):
	return self.numerador
	
# getDenominador: None -> int
# devuelve el valor del campo denominador
def getDenominador(self):
	return self.denominador
	
#setNumerador: int -> None
# afecto: modifica el valor del campo numerador
def setNumerador(self, numerador):
	self.numerador = numerador
	
#setDenominador: int -> None
# afecto: modifica el valor del campo denominador
def setDenominador(self, denominador):
	self.denominador = denominador
	
# mcd: int int -> int
# devuelve el maximo comun divisor entre dos numeros x e y
# ejemplo: mcd(12, 8) devuelve 4
global mcd
def mcd(x, y):
	if x == y: return x
	elif x > y: return mcd(x-y, y)
	else: return mcd(x, y-x)
	
#Test
assert mcd(12, 8) == 4

# simplificar: None -> Nome
# efecto: simplificar la fraccion, puede modificar numerador y denominador
def simplificar(self):
	valor = mcd(self.numerador, self.denominador)
	if valor > 1:
		self.numerador = self.numerador /valor
		self.denominador = self.denominador /valor
		
#toString : None -> str
#devuelve un string con la fraccion
def toString(self):
	return str(self.numerador) + "/" + str(self.denominador)
	
# mayorQue: Fraccion -> bool
# devuelve True si self es mayor que fraccion
def matorQue(self):
	return self.numerador * fraccion.denominador >  fraccion.numerador * self.denominador
	

Estructuras de Datos
--------------------
import estructura

#lista: valor(..... = cualquier tipo) siguiente (lista)
estructura.crea("lista", "valor siguiente")


Documento Clase 5