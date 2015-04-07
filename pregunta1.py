
# cuentaVocales: str -> int
# Lee un string y devuelve la cantidad de vocales que tiene
# Ejemplo: cuentaVocales("Hola 2015!") retorna 2


def cuentaVocales(lectura):
   
   for caracter in lectura:
		cont = lectura.count ("a") + lectura.count ("e") + lectura.count ("i") + lectura.count ("o") + lectura.count ("u") 
		contUP = lectura.count ("A") + lectura.count ("E") + lectura.count ("I") + lectura.count ("O") + lectura.count ("U") 
		return cont+contUP


#TEST

assert cuentaVocales("HOLA, como estas????") == 6
assert cuentaVocales("bien po! y tu jajaja") == 7
assert cuentaVocales("excelente, estoy al 100%") == 7
assert cuentaVocales("eso pareceeeeeeee") == 12