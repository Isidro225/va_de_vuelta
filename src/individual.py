import pilas
import json

from pilas.escena import Base


class Individual(Base):

	def iniciar(self):
		archivo = open("data/archivos/usuarios.json","r")
		self.datos_usuarios = json.load(archivo)
		archivo.close()
		archivo1 = open("data/archivos/estadisticas.json","r")
		self.datos_estadisticas = json.load(archivo1)
		archivo1.close()
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.fondo()
		self.calcular()
		self.enunciado1 = pilas.actores.Texto(" ")

	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/trabalenguas.jpg")
		opc = [("Volver",self.volver)]
		self.menu = pilas.actores.Menu(opc ,y=-350 , fuente="data/fonts/American Captain.ttf")
		self.menu.escala = 1.4

	def volver(self):
		self.sonido_boton.reproducir()
		pilas.recuperar_escena()

	def transformar(self,time):
		minutes=(int(time / 60))
		seconds=time-(minutes * 60)
		secondsStr=str(seconds)
		minutesStr=str(minutes)
		if (len(str(seconds)) < 2): 
			secondsStr = '0'+secondsStr
		if (len(str(minutes)) < 2): 
			minutesStr = '0'+minutesStr
		texto = str(minutesStr) + ":" + str(secondsStr)
		return texto

	def calcular(self):
		lista_coordenadas = [250,230,210,190,170,150,130,110,90,70,50,30,10,-10,-30,-50,-70,-90,-110,-130,-150,-170,-190,-210,-230,-250,-270,-290,-310,-330]
		self.usuarios = self.datos_estadisticas.keys()
		self.lista = []
		for x in range(0,len(self.usuarios)):
			if(x < 31):
				yy= lista_coordenadas[x]
				self.enunciado1 = pilas.actores.Texto(str(self.usuarios[x]) ,x = -400 ,y = yy)
				self.enunciado1.escala = 0.5
				if(self.datos_estadisticas[self.usuarios[x]]['tiempo_ahorcado'][2]>0):
					self.enunciado2 = pilas.actores.Texto("Fallo "+str(self.datos_estadisticas[self.usuarios[x]]['tiempo_ahorcado'][2])+" veces", x = -250 , y = yy)
				elif(self.datos_estadisticas[self.usuarios[x]]['tiempo_ahorcado'][0] != 0):
					self.enunciado2 = pilas.actores.Texto("Acerto "+str(self.datos_estadisticas[self.usuarios[x]]['tiempo_ahorcado'][1])+" veces" , x = -250 , y = yy)
				else:
					self.enunciado2 = pilas.actores.Texto("No Jugo", x = -250 , y = yy)
				self.enunciado2.escala = 0.5
				if(self.datos_estadisticas[self.usuarios[x]]['tiempo_adivinanza'][2]>0):
					self.enunciado3 = pilas.actores.Texto("Fallo "+str(self.datos_estadisticas[self.usuarios[x]]['tiempo_adivinanza'][2])+" veces", x = -150 , y = yy)
				elif(self.datos_estadisticas[self.usuarios[x]]['tiempo_adivinanza'][0] != 0):
					self.enunciado3 = pilas.actores.Texto("Acerto "+str(self.datos_estadisticas[self.usuarios[x]]['tiempo_adivinanza'][1])+" veces", x = -150 , y = yy)
				else:
					self.enunciado3 = pilas.actores.Texto("No Jugo", x = -150 , y = yy)
				self.enunciado3.escala = 0.5
				if(self.datos_estadisticas[self.usuarios[x]]['tiempo_trabalenguas'][2]>0):
					self.enunciado4 = pilas.actores.Texto("Fallo "+str(self.datos_estadisticas[self.usuarios[x]]['tiempo_trabalenguas'][2])+" veces", x = -50 , y = yy)
				elif(self.datos_estadisticas[self.usuarios[x]]['tiempo_trabalenguas'][0] != 0):
					self.enunciado4 = pilas.actores.Texto("Acerto "+str(self.datos_estadisticas[self.usuarios[x]]['tiempo_trabalenguas'][1])+" veces", x = -50 , y = yy)
				else:
					self.enunciado4 = pilas.actores.Texto("No Jugo", x = -50 , y = yy)
				self.enunciado4.escala = 0.5
				try:
					t_ahorcado = int(self.datos_estadisticas[self.usuarios[x]]['tiempo_ahorcado'][0]) / int(self.datos_estadisticas[self.usuarios[x]]['tiempo_ahorcado'][1])
				except(ZeroDivisionError):
					t_ahorcado = 0
				try:
					t_adivinanza = int(self.datos_estadisticas[self.usuarios[x]]['tiempo_adivinanza'][0]) / int(self.datos_estadisticas[self.usuarios[x]]['tiempo_adivinanza'][1])
				except(ZeroDivisionError):
					t_adivinanza = 0
				try:
					t_trabalenguas = int(self.datos_estadisticas[self.usuarios[x]]['tiempo_trabalenguas'][0]) / int(self.datos_estadisticas[self.usuarios[x]]['tiempo_trabalenguas'][1])
				except(ZeroDivisionError):
					t_trabalenguas = 0
				tiempo = int(self.datos_usuarios[self.usuarios[x]]['tiempo']) - int(self.datos_estadisticas[self.usuarios[x]]['tiempo'])
				promedio_adivinanzas = self.transformar(t_adivinanza)
				promedio_trabalenguas = self.transformar(t_trabalenguas)
				promedio_ahorcado = self.transformar(t_ahorcado)
				tiempo = self.transformar(tiempo)
				if(tiempo == "20:00"):
					tiempo = "00:00"
				rayos = self.datos_estadisticas[self.usuarios[x]]['rayos']
				self.enunciado5 = pilas.actores.Texto(promedio_ahorcado,x = 50, y = yy)
				self.enunciado5.escala = 0.5
				self.enunciado6 = pilas.actores.Texto(promedio_adivinanzas,x= 150 , y = yy)
				self.enunciado6.escala = 0.5
				self.enunciado7 = pilas.actores.Texto(promedio_trabalenguas,x = 250 , y= yy)
				self.enunciado7.escala = 0.5
				self.enunciado8 = pilas.actores.Texto(tiempo, x = 400 , y= yy)
				self.enunciado8.escala = 0.5
				self.enunciado9 = pilas.actores.Texto(str(rayos) , x = 500 , y = yy)
				self.enunciado9.escala = 0.5
		self.titulo1 = pilas.actores.Texto("Nombres",x = -400 , y = 300)
		self.titulo2 = pilas.actores.Texto("Intentos",x = -150 , y = 320)
		self.titulo6 = pilas.actores.Texto("Tiempos",x = 150 , y = 320)
		self.titulo10 = pilas.actores.Texto("Ultimo Tiempo",x=400,y=300)
		self.titulo10.escala = 0.7
		self.titulo3 = pilas.actores.Texto("Ahorcado",x = -250 , y = 290)
		self.titulo3.escala = 0.5
		self.titulo4 = pilas.actores.Texto("Adivinanza",x = -150 , y = 290)
		self.titulo4.escala = 0.5
		self.titulo5 = pilas.actores.Texto("Trabalenguas",x = -50 , y = 290)
		self.titulo5.escala = 0.5
		self.titulo7 = pilas.actores.Texto("Ahorcado",x = 50 , y = 290)
		self.titulo7.escala = 0.5
		self.titulo8 = pilas.actores.Texto("Adivinanza",x = 150 , y = 290)
		self.titulo8.escala = 0.5
		self.titulo9 = pilas.actores.Texto("Trabalenguas",x = 250 , y = 290)
		self.titulo9.escala = 0.5
		self.titulo11 = pilas.actores.Texto("Rayos",x= 500 , y=300)
		self.titulo11.escala = 0.7