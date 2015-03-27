from funcionesAbstractas import * 
from estructura import *
from lista import *
from cerca import *
import math 

Ls = lista(10, lista(10, lista(30, listaVacia))) 
Ls2 = lista(3, lista(3, lista(4, lista(5, lista(7, listaVacia))))) 

# contador: lista(...) -> int
# Devuelve la cantidad de elementos que contiene la lista
# Ejemplo: contador(10, lista(20, lista(30, listaVacia))) retorna 3


def contador(listaNumeros):

	if vacia(listaNumeros):
		return 0
	else:
		cabeza(listaNumeros)
		cont = 1
		return cont + contador(cola(listaNumeros))

print "El numero de elementos en lista es: "+str(contador(Ls)) 



# promedio: lista(...) -> float
# Devuelve el promedio de la sumatoria de elementos existentes en la lista
# ejemplo: contador(10, lista(20, lista(30, listaVacia))) retorna 16

def promedio(listaNumeros):

	if vacia(listaNumeros):
		return 0
	else:
		suma = cabeza(listaNumeros)
		prom = (suma + promedio(cola(listaNumeros))/contador(Ls))
		return prom

print "El promedio de elemtos en lista es: "+str(float(promedio(Ls)))



# desviacionEstandar: lista(...) -> float
# Devuelve la desviacion estandar a partir de elementos existentes en la lista
# ejemplo: desviacionEstandar(3, lista(3, lista(4, lista(5, lista(7, listaVacia))))) retorna 1.6733200530682

def desviacionEstandar(listaNumeros):

	if vacia(listaNumeros):
		return 0
	else:
		return fold(lambda x,y: math.sqrt((x-promedio(Ls)**2)/(float(promedio(Ls)))), 0, Ls)