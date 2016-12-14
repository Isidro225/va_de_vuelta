# -*- encoding: utf-8 -*-

casilleros = [(338,-268),(285,-268),(233,-268),(182,-268),(131,-268),(131,-210),(444,-268),(444,-218),(444,-168),
(444,-118),(444,-68),(444,-18),(393,-18),(341,-18),(288,-18),(236,-18),(184,-17),(131,-100),(81,-151),(-26,-151),(27,-151),
(-79,-151),(-131,-151),(-184,-100),(-184,-200),(-184,-306),(-237,-306),(-288,-306),(-339,-306),(-339,-256),(-339,-206),
(-339,-156),(-339,-106),(133,29),(133,79),(133,129),(133,179),(133,229),(133,279),(133,329),(79,329),(27,329),(-25,329),
(-78,329),(-131,329),(-184,329),(-237,329),(-288,329),(81,-18),(31,-18),(-21,-18),(-76,-18),(-128,-18),(-181,-18),
(-235,-18),(-286,-18),(-338,-18),(-338,32),(-338,82),(-338,132),(-338,182),(-338,232)]

casilleros_bifurcacion = [(391,-265),(131,-148),(133,-18),(-185,-151)]

camino_1 = [(391,-265),(338,-268),(285,-268),(233,-268),(182,-268),(131,-268),(131,-210),(131,-148)] #Ordenado, con I en bifurcacion 1 y F en bifurcacion 2
camino_2 = [(391,-266),(444,-268),(444,-218),(444,-168),(444,-118),(444,-68),(444,-18),(393,-18),(341,-18),(288,-18),(236,-18),(184,-17),(133,-18)] #Ordenado, con I en bifurcacion 1 y F en bifurcacion 3
camino_3 = [(131,-147),(131,-100),(133,-17)] #Ordenado, con I en bifurcacion 2 y F en bifurcacion 3
camino_4 = [(131,-149),(81,-151),(27,-151),(-26,-151),(-79,-151),(-131,-151),(-185,-151)] #Ordenado, con I en bifurcacion 2 y F en bifurcacion 4
camino_5 = [(-186,-151),(-184,-100),(-180,-18),(-234,-18),(-285,-18),(-337,-18),(-337,32),(-337,82),(-337,132),(-337,182),(-337,232),(-364,315)] #Ordenado, con I en bifurcacion 4 y F en castillo
camino_6 = [(-184,-151),(-184,-200),(-184,-306),(-237,-306),(-288,-306),(-339,-306),(-339,-256),(-339,-206),(-339,-156),(-339,-106),(-339,-18),(-339,32),(-339,82),(-339,132),(-339,182),(-339,232),(-366,315)] #Ordenado, con I en bifurcacion 4 y F en castillo
camino_7 = [(134,-18),(133,29),(133,79),(133,129),(133,179),(133,229),(133,279),(133,329),(79,329),(27,329),(-25,329),(-78,329),(-131,329),(-184,329),(-237,329),(-288,329),(-365,315)] #Ordenado, con bifurcacion I y F Castillo
camino_8 = [(132,-18),(81,-18),(31,-18),(-21,-18),(-76,-18),(-128,-18),(-181,-18),(-235,-18),(-286,-18),(-338,-18),(-338,32),(-338,82),(-338,132),(-338,182),(-338,232),(-365,316)] #Ordenado, con I en bifurcacion 3 y F en castillo

sorteo_b1 = [camino_1, camino_2]
sorteo_b2 = [camino_3, camino_4]
sorteo_b3 = [camino_7, camino_8]
sorteo_b4 = [camino_5, camino_6]

casillero_castillo = (-365,315)
casillero_mapa = (391,-312)

import random
import pickle
import pilas
import json

from casillero_verde import Adivinanza
from casillero_naranja import Trabalenguas
from casillero_violeta import Chistes
from ahorcado import Ahorcado
from temporizador import Temporizador
from dado import Dado
from ayuda import Ayuda
from musica import Sonido
from pilas.escena import Base

class Tablero(Base):

	def __init__(self, nombre,musica):
		Base.__init__(self)
		self.nombre = nombre
		self.musica = musica
		self.energia = 3

	def fondo(self):
 		pilas.fondos.Fondo('data/img/fondos/tablero_img.png')

 	def escena_ayuda(self):
 		self.sonido_boton.reproducir()
		pilas.almacenar_escena(Ayuda())

 	def act(self):
 		self.dado.activar()
 		self.boton.activar()
 		self.ayuda.activar()

 	def des(self):
 		self.dado.desactivar()
 		self.boton.desactivar()
 		self.ayuda.desactivar()

	def regresar(self):
	 	self.sonido_boton.reproducir()
	 	self.musicaa.solo_detener()
	 	musica = open("data/archivos/musica.txt",'rb')
		self.estado = pickle.load(musica)
		musica.close()
		pilas.mundo.deshabilitar_sonido(False)
		if (self.estado == True):
			self.musica.encender()
		elif(self.estado == False):
			self.musica.apagar()
	 	pilas.recuperar_escena()

	def volver(self):
		def continuar():
			self.sonido_boton.reproducir()
			self.text1.eliminar()
			self.si.eliminar()
			self.no.eliminar()
			self.cartel.eliminar()
			self.act()
			self.timer.continuar()
		def crear_texto():
			self.text1 = pilas.actores.Texto("Esta seguro que desea salir?",fuente="data/fonts/American Captain.ttf",y=100)
			self.si = pilas.actores.Boton(y=-35)
			self.si.definir_imagen('data/img/interfaz/si.png')
			self.si.escala = 0.7
			self.no = pilas.actores.Boton(y=-165)
			self.no.definir_imagen('data/img/interfaz/no.png')
			self.no.escala  = 0.7
			self.si.conectar_presionado(self.regresar)
			self.no.conectar_presionado(continuar)
		self.sonido_boton.reproducir()
		self.timer.stopTimer()
		self.des()
		self.cartel = pilas.actores.Actor('data/img/iconos/cartel.png')
		self.cartel.escala = [1.8,1],0.8
		pilas.mundo.agregar_tarea(1,crear_texto)

	def cargar_sonidos(self):
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.sonido_dado = pilas.sonidos.cargar("data/audio/dice.ogg")
 		self.sonido_teleport = pilas.sonidos.cargar("data/audio/teleport.ogg")
 		self.sonido_vida = pilas.sonidos.cargar("data/audio/pierde_vida.ogg")
 		self.gana_energia = pilas.sonidos.cargar("data/audio/gana_energia.ogg")
 		self.pierde_energia = pilas.sonidos.cargar("data/audio/pierde_energia.ogg")
 		self.gana_partida = pilas.sonidos.cargar("data/audio/victoria.ogg")
 		self.pierde_partida = pilas.sonidos.cargar("data/audio/derrota.ogg")

 	def iniciar(self):
 		self.fondo()
 		archivo = open('data/archivos/usuarios.json', 'r')
 		self.usuarios = json.load(archivo)
 		archivo.close()
 		archivo1 = open('data/archivos/estadisticas.json','r')
 		self.datos = json.load(archivo1)
 		archivo1.close()
 		self.estado = True
 		self.cargar_sonidos()
 		self.crear_tablero()
 		self.iniciar_personaje()
 		self.crear_interfaz()
 		self.casillero_actual = casillero_mapa
 		self.camino_actual = camino_1

 	def iniciar_sonido(self):
		musica = open("data/archivos/musica.txt",'rb')
		est = pickle.load(musica)
		musica.close()
		self.music = pilas.sonidos.cargar("data/audio/Enchanted Festival Loop.ogg")
		if est:
			self.music.reproducir(repetir=True)
		self.musicaa = Sonido(musica=self.music, x= -445 , y=-190, estado=est ,imagen1="data/img/interfaz/on1.png",imagen2="data/img/interfaz/off1.png")

 	def crear_interfaz(self):
 		self.iniciar_sonido()
 		self.boton = pilas.actores.Boton(x=-450, y=-313)
 		self.boton.definir_imagen('data/img/interfaz/atras.png')
 		self.boton.escala = 0.09
 		self.boton.conectar_presionado(self.volver)
 		self.ayuda = pilas.actores.Boton(x=-445, y=-250)
 		self.ayuda.definir_imagen('data/img/interfaz/ayuda.png')
 		self.ayuda.escala = 0.2
 		self.ayuda.conectar_presionado(self.escena_ayuda)

 	def crear_tablero(self):
 		self.mapa()
 		self.castillo()
 		self.flechas()
 		self.crear_casilleros()
 		self.titulo_vidas = pilas.actores.Texto("VIDAS:",fuente="data/fonts/American Captain.ttf", x=355, y=332)
 		self.crear_vidas()
 		self.titulo_energia = pilas.actores.Texto("ENERGIA:",fuente="data/fonts/American Captain.ttf", x=369, y=260)
 		self.crear_energia()
 		self.titulo_tiempo = pilas.actores.Texto("TIEMPO:",fuente="data/fonts/American Captain.ttf", x=369, y=220)
 		self.crear_timer()
 		self.dado=Dado(x= -110,y= 134)
 		self.dado.conectar_presionado(self.tirar_dado)

 	def crear_timer(self):
 		self.timer = Temporizador(x=420,y=220)
 		self.timer.setDatas(self.usuarios[self.nombre]['tiempo'])
 		self.timer.iniciar()
 		pilas.mundo.agregar_tarea_siempre(1,self.timer_preguntar)

 	def timer_preguntar(self):
 		if(self.timer.getTime() == 0):
 			self.perdio()

 	def _cont_energia(self):
 		num = 'x'+str(self.energia)
 		self.contador_energia = pilas.actores.Texto(num,fuente="data/fonts/American Captain.ttf",x=460,y=260)

 	def crear_energia(self):
 		#Rayo
 		self.rayo = pilas.actores.Actor('data/img/iconos/rayo.png',x=430,y=260)
 		self.rayo.escala = 0.050
		#Energia
 		self._cont_energia()

 	def crear_vidas(self):
 		#Vida 1
 		self.vida1 = pilas.actores.Actor('data/img/iconos/corazon.png')
 		self.vida1.escala = 0.050
 		self.vida1.x = 350
 		self.vida1.y = 300
 		#Vida 2
 		self.vida2 = pilas.actores.Actor('data/img/iconos/corazon.png')
 		self.vida2.escala = 0.050
 		self.vida2.x = 390
 		self.vida2.y = 300
 		#Vida 3
 		self.vida3 = pilas.actores.Actor('data/img/iconos/corazon.png')
 		self.vida3.escala = 0.050
 		self.vida3.x = 430
 		self.vida3.y = 300
 		self.vidas = 3

 	def iniciar_personaje(self):
 		self.personaje = pilas.actores.Actor('data/img/iconos/character.png')
 		self.personaje.escala = 0.2
 		self.personaje.x = casillero_mapa[0]
 		self.personaje.y = casillero_mapa[1]
 		self.personaje.decir("Hola! Empecemos a jugar!")

 	def flechas(self):
 		#Flecha 1
 		self.flecha1 = pilas.actores.Actor('data/img/interfaz/flecha_arriba.png',x=-338,y=-62)
 		self.flecha1.escala = 0.040
 		#Flecha 2
 		self.flecha2 = pilas.actores.Actor('data/img/interfaz/flecha_arriba.png',x=-182,y=-59)
 		self.flecha2.escala = 0.040
 		#Flecha 3
 		self.flecha3 = pilas.actores.Actor('data/img/interfaz/flecha_arriba.png',x=132,y=-58)
 		self.flecha3.escala = 0.040
 		#Flecha 4
 		self.flecha4 = pilas.actores.Actor('data/img/interfaz/flecha_abajo.png',x=-184,y=-251)
 		self.flecha4.escala = 0.050

 	def castillo(self):
 		self.casti = pilas.actores.Actor('data/img/iconos/castillo.png',x=-365,y=315)
 		self.casti.escala = 0.11

 	def mapa(self):
 		self.mapita = pilas.actores.Actor('data/img/iconos/mapa.png',x=391,y=-325)
 		self.mapita.escala = 0.08

 	def crear_casilleros(self):
 		self.casi_tele = []
 		self.casi = casilleros[:]
 		self.imagenes_posiciones = casilleros[:]
		self.imagenes = {"data/img/iconos/Casillero.png":self.usuarios[self.nombre]['casillero_normal'],
 		"data/img/iconos/CasilleroVioleta.png":self.usuarios[self.nombre]['casillero_violeta']
 		,"data/img/iconos/CasilleroNaranja.png":self.usuarios[self.nombre]['casillero_naranja']
 		,"data/img/iconos/CasilleroVerde.png":self.usuarios[self.nombre]['casillero_verde']
 		,"data/img/iconos/ahorcado.png":4
 		,"data/img/iconos/Casillero_comodin.png":4
 		,"data/img/iconos/pare.png":4
 		,"data/img/iconos/perder_vida.png":4
 		,"data/img/iconos/teletransportacion.png":4}
 		for x in range(0,len(casilleros_bifurcacion)):
 			casillero = pilas.actores.Actor("data/img/iconos/bifurcacion.png")
 			casillero.escala = 0.055
 			casillero.x = casilleros_bifurcacion[x][0]
 			casillero.y = casilleros_bifurcacion[x][1]
 		for x in self.imagenes.keys():
 			for i in range(0,self.imagenes[x]):
 				casillero = pilas.actores.Actor(x)
 				self.posi = random.randrange(0,len(self.casi))
 				casille = self.casi[self.posi]
 				self.casi.remove(casille)
 				self.imagenes_posiciones[self.imagenes_posiciones.index(casille)]=x
 				casillero.x = casille[0]
 				casillero.y = casille[1]
 				casillero.escala = 0.09
 				if (x == "data/img/iconos/teletransportacion.png"):
 					tele = (casillero.x,casillero.y)
 					self.casi_tele.append(tele)
 		self.guardar_imagenes()
 	
 	def guardar_imagenes(self):
 		datos = open("data/archivos/imagenes.json",'w')
 		elementos ={"imagenes":self.imagenes_posiciones,
 					"casilleros":casilleros}
 		datos.write(json.dumps(elementos))
 		datos.close()

 	def actualizar_energia(self):
		archivo_energia = open('data/archivos/energia.txt','rb')
		boolean = pickle.load(archivo_energia)
		archivo_energia.close()
		self.contador_energia.eliminar()
		if(boolean == True):
			self.energia = self.energia + 1
			self.gana_energia.reproducir()
 		else:
 			self.energia = self.energia - 1
 			self.pierde_energia.reproducir()
 		self._cont_energia()
 		if (self.energia == 0):
 			self.perder_vida()

 	def ver_est(self):
		if self.estado:
			self.musicaa.encender()

	def desactivar_sonido(self):
		musica = open("data/archivos/musica.txt",'rb')
		self.estado = pickle.load(musica)
		musica.close()
		if self.estado:
			self.musicaa.apagar()
			pilas.mundo.deshabilitar_sonido(False)

 	def gano(self):
		self.des()
		self.guardar_tiempo()
		self.gana_partida.reproducir()
		pantalla1 = pilas.actores.Actor('data/img/fondos/trono.jpg')
		titulo1 = pilas.actores.Actor('data/img/enunciados/victoria.png')
		titulo1.escala = 0.5
		self.boton1 = pilas.actores.Boton(x=-420, y=-300)
 		self.boton1.definir_imagen('data/img/interfaz/atras.png')
 		self.boton1.escala = 0.1
 		self.boton1.conectar_presionado(self.regresar)

	def perdio(self):
		self.des()
		self.guardar_tiempo()
		self.pierde_partida.reproducir()
		pantalla = pilas.actores.Actor('data/img/fondos/derrota.jpg')
		titulo_perdio = pilas.actores.Actor("data/img/enunciados/derrota.png")
		titulo_perdio.escala = 0.5
		self.boton2 = pilas.actores.Boton(x=-420, y=-300)
 		self.boton2.definir_imagen('data/img/interfaz/atras.png')
 		self.boton2.escala = 0.1
 		self.boton2.conectar_presionado(self.regresar)

 	def perder_vida(self):
 		self.sonido_vida.reproducir()
		self.contador_energia.eliminar()
		if(self.vidas == 3):
			self.vida3.eliminar()
			self.vidas -= 1
			self.energia = 3
			self._cont_energia()
		elif(self.vidas == 2):
			self.vida2.eliminar()
			self.vidas -= 1
			self.energia = 3
			self._cont_energia()
		elif(self.vidas == 1):
			self.des()
			self.energia = 0
			self._cont_energia()
			self.vida1.eliminar()
			self.perdio()

	def teletransportacion(self):
		self.sonido_teleport.reproducir()
		self.personaje.escala = [0.4,0.2],1.5
		casillero_tele = random.choice(self.casi_tele)
		self.casillero_actual = casillero_tele
		if(self.casillero_actual in camino_1):
			self.camino_actual = camino_1
		elif(self.casillero_actual in camino_2):
			self.camino_actual = camino_2
		elif(self.casillero_actual in camino_3):
			self.camino_actual = camino_3
		elif(self.casillero_actual in camino_4):
			self.camino_actual = camino_4
		elif(self.casillero_actual in camino_5):
			self.camino_actual = camino_5
		elif(self.casillero_actual in camino_6):
			self.camino_actual = camino_6
		elif(self.casillero_actual in camino_7):
			self.camino_actual = camino_7
		elif(self.casillero_actual in camino_8):
			self.camino_actual = camino_8
		self.personaje.x = self.casillero_actual[0]
		self.personaje.y = self.casillero_actual[1]
		self.personaje.escala = [0.3,0.2],1.5

	def retroceder(self):
		i = self.camino_actual.index(self.casillero_actual) - 1
		self.casillero_actual = self.camino_actual[i]
		self.personaje.x = [self.casillero_actual[0]]
		self.personaje.y = [self.casillero_actual[1]]
		#Parches para que funcione al caer en una bifurcacion
		if(self.casillero_actual in camino_2)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0], self.casillero_actual[1]+1)
		if(self.casillero_actual in camino_3)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0], self.casillero_actual[1]-1)
		if(self.casillero_actual in camino_4)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0], self.casillero_actual[1]+1)
		if(self.casillero_actual in camino_5)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0]+1, self.casillero_actual[1])
		if(self.casillero_actual in camino_6)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0]-1, self.casillero_actual[1])
		if(self.casillero_actual in camino_7)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0]-1, self.casillero_actual[1])
		if(self.casillero_actual in camino_8)and(self.camino_actual.index(self.casillero_actual)<1):
			self.casillero_actual = (self.casillero_actual[0]+1, self.casillero_actual[1])
		self.preguntar_accion()

	def guardar_tiempo(self):
		self.timer.stopTimer()
		self.tiempo_pasado = self.timer.getTime()
		self.datos[self.nombre]["tiempo"] = self.tiempo_pasado
		self.datos[self.nombre]["rayos"] = self.energia
		archivo = open('data/archivos/estadisticas.json','w')
		archivo.write(json.dumps(self.datos))
		archivo.close()

 	def preguntar(self):
 		def borrar1():
 			self.izquierda.desactivar()
 			self.izquierda.destruir()
 			self.derecha.desactivar()
 			self.derecha.destruir()
 			self.cartel_bifurcacion.destruir()
 			self.act()
 		def borrar2():
 			self.arriba.desactivar()
 			self.arriba.destruir()
 			self.izquierda.desactivar()
 			self.izquierda.destruir()
 			self.cartel_bifurcacion.destruir()
 			self.act()
 		def borrar3():
 			self.arriba.desactivar()
 			self.arriba.destruir()
 			self.abajo.desactivar()
 			self.abajo.destruir()
 			self.cartel_bifurcacion.destruir()
 			self.act()
 		def bifurcacion1_izquierda():
 			self.camino_actual = camino_1
 			self.casillero_actual = self.camino_actual[0]
 			borrar1()
 		def bifurcacion1_derecha():
 			self.camino_actual = camino_2
 			self.casillero_actual = self.camino_actual[0]
 			borrar1()
 		def bifurcacion2_arriba():
 			self.camino_actual = camino_3
 			self.casillero_actual = self.camino_actual[0]
 			borrar2()
 		def bifurcacion2_izquierda():
 			self.camino_actual = camino_4
 			self.casillero_actual = self.camino_actual[0]
 			borrar2()
 		def bifurcacion3_arriba():
 			self.camino_actual = camino_7
 			self.casillero_actual = self.camino_actual[0]
 			borrar2()
 		def bifurcacion3_izquierda():
 			self.camino_actual = camino_8
 			self.casillero_actual = self.camino_actual[0]
 			borrar2()
 		def bifurcacion4_arriba():
 			self.camino_actual = camino_5
 			self.casillero_actual = self.camino_actual[0]
 			borrar3()
 		def bifurcacion4_abajo():
 			self.camino_actual = camino_6
 			self.casillero_actual = self.camino_actual[0]
 			borrar3()
		self.cartel_bifurcacion = pilas.actores.Actor('data/img/iconos/cartel_bifurcacion.png',x=8,y=100)
		self.cartel_bifurcacion.escala = 1	
		if (self.casillero_actual == (391,-265)):
			self.izquierda = pilas.actores.Boton(x=10,y=175)
			self.izquierda.definir_imagen('data/img/interfaz/izquierda.png')
			self.izquierda.escala = 0.5
			self.derecha = pilas.actores.Boton(x=10,y=120)
			self.derecha.definir_imagen('data/img/interfaz/derecha.png')
			self.derecha.escala = 0.5
			self.izquierda.conectar_presionado(bifurcacion1_izquierda)
			self.derecha.conectar_presionado(bifurcacion1_derecha)	
		if (self.casillero_actual == (131,-148)):
			self.arriba = pilas.actores.Boton(x=10,y=175)
			self.arriba.definir_imagen('data/img/interfaz/arriba.png')
			self.arriba.escala = 0.5
			self.izquierda = pilas.actores.Boton(x=10,y=120)
			self.izquierda.definir_imagen('data/img/interfaz/izquierda.png')
			self.izquierda.escala = 0.5
			self.arriba.conectar_presionado(bifurcacion2_arriba)
			self.izquierda.conectar_presionado(bifurcacion2_izquierda)
		if (self.casillero_actual == (133,-18)):
			self.arriba = pilas.actores.Boton(x=10,y=175)
			self.arriba.definir_imagen('data/img/interfaz/arriba.png')
			self.arriba.escala = 0.5
			self.izquierda = pilas.actores.Boton(x=10,y=120)
			self.izquierda.definir_imagen('data/img/interfaz/izquierda.png')
			self.izquierda.escala = 0.5
			self.arriba.conectar_presionado(bifurcacion3_arriba)
			self.izquierda.conectar_presionado(bifurcacion3_izquierda)
		if (self.casillero_actual == (-185,-151)):
			self.arriba = pilas.actores.Boton(x=10,y=175)
			self.arriba.definir_imagen('data/img/interfaz/arriba.png')
			self.arriba.escala = 0.5
			self.abajo = pilas.actores.Boton(x=10,y=120)
			self.abajo.definir_imagen('data/img/interfaz/abajo.png')
			self.abajo.escala = 0.5
			self.arriba.conectar_presionado(bifurcacion4_arriba)
			self.abajo.conectar_presionado(bifurcacion4_abajo)	

	def verde(self):
		pilas.almacenar_escena(Adivinanza(self.nombre,self.datos))

	def naranja(self):
		pilas.almacenar_escena(Trabalenguas(self.nombre,self.datos))

	def violeta(self):
		pilas.almacenar_escena(Chistes())

	def ahorcado_juego(self):
		pilas.almacenar_escena(Ahorcado(self.nombre,self.datos))

	def preguntar_accion(self):
		if(self.casillero_actual in casilleros_bifurcacion):
			pilas.mundo.agregar_tarea(2.5,self.preguntar)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/pare.png"):
			pilas.mundo.agregar_tarea(2.5,self.retroceder)
			pilas.mundo.agregar_tarea(3,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/perder_vida.png"):
			pilas.mundo.agregar_tarea(2.3,self.perder_vida)
			pilas.mundo.agregar_tarea(2.5,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/teletransportacion.png"):
			pilas.mundo.agregar_tarea(2.5,self.teletransportacion)
			pilas.mundo.agregar_tarea(3,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/Casillero.png"):
			pilas.mundo.agregar_tarea(2.5,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/CasilleroVerde.png"):
			pilas.mundo.agregar_tarea(2.5,self.verde)
			pilas.mundo.agregar_tarea(3,self.actualizar_energia)
			pilas.mundo.agregar_tarea(3.2,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/CasilleroVioleta.png"):
			pilas.mundo.agregar_tarea(2,self.desactivar_sonido)
			pilas.mundo.agregar_tarea(2.5,self.violeta)
			pilas.mundo.agregar_tarea(3.4,self.ver_est)
			pilas.mundo.agregar_tarea(4,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/CasilleroNaranja.png"):
			pilas.mundo.agregar_tarea(2.5,self.naranja)
			pilas.mundo.agregar_tarea(3,self.actualizar_energia)
			pilas.mundo.agregar_tarea(3.2,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/ahorcado.png"):
			pilas.mundo.agregar_tarea(2.5,self.ahorcado_juego)
			pilas.mundo.agregar_tarea(3,self.actualizar_energia)
			pilas.mundo.agregar_tarea(3.2,self.act)
		elif (self.imagenes_posiciones[casilleros.index(self.casillero_actual)] == "data/img/iconos/Casillero_comodin.png"):
			def eliminar_cartel():
				self.boton_violeta.desactivar()
				self.boton_violeta.destruir()
				self.boton_naranja.desactivar()
				self.boton_naranja.destruir()
				self.boton_verde.desactivar()
				self.boton_verde.destruir()
				self.cartel_comodin.destruir()
			def conectar_violeta():
				pilas.mundo.agregar_tarea(1,self.desactivar_sonido)
				pilas.mundo.agregar_tarea(1.5,self.violeta)
				pilas.mundo.agregar_tarea(1.6,eliminar_cartel)
				pilas.mundo.agregar_tarea(1.7,self.ver_est)
				pilas.mundo.agregar_tarea(1.9,self.act)
			def conectar_naranja():
				pilas.mundo.agregar_tarea(1.5,self.naranja)
				pilas.mundo.agregar_tarea(1.6,eliminar_cartel)
				pilas.mundo.agregar_tarea(1.7,self.actualizar_energia)
				pilas.mundo.agregar_tarea(1.9,self.act)
			def conectar_verde():
				pilas.mundo.agregar_tarea(1.5,self.verde)
				pilas.mundo.agregar_tarea(1.6,eliminar_cartel)
				pilas.mundo.agregar_tarea(1.7,self.actualizar_energia)
				pilas.mundo.agregar_tarea(1.9,self.act)
			def generar_botones():
				#Boton violeta
				self.boton_violeta = pilas.actores.Boton(x=10,y=87)
				self.boton_violeta.definir_imagen('data/img/interfaz/boton_violeta.png')
				self.boton_violeta.escala = 0.7
				self.boton_violeta.conectar_presionado(conectar_violeta)
				#Boton naranja
				self.boton_naranja = pilas.actores.Boton(x=10,y=-65)
				self.boton_naranja.definir_imagen('data/img/interfaz/boton_naranja.png')
				self.boton_naranja.escala = 0.7
				self.boton_naranja.conectar_presionado(conectar_naranja)
				#Boton verde
				self.boton_verde = pilas.actores.Boton(x=16,y=-225)
				self.boton_verde.definir_imagen('data/img/interfaz/boton_verde.png')
				self.boton_verde.escala = 0.7
				self.boton_verde.conectar_presionado(conectar_verde)
			self.des()
			self.cartel_comodin = pilas.actores.Actor('data/img/iconos/cartel_comodin.png',y=-70)
			self.cartel_comodin.escala = [2.5,2],0.8
			pilas.mundo.agregar_tarea(1,generar_botones)

	def mover(self,mov):
		mover_x = []
		mover_y = []
		for x in mov:
			mover_x.append(x[0])
			mover_y.append(x[1])
		self.personaje.x =pilas.interpolar(mover_x,2)
		self.personaje.y =pilas.interpolar(mover_y,2)

 	def tirar_dado(self):
 		self.sonido_dado.reproducir()
		n = self.dado.tirar()
		mov = []
		self.des()
		for x in range(n):
			#Movimiento en camino_1
			if(self.casillero_actual in camino_1)and(self.camino_actual.index(self.casillero_actual)<len(camino_1)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_1)and(self.camino_actual.index(self.casillero_actual)==len(camino_1)-1)and(x<n):
				self.camino_actual = random.choice(sorteo_b2)
				self.casillero_actual = self.camino_actual[0]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_1)and(self.camino_actual.index(self.casillero_actual)==len(camino_1)-1)and(x==n):
				self.casillero_actual = casilleros_bifurcacion[1]
				mov.append(self.casillero_actual)
			#Movimiento en camino_2
			if(self.casillero_actual in camino_2)and(self.camino_actual.index(self.casillero_actual)<len(camino_2)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_2)and(self.camino_actual.index(self.casillero_actual)==len(camino_2)-1)and(x<n):
				self.camino_actual = random.choice(sorteo_b3)
				self.casillero_actual = self.camino_actual[0]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_2)and(self.camino_actual.index(self.casillero_actual)==len(camino_2)-1)and(x==n):
				self.casillero_actual = casilleros_bifurcacion[2]
				mov.append(self.casillero_actual)
			#Movimiento en camino_3
			if(self.casillero_actual in camino_3)and(self.camino_actual.index(self.casillero_actual)<len(camino_3)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_3)and(self.camino_actual.index(self.casillero_actual)==len(camino_3)-1)and(x<n):
				self.camino_actual = random.choice(sorteo_b3)
				self.casillero_actual = self.camino_actual[0]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_3)and(self.camino_actual.index(self.casillero_actual)==len(camino_3)-1)and(x==n):
				self.casillero_actual = casilleros_bifurcacion[2]
				mov.append(self.casillero_actual)
			#Movimiento en camino_4
			if(self.casillero_actual in camino_4)and(self.camino_actual.index(self.casillero_actual)<len(camino_4)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_4)and(self.camino_actual.index(self.casillero_actual)==len(camino_4)-1)and(x<n):
				self.camino_actual = random.choice(sorteo_b4)
				self.casillero_actual = self.camino_actual[0]	
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_4)and(self.camino_actual.index(self.casillero_actual)==len(camino_4)-1)and(x==n):
				self.casillero_actual = casilleros_bifurcacion[3]
				mov.append(self.casillero_actual)
			#Movimiento en camino_5
			if(self.casillero_actual in camino_5)and(self.camino_actual.index(self.casillero_actual)<len(camino_5)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_5)and(self.camino_actual.index(self.casillero_actual)==len(camino_5)-1):
				self.casillero_actual = casillero_castillo
				mov.append(self.casillero_actual)
				break
			#Movimiento en camino_6
			if(self.casillero_actual in camino_6)and(self.camino_actual.index(self.casillero_actual)<len(camino_6)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_6)and(self.camino_actual.index(self.casillero_actual)==len(camino_6)-1):
				self.casillero_actual = casillero_castillo
				mov.append(self.casillero_actual)
				break
			#Movimiento en camino_7
			if(self.casillero_actual in camino_7)and(self.camino_actual.index(self.casillero_actual)<len(camino_7)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_7)and(self.camino_actual.index(self.casillero_actual)==len(camino_7)-1):
				self.casillero_actual = casillero_castillo
				mov.append(self.casillero_actual)
				break
			#Movimiento en camino_8
			if(self.casillero_actual in camino_8)and(self.camino_actual.index(self.casillero_actual)<len(camino_8)-1):
				i = self.camino_actual.index(self.casillero_actual) + 1
				self.casillero_actual = self.camino_actual[i]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual in camino_8)and(self.camino_actual.index(self.casillero_actual)==len(camino_8)-1):
				self.casillero_actual = casillero_castillo
				mov.append(self.casillero_actual)
				break
			#Movimiento inicial
			if(self.casillero_actual==casillero_mapa)and(n>1):
				self.camino_actual = random.choice(sorteo_b1)
				self.casillero_actual = self.camino_actual[0]
				mov.append(self.casillero_actual)
			elif(self.casillero_actual==casillero_mapa)and(n==1):
				self.casillero_actual = casilleros_bifurcacion[0]
				mov.append(self.casillero_actual)
		#Parche para que funcione adecuamente el camino 3 con la bifurcacion
		if(self.casillero_actual in camino_3)and(self.camino_actual.index(self.casillero_actual)>1):
			self.casillero_actual = (self.casillero_actual[0], self.casillero_actual[1]-1)
		#Parche para que funcionen adecuadamente los caminos 5 y 6 con los juegos
		if(self.casillero_actual in camino_5)and(self.camino_actual.index(self.casillero_actual)>1):
			self.casillero_actual = (self.casillero_actual[0]-1, self.casillero_actual[1])
			self.camino_actual = camino_8
		if(self.casillero_actual in camino_6)and(self.camino_actual.index(self.casillero_actual)>9):
			self.casillero_actual = (self.casillero_actual[0]+1, self.casillero_actual[1])
			self.camino_actual = camino_8
		#Parche para que funcione adecuadamente el casillero castillo
		if(self.casillero_actual in camino_8)and(self.camino_actual.index(self.casillero_actual)>14):
			self.casillero_actual = (self.casillero_actual[0], self.casillero_actual[1]-1)
		#Movimiento
		self.mover(mov)
		#Final
		if(self.casillero_actual == casillero_castillo):
			pilas.mundo.agregar_tarea(2.5,self.gano)
		else:
			#Acciones a realizar al caer en un casillero determinado
			self.preguntar_accion()