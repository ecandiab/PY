# -*- coding: cp1252 -*-
#Clase 7

# Busqueda
# Busqueda de un lista
lista = [20,10,30,10]
lista.index(10)
## 1
lista,index(40) #produce error ValueError

##Como evitar el error ???

# buscar: list -> int
# Buscar valor x en la lista, retorna el primer indice donde se encuentra
# o -1 si no se encuentra

def buscar(x, lista):
        if x in lista: indice = lista.index(x)
        else: indice = -1 #no esta
#Nota: se realizan dos recorridos de la lista

# Busqueda secuencial
# Realizando solu un recorrido de la lista
# buscar: _ list -> int
# Buscar valor x eb la lista, retorna el primer indice donde se encuentre
# o -1 si no se encuetra
def buscar(x, lista):
        for i in range(len(lista)):
                if lista[i] == x;
                        return i
        return -1

# busquedaBinaria: ... list int int -> int
# Buscar valor x en lista ordenada en el segmento [ip, iu], retorna el
# primer indice donde se encuentre o -1 si no se encuentra
# Ejemplo: indice(20, [10,10,20,30,0,80], 3, 5) retorna -1
def busquedaBinaria(x, lista, ip, iu):
        # retorna -1 si lista esta vacia (indice ip es mayor que iu)
        if ip > iu: return -1
        # comparar x con elemento que esta en la mitad
        im = (ip + iu)/2 # indice del medio
        c = cmp(x, lista[im])
        # si son iguales, retorna indice de mitad
        if c == 0: return im
        # si x es menor, buscar en 2da mitad de lista
        if c < 0:
                return busquedaBinaria(x, lista, ip, im-1)
        # si x es mayor, buscar en la 2da mitad de lista
        else:
                return busquedaBinaria(x, lista, im+1, iu)

# Ordenamiento
#---------------

# Algoritmo de seleccion:
# ordenarSeleecion: list -> None
# Ejemplo: ordenarSeleccion([40,20,30,10]) modifica
# lista a [10,20,30,40]

def ordenarSeleccion(lista):
        n = len[lista]
        # repetir n veces
        for ip in range(0,n): #indice del primer valor desordenado
                #encontrar el indice del menor entre valores desordenados
                im = ip
                for i in range(ip, n):
                        if lista[i] < lista[im]:
                                im = i
                # intercambiar manor con el primero
                tmp = lista[ip]
                lista[ip] = lista[im]
                lista[im] = tmp

#Algoritmo Burbuja

elementos = [1,3,5,4,7,9,8,6]
numero = len(elementos)
i= 0
while (i < numero):
    j = i
    while (j < numero):
        if(elementos[i] > elementos[j]):
            temp = elementos[i]
            elementos[i] = elementos[j]
            elementos[j] = temp
        j= j+1
    i=i+1

#  Algoritmo Mergesort

# mergesort: list int int -> None
# Modifica lista y deja ordenado ascendentemente el segmento [ip, iu]
# ejemplo mergesort([40,20,30,10], 0 ,3)
# modifica lista a [10,20,30,40]
def mergesort(lista, ip, iu):
        if ip >= iu: return # caso base
        im = (ip+iu)/ 2 # indice mitad
        mergesort(lista, ip, im) # ordena mitad 1
        mergesort(lista, im+1, iu) # ordena mitad 2
        merge(lista, ip, im, iu) # mezcla mitades MERGE

# Primera invocacion
# mergesort(lista, 0, len(lista)-1)

# merge: list int int int -> None
# modifica lista y mezclasegmentos de lista ordenada [ip, im] e [im+1, iu]
# Ejemplo: merge([10,30,50,20,40,60], 0, 2, 5)
# Modifica lista a [10, 20, 30, 40, 50, 60]
def merge(lista, ip, im, iu):
        listaAux = [] # lista auxiliar
        i1 = ip # indice comienzo primera mitad
        i2 = im+1 # indice comienzo mitad
        while i1 <= im and i2 <= iu:
                #selecciona y copiar el menor valor
                if lista[i1] < lista[i2]:
                        litaAux.append(lista[i1])
                        i1 += 1
                else:
                        litaAux.append(lista[i2])
                        i2 += 1
        #traspasar restantes primera mitad
        #(si quedan)
        while i1 <= im:
                listaAux.append(x[i1])
                i1 +=1
        #traspasar restantes segunda mitad
        #(si quedan)
        while i2 <= iu:
                listaAux.append(x[i2])
                i2 +=1
        #copiar lista auxiliar en original
        for in range(ip, iu+1):
                lista[i] = listaAux[i-ip]

# Algoritmo Quicksort

# quicksort: list int int -> None
# Modifica lista y deja ordenado ascendentemente el segmento [ip, iu]
# Ejemplo: quicksort([40, 20, 30, 10], 0, 3)
# modifica lista a [10, 20, 30, 40]

def quicksort(lista, ip, iu):
        #caso base (0 o 1 elemento)
        if ip >= iu: return
        #particionar (y obtener indice de pivote)
        i = particionar(lista, ip, iu)
        #ordenar primera parte
        quicksort(lista, ip, i-1)
        #ordenar segunda parte
        quicksort(lista, i+1, iu)

#Primera invocacion
#quicksort(lista, 0, len(lista)-1)

# particionar: list int int -> int
# escoge pivote aleatorio, particiona lista
# en rango [ip, iu] y retorna posicion final
# del pivote
def particionar(lista, ip, iu):
        #elegir pivote aleatorio
        import random
        indicePivote = lista[random.randint(ip, iu)
        pivote =lista[indicePivote]
        lista[indicePivote] = lista[ip]
        lista[ip] = pivote
        #repetir hasta que indices se superen
        i = ip+1
        j = iu
        while i <= j:
                #avanzar indice de menores
                while i <= j and lista[i] < pivote:
                        i = i+1
                #retroceder indice de mayores o iguales
                while i <= j and lista[j] >= pivote:
                        j = j-1
                #intercambiar menor con mayor (si corr)
                if i <= j:
                        tmp = lista[i]
                        lista[i] = lista[j]
                        lista[j] = tmp
                i = i+1
                j = j-1
        #pivote a su posicion final
        lista[ip] = lista[j]
        lista[j] = pivote
        return j

# particionar: list int int -> int
# escoge pivote aleatorio, particiona lista en rango [ip, iu]
# y retorna posicion final del pivote
def particionar(lista, ip, iu):
        #elegir pivote aleatorio
        import random
        indicePivote = lista[random.randint(ip, iu)
        pivote =lista[indicePivote]
        lista[indicePivote] = lista[ip]
        lista[ip] = pivote
        #inicializar índice de último de menores
        i = ip
        #recorrer elementos
        for j in range(ip+1,iu+1):
                #si es menor que pivote juntarlo con menores
                if lista[j] < pivote:
                i = i+1
                tmp = lista[i]
                lista[i] = lista[j]
                lista[j] = lista[i]
        #pivote a su posicion final
        lista[ip] = lista[i]
        lista[i] = pivote
        return i


#Algoritmo heapsort
def heapsort(lista,tam):
    for k in range(tam-1,-1,-1):
        for i in range(0,k):
            item=lista[i]
            j=(i+1)/2
            while j>=0 and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=j/2
            lista[i]=item
        temp=lista[0];
    lista[0]=lista[k];
    lista[k]=temp;

# extraer de mayor a menor en caso de ser Max-Heap
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print lista[i]
 
def leeLista():
    lista=[]
    cn=int(raw_input("Cantidad de numeros a ingresar: "))
 
    for i in range(0,cn):
        lista.append(int(raw_input("Ingrese numero %d : " % i)))
    return lista
 
A=leeLista()
heapsort(A,len(A))
imprimeLista(A,len(A))
