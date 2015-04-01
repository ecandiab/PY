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

def caja(lista):

	j = 0
	
	for indice in range(len(lista)):
		largoPalabra =  len(lista[indice])
		if largoPalabra > len(lista[j]):
			maxPalabra = largoPalabra
			j = j+1
		
			asterisco = "*"*maxPalabra

	lista.insert(0, asterisco)
	lista.append(asterisco)
	

	for indice in range(len(lista)):
		espacios = " "*(maxPalabra-len(lista[indice]))

		print "*"+lista[indice]+espacios+"*"



print caja(frase3.split())


