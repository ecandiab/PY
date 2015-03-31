# Campos
# lista: list(int)

from lista import *

class ColaPrioridad:

    # __init__: None -> ColaPrioridad
    # crea una cola de prioridad vacia
    def __init__(self):
        self.lista = [None]

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

            

    # extraerMinimo: None -> int
    # Saca el valor minimo de la cola de prioridad y lo retorna
    # manteniendo la propiedad de min-heap de la cola de prioridad
    def extraerMinimo(self):

        print self.lista
        minimo = self.lista[1]
        ultimoVal = self.lista.pop()
        self.lista[1] = ultimoVal
        self.lista.pop()
        indiceUno = self.lista[1]
        print self.lista


        hijoIzq = indiceUno*2
        hijoDer = indiceUno*2+1

        while hijoIzq in self.lista

        if hijoIzq > hijoDer # cuando el DERECHO derecho es el menor
            if hijoDer > indiceUno:
                break
                else:
                    hijoDer = indiceUno
                    #ACTUALIZAR CASILLERO DEL INDICE
                    return #menor valor

            else: hijoIzq > hijoDer # cuando el hijo IZQUIERDO es el menor
                if hijoDer > indiceUno:
                    break
                else:
                    hijoDer = indiceUno
                    #ACTUALIZAR CASILLERO DEL INDICE
                    return #menor valor        





 




       

# Tests
heap = ColaPrioridad()
heap.insertar(45)
heap.insertar(40)
heap.insertar(60)
heap.insertar(52)
heap.insertar(95)
heap.insertar(73)
heap.insertar(10)
heap.insertar(22)
heap.insertar(15)
heap.insertar(38)
heap.insertar(33)

assert heap.lista == [None, 10, 15, 40, 22, 33, 73, 60, 52, 45, 95, 38]
assert heap.extraerMinimo() == 10
assert heap.extraerMinimo() == 15
assert heap.extraerMinimo() == 22
assert heap.extraerMinimo() == 33
assert heap.extraerMinimo() == 38
assert heap.extraerMinimo() == 40
assert heap.extraerMinimo() == 45
assert heap.extraerMinimo() == 52
assert heap.extraerMinimo() == 60
assert heap.extraerMinimo() == 73
assert heap.extraerMinimo() == 95
assert heap.lista == [None]
