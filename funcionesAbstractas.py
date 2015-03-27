from lista import *

# filtro: (... -> bool) lista(...) ... -> lista(...)
# devuelve una lista con todos los valores donde la funcion operador es True
# para el valor n dado
# ejemplo: ...
def filtro(operador, unaLista):
    if vacia(unaLista):
        return listaVacia
    else:
        if operador(cabeza(unaLista)):
            return lista(cabeza(unaLista), filtro(operador, cola(unaLista)))
        else:
            return filtro(operador, cola(unaLista))

# mapa: (... -> ...) lista(...) -> lista(...)
# devuelve lista con funcion aplicada a todos sus elementos
# ejemplo: ...

def mapa(f, unaLista):
    if vacia(unaLista):
        return listaVacia
    else:
        return lista(f(cabeza(unaLista)), mapa(f, cola(unaLista)))

# fold: (... ... -> ...) ... lista(...) -> ...
# procesa la lista con la funcion f y devuelve un unico valor
# el valor init se usa como valor inicial para procesar el primer valor de la lista
# y como acumulador para los resultados parciales
# pre-condicion: la lista debe tener al menos un valor
# ejemplo: ...

def fold(f, init, unaLista):
    if cola(unaLista) == listaVacia: # un solo valor
        return f(init, cabeza(unaLista))
    else:
        return fold(f, f(init, cabeza(unaLista)), cola(unaLista))
