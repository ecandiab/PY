
# porcentaje: int int -> float
# devuelve el porcentaje de un valor con respecto a un total
# ejemplo: porcentaje(19, 100) devuelve 19.0 (que corresponde a 19.0%)
def porcentaje(valor, total):
    return valor * 100.0 / total

# Tests
from cerca import cerca
tolerancia = 0.00001
assert cerca(porcentaje(19, 100), 19.0, tolerancia)
assert cerca(porcentaje(32, 50), 64.0, tolerancia)

# Implemente aqui su funcion

# resultadoPlebiscito: int int int -> boolean
# devuelve TRUE si gana la opcion SI o FALSE si gana la opcion NO de los votos del plebiscito
# Ejemplo: resultadoPlebiscito(90, 10, 0, 100) retorna TRUE

# total = input("Total Inscritos? : ")
# si = input("Votos SI: ")
# no = input("Votos NO: ")
# invalidos = input("Votos INVALIDOS: ")



def resultadoPlebiscito(si, no, invalidos, total):

	emitidos = si+no+invalidos


	if porcentaje(emitidos,total) < porcentaje(20,total):
		return False 
	
	elif porcentaje(emitidos,total) >= porcentaje(20,total) and porcentaje(emitidos,total) < porcentaje(20,total):
		if si >= porcentaje(20,total):
			return True
		else:
			return False

	elif porcentaje(emitidos,total) >= porcentaje(20,total):
		if si > no:
			return True
		elif no > si:
			return False 
		elif si == no:
			return False

	





# Tests

# Caso 1: votos < 20% total inscritos, gana NO
assert not resultadoPlebiscito(1, 2, 0, 100)
assert not resultadoPlebiscito(1, 2, 0, 50)
assert not resultadoPlebiscito(11, 8, 0, 100)
assert not resultadoPlebiscito(5, 4, 0, 50)
# Caso 2: 20% total inscriots <= votos < 40% total inscritos, votos SI >= 20% total inscritos, gana SI
assert resultadoPlebiscito(20, 12, 3, 100)
assert resultadoPlebiscito(10, 6, 2, 50)
assert resultadoPlebiscito(31, 2, 5, 100)
assert resultadoPlebiscito(15, 1, 3, 50)
# Caso 3: 20% total inscritos <= votos < 40% total inscritos, SI < 20% total inscritos, gana NO
assert not resultadoPlebiscito(15, 12, 3, 100)
assert not resultadoPlebiscito(7, 6, 3, 50)
assert not resultadoPlebiscito(19, 0, 3, 100)
assert not resultadoPlebiscito(9, 8, 2, 50)
# Caso 4: 40% total inscritos <= votos, gana opcion con mas votos, caso empate gana NO
assert resultadoPlebiscito(50, 25, 11, 100)
assert resultadoPlebiscito(25, 13, 6, 50)
assert not resultadoPlebiscito(25, 48, 7, 100)
assert not resultadoPlebiscito(13, 24, 4, 50)
assert resultadoPlebiscito(1, 0, 99, 100)
assert not resultadoPlebiscito(0, 1, 49, 50)
assert not resultadoPlebiscito(40, 40, 3, 100)
assert not resultadoPlebiscito(6, 6, 8, 50)





