# cerca : num num num -> bool
# retorna True si x es igual a y con precision epsilon
def cerca(x, y, epsilon):
    diferencia = x - y
    return abs(diferencia) < epsilon

# Tests
import math
tolerancia = 0.0001
assert cerca(4.00005, 4.0 , tolerancia)
assert cerca(math.sqrt(2), 1.4142 , tolerancia)
