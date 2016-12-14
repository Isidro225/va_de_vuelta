# -*- encoding: utf-8 -*-

frutas = ["frutilla","pera","limon","lima","banana","naranja","mandarina","kiwi","mango","manzana","uva",
"higo","ciruela","frambuesa","sandia","melon","pomelo","arandano","coco","anana","melocoton","maracuya",
"cereza"]

animales = ["gato","perro","leon","ballena","pato","cocodrilo","panda",
"oso","cerdo","gallina","gallo","jirafa","foca","elefante","tortuga",
"vaca","camello","raton","tigre","zebra","topo","paloma","aguila","rana",
"vibora","rinoceronte","hiena","buitre","gorila","avestruz","gacela"]

meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

instrumentos = ["flauta","saxofon","piano","guitarra","organo","bajo","bateria","acordeon","armonica","arpa","clarinete",
"oboe","pandereta","trompeta","trombon","banyo","campana","clarin","tambor","violin","violonchelo","xilofono"]

cord_letras = [(-438,156),(-368,156),(-298,156),(-228,156),(-158,156),(-88,156),(-18,156),(-438,76),(-368,76),(-298,76),(-228,76),(-158,76),(-88,76),(-18,76),(-438,-4),(-368,-4),(-298,-4),(-228,-4),(-158,-4),(-88,-4),(-18,-4),(-368,-84),(-298,-81),(-228,-84),(-158,-84),(-88,-84)]
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

import pilas
import pickle
import json
import random
from letras import Letra
from pilas.escena import Base
from temporizador import Temporizador

class Ahorcado(Base):

	def __init__(self, nombre='',datos =''):
		Base.__init__(self)
		self.nombre = nombre
		archivo = open("data/archivos/usuarios.json",'r')
		dato = json.load(archivo)
		archivo.close()
		self.tema = dato[self.nombre]["tema_ahorcado"]
		self.datos = datos
		self.intentos = 6

	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/ahorcado.jpg")

	def iniciar(self):
		self.fondo()
		self.crear_letras()
		self.titulo = pilas.actores.Actor("data/img/enunciados/ahorcado.png", y= 250)
		self.titulo.escala = 0.4
		palo_ahorcado = pilas.actores.Actor('data/img/iconos/palo_ahorcado.png',x=280,y=100)
		palo_ahorcado.escala = 2
		self.generar_palabra()
	
	def crear_letras(self):
		self.lista_letras = []
		for x in range(len(letras)):
			self.actor_letra = Letra(letra=letras[x], x=cord_letras[x][0], y=cord_letras[x][1])
			self.actor_letra.escala = 0.74
			self.lista_letras.append(self.actor_letra)
			self.actor_letra.activar()
			self.actor_letra.conectar_presionado(self.presiona_tecla, arg=x)

	def presiona_tecla(self, x):
		self.actor_letra = self.lista_letras[x]
		letra_mayus = self.actor_letra.getLetra()
		self.letra = letra_mayus.lower()
		self.intentar()

	def generar_palabra(self):
		#Timer
		self.time = Temporizador(x=-250,y=300)
		self.time.setDatas(0)
		self.time.iniciar_aum()
		self.guion = []
		self.letras_utilizadas = []
		self.letras_adivinadas = 0
		if(self.tema == 'Animales'):
			self.palabra = random.choice(animales)
		if(self.tema == 'Frutas'):
			self.palabra = random.choice(frutas)
		if(self.tema == 'Meses'):
			self.palabra = random.choice(meses)
		if(self.tema == 'Instrumentos'):
			self.palabra = random.choice(instrumentos)
		if (len(self.palabra) <= 5):
			self.posx = -270
			for x in range(0,len(self.palabra)):
				self.actor_guion = pilas.actores.Actor("data/img/interfaz/guion.png",x=self.posx,y=-280)
				self.guion.append(self.posx)
				self.posx = self.posx + 100
				self.actor_guion.escala = 0.12
		elif(len(self.palabra) <= 9):
			self.posx = -400
			for x in range(0,len(self.palabra)):
				self.actor_guion = pilas.actores.Actor("data/img/interfaz/guion.png",x=self.posx,y=-280)
				self.guion.append(self.posx)
				self.posx = self.posx + 100
				self.actor_guion.escala = 0.12
		else:
			self.posx = -450
			for x in range(0,len(self.palabra)):
				self.actor_guion = pilas.actores.Actor("data/img/interfaz/guion.png",x=self.posx,y=-280)
				self.guion.append(self.posx)
				self.posx = self.posx + 80
				self.actor_guion.escala = 0.09

	def gano(self):
		for y in range(0,len(self.lista_letras)):
			self.actor_letra = self.lista_letras[y]
			self.actor_letra.desactivar()
		self.profesor = pilas.actores.Actor("data/img/iconos/profesor.png",x=500,y=-180)
		self.profesor.escala = 0.095
		self.profesor.x = [440]
		self.profesor.decir('Bien echo, ganaste 1 punto mas de energia!')
		self.ener = True
		pilas.mundo.agregar_tarea(1,self.profesor.eliminar)
		pilas.avisar('Volviendo al tablero..')
		pilas.mundo.agregar_tarea(2,self.volver)	

	def perdio(self):
		self.profesor = pilas.actores.Actor("data/img/iconos/profesor.png",x=500,y=-180)
		self.profesor.escala = 0.095
		self.profesor.x = [440]
		self.profesor.decir('Lo siento, perdiste 1 punto de energia!')
		self.ener = False
		pilas.mundo.agregar_tarea(1,self.profesor.eliminar)
		pilas.avisar('Volviendo al tablero..')
		pilas.mundo.agregar_tarea(2,self.volver)	

	def cuerpo(self):
		if(self.intentos == 5):
			cabeza = pilas.actores.Actor('data/img/iconos/cabeza.png',x=263,y=190)
		if(self.intentos == 4):
			torzo = pilas.actores.Pizarra()
			torzo.linea(263,152,263,20,pilas.colores.negro,grosor=6)
		if(self.intentos == 3):
			brazo_derecho = pilas.actores.Pizarra()
			brazo_derecho.linea(263,130,210,95,pilas.colores.negro,grosor=6)
		if(self.intentos == 2):
			brazo_izquierdo = pilas.actores.Pizarra()
			brazo_izquierdo.linea(263,130,316,95,pilas.colores.negro,grosor=6)
		if(self.intentos == 1):
			pierna_derecha = pilas.actores.Pizarra()
			pierna_derecha.linea(263,20,218,-34,pilas.colores.negro,grosor=6)
		if(self.intentos == 0):
			pierna_izquierda = pilas.actores.Pizarra()
			pierna_izquierda.linea(263,20,308,-34,pilas.colores.negro,grosor=6)
			self.perdio()

	def intentar(self):
		no_se_encuentra = True
		indice = 0
		if(self.intentos == 0):
			self.perdio()
		else:
			if(self.letra in self.letras_utilizadas):
				self.profesor = pilas.actores.Actor("data/img/iconos/profesor.png",x=500,y=-180)
				self.profesor.escala = 0.095
				self.profesor.x = [440]
				self.profesor.decir('Ya utilizaste esa letra!')
				pilas.mundo.agregar_tarea(2,self.profesor.eliminar)
			else:
				for x in self.palabra:
					if(self.letra == x):
						no_se_encuentra = False
						break
				if(no_se_encuentra == True):
					self.profesor = pilas.actores.Actor("data/img/iconos/profesor.png",x=500,y=-180)
					self.profesor.escala = 0.095
					self.profesor.x = [440]
					self.profesor.decir('Ups, esa letra no se encuentra en la palabra!')
					pilas.mundo.agregar_tarea(2,self.profesor.eliminar)
					self.letras_utilizadas.append(self.letra)
					self.intentos = self.intentos-1
					self.cuerpo()
				else:
					for x in self.palabra:
						if (self.letra==x) and (self.letras_adivinadas<len(self.palabra)):
							self.letra_adivinada = pilas.actores.Texto(x,fuente="data/fonts/American Captain.ttf",y=-258)
							self.letra_adivinada.escala = 2
							self.letra_adivinada.color = pilas.colores.negro 
							self.letra_adivinada.x = self.guion[indice]
							self.letras_adivinadas = self.letras_adivinadas + 1
							self.letras_utilizadas.append(x)	
							if (self.letras_adivinadas == len(self.palabra)):
								self.gano()
						indice = indice + 1

	def volver(self):
		self.time.stopTimer()
		self.datos[self.nombre]['tiempo_ahorcado'][0] = self.datos[self.nombre]['tiempo_ahorcado'][0] + self.time.getTime()
		self.datos[self.nombre]['tiempo_ahorcado'][1] = self.datos[self.nombre]['tiempo_ahorcado'][1] + 1
		if(self.ener == False):
			self.datos[self.nombre]['tiempo_ahorcado'][2] = self.datos[self.nombre]['tiempo_ahorcado'][2] + 1	
		f = open("data/archivos/estadisticas.json","w")
		f.write(json.dumps(self.datos))
		f.close()
		e = open("data/archivos/energia.txt",'wb')
		pickle.dump(self.ener,e)
		e.close()
		pilas.recuperar_escena()