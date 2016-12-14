import pilas
import json
from pilas.escena import Base

class General(Base):

	def __init__(self):
		Base.__init__(self)

	def iniciar(self):
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		archivo = open("data/archivos/usuarios.json","r")
		self.datos_usuarios = json.load(archivo)
		archivo.close()
		archivo1 = open("data/archivos/estadisticas.json","r")
		self.datos_estadisticas = json.load(archivo1)
		archivo1.close()
		self.max_consigna = "Ninguna"
		self.interfaz()
		self.calcular()
		self.mostrar()

	def interfaz(self):
		pilas.fondos.Fondo("data/img/fondos/trabalenguas.jpg")
		self.titulo_general = pilas.actores.Actor("data/img/enunciados/general.png", y = 250)
		self.titulo_general.escala = 0.3
		opc = [("Volver",self.volver)]
		self.menu = pilas.actores.Menu(opc ,y=-200 , fuente="data/fonts/American Captain.ttf")
		self.menu.escala = 1.4

 	def volver(self):
 		self.sonido_boton.reproducir()
 		pilas.recuperar_escena()

	def calcular(self):
		self.tiempo_total = 0
		self.max_consigna = "Ninguna"
		sumaahorcado = 0
		sumatrabalenguas = 0
		sumaadivinanza = 0
		self.time_ahorcado = 0
		self.time_adivinanza = 0
		self.time_trabalenguas = 0
		for x in self.datos_estadisticas.keys():
			try:
				t_ahorcado = int(self.datos_estadisticas[x]['tiempo_ahorcado'][0]) / int(self.datos_estadisticas[x]['tiempo_ahorcado'][1])
			except(ZeroDivisionError):
				t_ahorcado = 0
			try:
				t_adivinanza = int(self.datos_estadisticas[x]['tiempo_adivinanza'][0]) / int(self.datos_estadisticas[x]['tiempo_adivinanza'][1])
			except(ZeroDivisionError):
				t_adivinanza = 0
			try:
				t_trabalenguas = int(self.datos_estadisticas[x]['tiempo_trabalenguas'][0]) / int(self.datos_estadisticas[x]['tiempo_trabalenguas'][1])
			except(ZeroDivisionError):
				t_trabalenguas = 0
			self.time_ahorcado = self.time_ahorcado + t_ahorcado
			self.time_trabalenguas = self.time_trabalenguas + t_trabalenguas
			self.time_adivinanza = self.time_adivinanza + t_adivinanza
			intentos_ahorcado = int(self.datos_estadisticas[x]['tiempo_ahorcado'][2])
			intentos_trabalenguas = int(self.datos_estadisticas[x]['tiempo_trabalenguas'][2])
			intentos_adivinanza = int(self.datos_estadisticas[x]['tiempo_adivinanza'][2])
			if((intentos_adivinanza > intentos_trabalenguas)and(intentos_adivinanza > intentos_ahorcado)):
				sumaadivinanza = sumaadivinanza + 1
			elif((intentos_ahorcado > intentos_trabalenguas)and(intentos_ahorcado > intentos_adivinanza)):
				sumaahorcado = sumaahorcado + 1
			elif((intentos_trabalenguas > intentos_adivinanza)and(intentos_trabalenguas > intentos_ahorcado)):
				sumatrabalenguas = sumatrabalenguas + 1
			tiempo = int(self.datos_usuarios[x]['tiempo']) - int(self.datos_estadisticas[x]['tiempo'])
			self.tiempo_total = self.tiempo_total + tiempo
		if(sumaadivinanza >= sumatrabalenguas)and(sumaadivinanza >= sumaahorcado):
			self.max_consigna = "Adivinanza"
		elif(sumaahorcado > sumatrabalenguas)and(sumaahorcado > sumaadivinanza):
			self.max_consigna = "Ahorcado"
		elif(sumatrabalenguas > sumaahorcado)and(sumatrabalenguas > sumaadivinanza):
			self.max_consigna = "Trabalenguas"
		self.promedio_ahorcado = int(self.time_ahorcado) / int(len(self.datos_estadisticas))
		self.promedio_adivinanzas = int(self.time_adivinanza) / int(len(self.datos_estadisticas))
		self.promedio_trabalenguas = int(self.time_trabalenguas) / int(len(self.datos_estadisticas))

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

	def mostrar(self):
		self.tiempo_promedio = int(self.tiempo_total) / int(len(self.datos_estadisticas))
		self.tiempo_promedio = self.transformar(self.tiempo_promedio)
		self.promedio_adivinanzas = self.transformar(self.promedio_adivinanzas)
		self.promedio_trabalenguas = self.transformar(self.promedio_trabalenguas)
		self.promedio_ahorcado = self.transformar(self.promedio_ahorcado)
		self.enunciado1 = pilas.actores.Texto("Consigna en la que mas se equivocaron:" , fuente="data/fonts/American Captain.ttf", x=-100 , y= 130)
		self.respuesta1 = pilas.actores.Texto(self.max_consigna , fuente="data/fonts/American Captain.ttf",x = 170 , y = 130)
		self.enunciado2 = pilas.actores.Texto("El tiempo promedio de las partidas es de:", fuente="data/fonts/American Captain.ttf", x=-100 , y= 80)
		self.respuesta2 = pilas.actores.Texto(self.tiempo_promedio, fuente="data/fonts/American Captain.ttf", x=170 , y= 80)
		self.enunciado3 = pilas.actores.Texto("El tiempo promedio de las adivinanzas es de:", fuente="data/fonts/American Captain.ttf", x=-100 , y= 30)
		self.respuesta3 = pilas.actores.Texto(self.promedio_adivinanzas, fuente="data/fonts/American Captain.ttf", x=170  , y= 30)
		self.enunciado4 = pilas.actores.Texto("El tiempo promedio de los trabalenguas es de:", fuente="data/fonts/American Captain.ttf", x=-100 , y= -20)
		self.respuesta4 = pilas.actores.Texto(self.promedio_trabalenguas, fuente="data/fonts/American Captain.ttf", x=170  , y= -20)
		self.enunciado5 = pilas.actores.Texto("El tiempo promedio de los ahorcados es de:", fuente="data/fonts/American Captain.ttf", x=-100 , y= -70)
		self.respuesta5 = pilas.actores.Texto(self.promedio_ahorcado, fuente="data/fonts/American Captain.ttf", x=170 , y= -70)