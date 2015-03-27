from lista import *
inventario = lista("soldadito", lista("pelota", lista("oso", listaVacia)))


# hayPelotas: lista(str) -> bool
# determinar si el string "pelota" esta en la lista unaLista
# ejemplo: hayPelotas(inventario) devuelve True

def hayPelotas(unaLista):
	if vacia(unaLista):
		return False
	else:
		if cabeza(unaLista) == "pelota":
			return True
		else:
			return hayPelotas(cola(unaLista))

# test
assert hayPelotas(inventario)





# registro: producto(str) precio(int)
import estructura
estructura.crear("registro", "producto precio")

from lista import *

# suma: lista(registro) -> int
# calcula la suma de todos los precios en unInventario
# suma(listaVacia) == 0
# suma(lista(registro("muñeca", 2990), listaVacia)) == 2990
# suma(lista(registro("robot", 5990), lista(registro("muñeca", 2990), listaVacia))) == 8980
def suma(unInventario):
	