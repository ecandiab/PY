#Clase 6

# TDA Pilas
#Problema
# leer las lineas de un archivo de texto y guardarlas al reves.
     # - Leer lineas del archivo y guardarlas en una pila
     # - Sacar las lineas de la pila (salen en orden inverso) y grabarlas en el archivo

# Solucion 1

#leer lineas y ponerlas en stack
pila = Stack()
archivo = raw_input("nombre del archivo ?")
lector = open(archivo, "r")
for linea in lector:
        if pila.full():
                exit("muchas lineas")
        else:
                pila.push(linea)
lector.close()
#sacar y grabar lineas Stack
escritor = open(archivo, "w")
while not pila.empty():
        escritor.write(pila.pop())
escritor.close()
print "listo"


# Solucion 2

#leer lineas y ponerlas en stack
pila = Stack()
archivo = raw_input("nombre del archivo ?")
lector = open(archivo, "r")
try:
        for linea in open(archivo, "r"):
                pila.push(linea)
except StackFull:
        exit("muchas lineas")
lector.close()

#sacar y grabar lineas del stack
escritor = open(archivo, "w")
try:
        while True:
                escritor.write(pila.pop())
except stackEmpty:
        escritor.close()
        print "listo"

# TDA Cola (Queue)
# problema
# Simular una cola de atencion de clientes de acuerdo al siguiente dialogo:
# evento? 1
# cliente? A                            Eventos:
# evento? 1                             1 = llegada de cliente
# cliente? B                            2 = atencion de cliente
# evento? 2                             0 = fin de eventos
# se atiende ? A
# evento? 1
# cliente? C
# evento? 0

#Solucion
cola = Queue()
while True:
        evento = raw_input("evento ? ")
        if evento == 0:
                break
        elif evento == 1:
                try:
                        pila.enque(raw_input("cliente ?"))
                except QueueFull:
                        print "no hay espacio"
        elif evento == 2:
                try:
                        print "se atiende a", pila.deque()
                except QueueEmpty:
                        print "no hay clientes"
        else:
                print "evento incorrecto"

# TDA Diccionario
# problema
tel = {'jack': 4098, 'sape': 4139}
tel['guido']=4127
tel
## {'sape': 4139, 'guido': 4127, 'jack': 4098}
tel['jack']
## 4098
del tel['sape']
tel['irv'] = 4127
tel
## {'guido': 4127, 'irv': 4127, 'jack': 4098}
tel.keys()
## ['guido','irv','jack']
'guido' in tel
## True
tel.values() # solo los valores
tel.items()  # Todos los valores y palabras





####### MIN HEAP #########



# insertar: int -> None
# Inserta el valor val en la cola de prioridad
# manteniendo su propiedad de min-heap
def insertar(self, val):
    self.lista.append(val)
    j = len(self.lista) - 1
    
    while j > 1:
        if self.lista[j] < self.lista[j/2]:
            tmp = self.lista[j]
            self.lista[j] = self.lista[j/2]
            self.lista[j/2] = tmp
        j = j/2