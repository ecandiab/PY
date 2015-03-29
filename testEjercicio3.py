from Automovil import *
from cerca import cerca

# tests

class Test:
    
    def __init__(self):
        pass

    def test(self):
        auto = Automovil("Porsche", "911", 2015, 60.0, 65.0, 5.5)
        eps = 0.00001


        # chequear combustible
        assert cerca(auto.getCombustible(), 60.0, eps)
        print "El auto tiene: "+str(auto.getCombustible())+" Lts. de combustible."

        # auto no esta en panne
        assert not auto.panne()
        print "El auto esta en pana? "+str(auto.panne())
        
        # # avanzar 110 kilometros
        auto.avanzar(110.0)

        # # chequear combustible
        assert cerca(auto.getCombustible(), 40.0, eps)
        print "Ahora el auto tiene: "+str(auto.getCombustible())+" Lts. de combustible."


        # llenar estanque con 1000 litros, solo se pueden echar 25
       # assert cerca(auto.llenarEstanque(1000.0), 25.0, eps)
        print "Solo se cargo la maxima cantidad posible en este momento en estanque: "+str(auto.llenarEstanque(1000.0))+" Lts."

        # chequear combustible
        assert cerca(auto.getCombustible(), 65.0, eps)
        print "Ahora el auto tiene: "+str(auto.getCombustible())+" Lts. de combustible."

       
        # avanzar 1000 km, solo puede recorrer 357.5
       # assert cerca(auto.avanzar(1000.0), 357.5, eps)
        print "Se avanzaron "+str(auto.avanzar(1000.0))+" Km."

        # auto debe estar en panne de combustible
        assert auto.panne()
        print "El auto esta en pana? "+str(auto.panne())


# Ejecutar tests
t = Test()
t.test()
