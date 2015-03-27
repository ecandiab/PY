from funcionesAbstractas import * 
from estructura import *
from lista import *
from cerca import *
import math 

Ls = lista(3, lista(3, lista(4, lista(5, lista(7, listaVacia))))) 



print "La lista #1 es: "+str(Ls)




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

#Test 1 usando la funcion cerca
epsilon = 0.0001
Ls2 = lista(1, lista(1, (listaVacia))) 
assert cerca(contador(Ls2),2,epsilon)

# Test 2 usando la funcion cerca
epsilon = 0.0001
Ls3 = lista(1, lista(2, lista(3, lista(4, lista(10, listaVacia))))) 
assert cerca(contador(Ls3),5,epsilon)









# promedio: lista(...) -> float
# Devuelve el promedio de la sumatoria de elementos existentes en la lista
# Ejemplo: contador(10, lista(20, lista(30, listaVacia))) retorna 16

def promedio(listaNumeros):

	if vacia(listaNumeros):
		return 0
	else:
		return fold(lambda x,y: x+y, 0.0, listaNumeros)/contador(listaNumeros) 

print "El promedio de elementos en lista es: "+str(promedio(Ls))

# Test 1 usando la funcion cerca
epsilon = 0.0001
Ls4 = lista(0, lista(11, lista(33, lista(22, lista(5, lista(100, listaVacia))))))  
assert cerca(promedio(Ls4),28.5,epsilon)

# Test 2 usando la funcion cerca
epsilon = 0.0001
Ls5 = lista(3, (listaVacia))
assert cerca(promedio(Ls5),3,epsilon)







# desviacionEstandar: lista(...) -> float
# Devuelve la desviacion estandar de los elementos existentes en la lista
# Ejemplo: desviacionEstandar(3, lista(3, lista(4, lista(5, lista(7, listaVacia))))) retorna 1.6733200530682

def desviacionEstandar(listaNumeros):

	if vacia(listaNumeros):
		return 0
	else:
		return math.sqrt((1.0/(contador(listaNumeros)-1))*(fold(lambda x,y: x+y, 0, mapa(lambda x: (x-float(promedio(listaNumeros)))**2, listaNumeros))))

print "La desviacion estandar de la lista es: "+str(desviacionEstandar(Ls)) 

# Test 1 usando la funcion cerca
epsilon = 0.0001
assert cerca(desviacionEstandar(Ls),1.6733200530682,epsilon)

# Test 2 usando la funcion cerca
epsilon = 0.0001
Ls6 = lista(10, lista(10, lista(30, listaVacia))) 
assert cerca(desviacionEstandar(Ls6),11.5470053838,epsilon)


 