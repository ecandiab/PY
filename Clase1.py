# Resumen Clase 1.

# Funcion que calcula el area de un circulo

def	areaCirculo(radio):
	return  3.14 * radio ** 2
	
print areaCirculo(5)
# 78.5

# areaAnillo: num num -> float
# calcula el area de un anillo de radio exterior y
# cuyo agujero es de radio interior
# ejemplo areaAnillo(5,3) debe producir 50.24
def areaAnillo(exterior, interior):
	return areaCirculo(exterior) - areaCirculo(interior)
	
print areaAnillo(5,3)
# 50.24

#Tests
assert areaAnillo(5,3) == 50.24