import pilas
import json
from pilas.escena import Base
from general import General
from individual import Individual

class jugadores(Base):

	def __init__(self):
		Base.__init__(self)
		
	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/aplicacion.jpg")

	def general(self):
		self.sonido_boton.reproducir()
		pilas.almacenar_escena(General())

	def individual(self):
		self.sonido_boton.reproducir()
		pilas.almacenar_escena(Individual())

	def volver(self):
		self.sonido_boton.reproducir()
		pilas.recuperar_escena()

	def iniciar(self):
		self.fondo()
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.interfaz()
		self.mostrar()

	def interfaz(self):
		opcion= [("General",self.general),("Individual",self.individual),("Volver",self.volver)]
		menu = pilas.actores.Menu(opcion, y=50, fuente="data/fonts/American Captain.ttf")
		menu.escala = 1.3
		enunciado = pilas.actores.Actor("data/img/enunciados/estadisticas.png",y=250)
		enunciado.escala = 0.3