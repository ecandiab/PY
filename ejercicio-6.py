 # Caja

# caja: list -> str
# Recive una lista y retorna un string con las palabras separadas por lineas y encerradas en un marco con caracter "*"
# Ejemplo: caja("esto es una prueba") retorna...
# **********
# * Esto   *
# * es     *
# * una    *
# * prueba *
# ********** 

frase = "hola como estas"
frase2 = "muy bien gracias y tu"
frase3 = "yo esto muuuuuuy bieeeen aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aa"
frase4 = "excelente estas genial"
frase5 = ""
frase6 = "hola"

def caja(lista):

	j = 0
	L = [] 

	if len(lista) > 0: # si lista es vacia... retorna mensaje
		for indice in range(len(lista)): # recorre la lista
			largoPalabra =  len(lista[indice]) # en una variable almacena el largo de cada indice
			L.append(largoPalabra) # guarda el largo de los elementos en lista vacia L

			maxPalabra = max(L) # determina el mayor para determinar techo, base y pared derecha de asteriscos *
			asterisco = "*"*maxPalabra # crea el tamanio de techo/base de acuerdo a la mayor longitud de elemento en  lista

		lista.insert(0, asterisco) # techo *
		lista.append(asterisco) # base *
		

		for indice in range(len(lista)): # recorre la lista 
			espacios = " "*(maxPalabra-len(lista[indice])) # pared derecha *
			print "*"+lista[indice]+espacios+"*" # devuelve la lista en caja
	else:
		print "***Lista Vacia*** \n"


# Test 
caja(frase.split())
print "\n"
caja(frase2.split())
print "\n"
caja(frase3.split())
print "\n"
caja(frase4.split())
print "\n"
caja(frase5.split())
print "\n"
caja(frase6.split())

