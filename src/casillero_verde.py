#Definciones - pistas

adivinanzas=["Soy astuto y jugueton y cazar un raton es mi mayor aficion.",
"Dos pinzas tengo, hacia atras camino, de mar o de rio en el agua vivo.",
"Guau de noche , guau de dia , cazo y ladro , adivina quien seria",
"Vuelo entre las flores , vivo en la colmena , fabrico la miel y tambien la cera",
"Es la reina de los mares , su dentaruda es muy buena y por no ir nunca vacia , siempre dicen que va llena",
"Tengo grandes garras , y una larga melena , y digo que la carne de explorador , esta muy buena"]

lista=['gato','cangrejo','perro','abeja','ballena','leon']

import pilas
import random
import pickle
import json
from temporizador import Temporizador
from pilas.escena import Base
from pilas.actores import Boton

class Animal(Boton):

	def __init__(self,x=200,y=200,imagen =''):
		Boton.__init__(self,x=x,y=y)
		self.elemento = imagen
		self.gato = pilas.imagenes.cargar('data/img/animales/gato.png')
		self.cangrejo = pilas.imagenes.cargar('data/img/animales/cangrejo.png')
		self.perro = pilas.imagenes.cargar('data/img/animales/perro.png')
		self.abeja = pilas.imagenes.cargar('data/img/animales/abeja.png')
		self.ballena = pilas.imagenes.cargar('data/img/animales/ballena.png')
		self.leon = pilas.imagenes.cargar('data/img/animales/leon.png')
		self.definir()

	def definir(self):
		if(self.elemento == 'gato'):
			self.imagen = self.gato
		if(self.elemento == 'cangrejo'):
			self.imagen = self.cangrejo
		if(self.elemento == 'perro'):
			self.imagen = self.perro
		if(self.elemento == 'abeja'):
			self.imagen = self.abeja
		if(self.elemento == 'ballena'):
			self.imagen = self.ballena
		if(self.elemento == 'leon'):
			self.imagen = self.leon

	def getElemento(self):
		return self.elemento
		
class Adivinanza(Base):

	def __init__(self,nombre='',datos = ''):
		Base.__init__(self)
		self.nombre = nombre
		self.datos = datos

	def iniciar(self):
		self.fondo()
		self.interfaz()
		self.generar()

	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/adivinanza.jpg")

	def interfaz(self):
		#Timer
		self.time = Temporizador(x=-250,y=300)
		self.time.setDatas(0)
		self.time.iniciar_aum()
		#Titulo
		self.texto_titulo = pilas.actores.Actor("data/img/enunciados/adivinanza.png",y=270)
		self.texto_titulo.escala = 0.5
		#Recuadro
		self.recuadro = pilas.actores.Actor("data/img/interfaz/recuadrito.png",x = -20,y = 50)
		self.recuadro.escala = 0.4
		#Personaje
		self.personaje = pilas.actores.Actor("data/img/iconos/character.png",y=-150)
		self.personaje.escala = 0.26
		self.personaje.decir("Clickea en el animal al que hace referencia la adivinanza") ###dialogo
		#Adivinanza
		numero = random.randrange(0,6)
		self.adivinanza = adivinanzas[numero]
		self.texto = pilas.actores.Texto(self.adivinanza,fuente="data/fonts/American Captain.ttf", y = 50 , ancho = 256 )
		self.texto.color = pilas.colores.negro

	def generar(self):
		self.lista_elemento = []
		coor = [(-300,0),(280,-200),(280,200),(280,0),(-280,-200),(-280,200)]
		for x in range(len(lista)):
			self.elemento = Animal(x=coor[x][0],y=coor[x][1],imagen=lista[x])
			self.elemento.escala = 0.6
			self.lista_elemento.append(self.elemento)
			self.elemento.activar()
			self.elemento.conectar_presionado(self.verificar, arg=x)

	def verificar(self,x):
		self.elemento = self.lista_elemento[x]
		seleccion = self.elemento.getElemento()
		if(lista.index(seleccion)== adivinanzas.index(self.adivinanza)):
			self.personaje.decir("Bien hecho , ganaste un rayo de energia")
			self.ener = True
		else:
			self.personaje.decir("Respuesta incorrecta , perdiste un rayo")
			self.ener = False
		pilas.mundo.agregar_tarea(2,self.volver)

	def volver(self):
		self.time.stopTimer()
		self.datos[self.nombre]['tiempo_adivinanza'][0] = self.datos[self.nombre]['tiempo_adivinanza'][0] + self.time.getTime()
		self.datos[self.nombre]['tiempo_adivinanza'][1] = self.datos[self.nombre]['tiempo_adivinanza'][1] + 1
		if(self.ener == False):
			self.datos[self.nombre]['tiempo_adivinanza'][2] = self.datos[self.nombre]['tiempo_adivinanza'][2] + 1	
		f = open("data/archivos/estadisticas.json","w")
		f.write(json.dumps(self.datos))
		f.close()
		e = open("data/archivos/energia.txt",'wb')
		pickle.dump(self.ener,e)
		e.close()
		pilas.recuperar_escena()