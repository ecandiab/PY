# Ejercicio 4
# intersectaListas: lista lista -> lista
# Devuelve una lista con los elementos existentes en ambas listas ingresadas
# Ejemplo: intersectaListas([1, 2, "tres"], ["tres", 1, 5]) retorna [1, "tres"] 

from cerca import *

lista1 = ["uno", 2, "tres", 4, 4, "cinco", 6, "siete"]
lista2 = [1, "dos", "tres", 4, 4, 5, "seis", "siete"]
lista3 = [1,2,3,4, False, 2.5, 6.2, 9.9, "Filete", "Entrecot", "Hambre", 90000000.2]
lista4 = [1,2.0, 9, True, 2.5, "Hambre", 200.000000002]
lista5 = ["Azul", 123, "Rojo", True, 10.0, False, False, False, "Blanco", 123.123]
lista6 = ["Celeste", "Verde", "AMARILLO", 100000.10000, False, True, "cafe", "neGRO" ]

def intersectaListas(listaA,listaB):
 	
	listaC = []

  	for valor in listaA:
  		if listaB.count(valor) > 0:
  			if listaC.count(valor) == 0:
				listaC.append(valor) 
	return listaC


print "Lista 1: "+str(lista1)
print "Lista 2: "+str(lista2)
print "Lista 3: "+str(lista3)
print "Lista 4: "+str(lista4)
print "Lista 5: "+str(lista5)
print "Lista 6: "+str(lista6)
print "\n"



#Test 1
print "Interseccion Lista 1 con Lista 2: "+str(intersectaListas(lista1, lista2)) 
assert intersectaListas(lista1,lista2) == ['tres', 4, 'siete']

#Test 2
print "Interseccion Lista 3 con Lista 4: "+str(intersectaListas(lista3, lista4)) 
assert intersectaListas(lista3,lista4) == [1, 2, 2.5, 'Hambre']

#Test 3
print "Interseccion Lista 5 con Lista 6: "+str(intersectaListas(lista5, lista6)) 
assert intersectaListas(lista5,lista6) == [True, False]