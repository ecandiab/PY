#Campos:

# marca: str
# modelo: str
# ano: int
# combustible: float
# capcidad: float
# rendimiento: float

class Automovil:

	# Constructor 
	def __init__ (self, marca = "", modelo = "", ano = 0, combustible = 0.0, capacidad = 0.0, rendimiento = 0.0):
		
		# Inicializacion de campos
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.combustible = combustible
		self.capacidad = capacidad
		self.rendimiento = rendimiento

	# getCombustible: None -> float
	# Devuelve la cantidad de combustible del auto
	def getCombustible(self):
		return self.combustible

	# setCombustible: float -> float
	# Efecto: modifica el valor del campo combustible
	def setCombustible(self,combustible):
		self.combustible = combustible

	# panne: None -> boolean
	# Devuelve True o False	segun el estado del combustible del auto
	def panne(self):
		if self.combustible > 0.0:
			return False
		else:
			return True

	# avanzar: float -> float
	# Efecto: modifica el campo combustible
	# Devuelve la cantidad de KM recorridos
	# Ejemplo: avanzar(1000.0) -> retorna 357	/ supuesto: si es que en estanque hay 65 lts.
	def avanzar(self,kilometros):

		ltsViaje = (kilometros/self.rendimiento)

	  	if ltsViaje > self.combustible:
	  		maxViaje = self.combustible * self.rendimiento
	  		self.setCombustible(0)
	  		return maxViaje
	  	else: 
	  		litrosGasta = self.combustible - ltsViaje
	  		self.setCombustible(litrosGasta)
			return kilometros

	# llenarEstanque: float -> float
	# Efecto: modifica el campo combustible
	# Devuelve la cantidad de Litros que se llenaron 
	# Ejemplo: llenarEstanque(1000.0) retorna 25 / supuesto: si es que en estanque hay 40 lts.

	def llenarEstanque(self,litros):

		maxlitrosLlenar = (self.capacidad-self.combustible)

		if litros >= maxlitrosLlenar:
			lts = self.combustible + maxlitrosLlenar
			self.setCombustible(lts)
			return maxlitrosLlenar
		else:
			lts2 = self.combustible + litros
			self.setCombustible(lts2)
			return litros




