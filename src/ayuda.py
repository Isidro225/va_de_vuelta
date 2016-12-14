import pilas
from pilas.escena import Base

class Ayuda(Base):

	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/ayuda_imagen.jpg")

	def volver(self):
		self.sonido_boton.reproducir()
		pilas.recuperar_escena()

	def iniciar(self):
		self.fondo()
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.boton = pilas.actores.Boton(x=-450,y=-260)
		self.boton.definir_imagen("data/img/interfaz/boton_volver.png")
		self.boton.escala = 0.3
		self.boton.conectar_presionado(self.volver)