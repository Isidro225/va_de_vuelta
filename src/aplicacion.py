import pilas
import json
import sys
from pilas.escena import Base
from estadisticas import jugadores
from creds import Credits

class App(Base):

	def __init__(self):
		Base.__init__(self)

	def iniciar(self):
		self.fondo()
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.interfaz()

	def fondo(self):
		f = pilas.fondos.Fondo("data/img/fondos/aplicacion.jpg")

	def interfaz(self):
		titulo = pilas.actores.Actor("data/img/enunciados/estadisticapp.png",y=250)
		titulo.escala= [0.5,0.4],1
		opciones = [("Estadisticas", self.estadisticas),("Creditos",self.creditos),("Salir",self.salir)]
		menu = pilas.actores.Menu(opciones,y=50,fuente="data/fonts/American Captain.ttf")
		menu.escala = 1.3

	def estadisticas(self):
		self.sonido_boton.reproducir()
		pilas.almacenar_escena(jugadores())

	def creditos(self):
		self.sonido_boton.reproducir()
		pilas.almacenar_escena(Credits())

	def salir(self):
		self.sonido_boton.reproducir()
		sys.exit(0)



