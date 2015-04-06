# Resumen Clase 3.
# Estructuras indexadas (String, Listas, Tuplas)

# Estructuras de datos indexada
s = "murcielago"
print s[0]
# m
print s[len(s)-1]
# o

lista = ['ana','maria','luisa','teresa']
len(lista)
# 4

#LISTAS DE PYTHON
lista = [10, 20, 30, 40, 50, 60]
lista[3] = 'X'
lista
# [10, 20, 30, 'X', 50, 60]

# Sublitas
cuadrados = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
cuadrados[3:6]
# [9, 16, 25]

# matriz
matriz = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
matriz[1][2]
# 60

#Instrucciones para iterar sobre estructuras indexadas
#-----------------------------------------------------

lista = [10,20,30,40,50]
for valor in lista:
	print valor
# 10
# 20
# 30
# 40
# 50

lista = [10,20,30,40,50]
for indice in range(len(lista)):
	print lista[indice]
# 10
# 20
# 30
# 40
# 50

lista = [10,20,30,40,50]
indice = 0
while indice < len(lista):
	print lista[indice]
	indice = indice + 1
# 10
# 20
# 30
# 40
# 50

palabra = 'hola'
for caracter in palabra:
	print caracter
# h
# o
# l
# a



Tuplas son listas inmutables de Python
--------------------------------------
# fecha: str -> tupla
# convierte String en formato 'DD/MM/AAAA' a tupla (AAAA,MM,DD)
# ejemplo: fecha('10/04/2014') retorna (2014, 04, 10)
def fecha(x):
	lista = x.split('/') # lista = ['DD','MM','AAAA']
	return (int(lista[2])), (int(lista[1])), (int(lista[0]))
	
Pack y Unpack de Tuplas
-----------------------
#saludar las personas que esten de cumpleaños
#datos en archivo personas.txt
#cada linea del archivo contiene los datos de una persona
#Fecha de Nacimiento: 10 primeros caracteres (formato 'DD/MM/AAAA')
# Nombre: caracter restantes de la linea

print 'fecha de hoy:'
hoy = (input('anno? '), input('mes? '), input('dia? '))

for linea in open('personas.txt'):
	(aNac,mNac,dNac) = fecha(linea[0:10])
	(aHoy,mHoy,dHoy) = hoy
	if (mNac, dNac) == (mHoy, dHoy):
		print 'Feliz cumpleaños ', linea[10: -1]
		
		
Entrada/Salida
--------------
# grabar lineas en un archivo
# abrir (preparar) archivo para escribir (grabar)
escritor = open("lineas.txt", "w")

# leer lineas hasta "fin"
while True:
	lineas = raw_input("palabra (o fin) ?")
	if linea == "fin": break
	#grabar lineas en archivo
	escritor.write(linea+"\n")
	
#cerrar archivo
escritor.close()

"Mostrar el archivo "lineas.txt"
################################
#primera solucion
#leer y mostrar lineas de archivo
lector = open("lineas.txt","r")

#leer lineas hasta detectar fin de archivo
while True:
	linea = lector.readline()
	if linea == "": break
	#mostrar linea
	# print linea[0:len(linea)-1] o linea[0:-1]
	print linea
	
#cerrar archivo
lector.close()

################################
#segunda solucion
#leer y mostrar lineas de archivo
lector = open("lineas.txt","r")

#leer todas las lineas del archivo
for linea in lector:
	#mostrar string (salvo ultimo caracter)
	print linea[0:-1]
	
#cerrar archivo
lector.close()

#################################
# Copia de archivos de texto
#Abrir archivos de entrada y salida
lector = open(raw_input("input? "), "r")
escritor = open(raw_input("output? "), "w")

#copiar todas las lineas del archivo
for linea in lector:
	escritor.write(linea)
#cerrar archivos
lector.close()
escritor.close()


