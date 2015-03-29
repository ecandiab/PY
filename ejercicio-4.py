#Ejercicio 4

lista1 = ["uno", 2, "tres", 4, "cinco", 6, "siete"]
lista2 = [1, "dos", "tres", 4, 5, "seis", "siete"]

def intersectaListas(listaA,listaB):
 	
	listaC = []

  	for valor in listaA:

  		if listaB.count(valor) > 0:
  			if listaC.count(valor) == 0:
				listaC.append(valor) 
	return listaC


print intersectaListas(lista1, lista2) 