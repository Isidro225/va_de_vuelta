chistes = ["data/audio/chiste1.wav","data/audio/chiste2.wav","data/audio/chiste3.wav","data/audio/chiste4.wav","data/audio/chiste5.wav","data/audio/chiste6.wav",
		   "data/audio/chiste7.wav"]

import pilas
import random

from pilas.escena import Base

class Chistes(Base):

	def __init__(self):
		Base.__init__(self)

	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/fondo_chistes.jpg")

	def volver(self):
		self.sonido_boton.reproducir()
		pilas.recuperar_escena()

	def iniciar(self):
		self.fondo()
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.chiste()

	def chiste(self):
		self.chistee = random.choice(chistes)
		self.audio = pilas.sonidos.cargar(self.chistee)
		self.audio.reproducir()
		self.boton = pilas.actores.Boton(x=-450, y=-250)
 		self.boton.definir_imagen("data/img/interfaz/boton_volver.png")
 		self.boton.escala = 0.4
 		self.boton.conectar_presionado(self.cambiar_estado)

	def cambiar_estado(self):
		self.audio.detener()
		pilas.mundo.agregar_tarea(1,self.volver)