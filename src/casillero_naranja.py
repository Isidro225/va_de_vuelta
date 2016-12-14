# -*- encoding: utf-8 -*-

trabalenguas = ["La sucesion sucesiva de sucesos sucede sucesivamente con la sucesion del tiempo.",
"Si el caracol tuviera cara como tiene el caracol, fuera cara, fuera col,  fuera caracol con cara.",
"A Cuesta le cuesta subir la cuesta, y en medio de la cuesta, va y se acuesta",
"Compre pocas copas, pocas copas compre, como compre pocas copas, pocas copas pagare.",
"Toto toma te, Tita toma mate, y yo me tomo toda mi taza de chocolate.",
"En un juncal de Junqueira, juncos juntaba Julian. Juntase Juan a juntarlos y juntos juntaron mas.",
"Papa ornitorrinco y sus cinco ornitorrinquitos recorren rincones sequitos.",
"Un tubo tiro un tubo y otro tubo lo detuvo. Hay tubos que tienen tubos pero este tubo no tuvo tubo.",
"Si la sierva que te sirve, no te sirve como sierva, de que sirve que te sirvas de una sierva que no sirve.",
"Treinta y tres tramos de troncos trozaron tres tristes trozadores de troncos y triplicaron su trabajo.",
"Compadre de la capa parda, no compre usted mas capa parda,que el que mucha capa parda compra, mucha capa parda paga.",
"De Guadalajara vengo, jara traigo, jara vendo, a medio doy cada jara. Que jara tan cara traigo de Guadalajara."]

trabalenguas_solucion = [["sucesos","sucesion","sucede"],
["cara","col","caracol"],
["cuesta","acuesta","cueva"],
["copas","pocas","compre"],
["toma","taza","mate"],
["juncal","juntos","juan"],
["ornitorrinco","rincones","cinco"],
["tiro","tubos","detuvo"],
["sierva","sirve","sirvas"],
["tramos","trozadores","troncos"],
["parda","capa","paga"],
["traigo","jara","cara"]]

problemas = ["La sucesion sucesiva de ....... sucede sucesivamente con la ........ del tiempo.",
"Si el caracol tuviera .... como tiene el caracol, fuera cara, fuera ... , fuera caracol con cara.",
"A Cuesta le cuesta subir la ...... , y en medio de la cuesta, va y se .......",
"Compre pocas copas, pocas ..... compre, como compre pocas copas, ..... copas pagare.",
"Toto .... te, Tita toma mate, y yo me tomo toda mi .... de chocolate.",
"En un ...... de Junqueira, juncos juntaba Julian. Juntase Juan a juntarlos y ...... juntaron mas.",
"Papa ............ y sus cinco ornitorrinquitos recorren ........ sequitos.",
"Un tubo .... un tubo y otro tubo lo detuvo  Hay tubos que tienen ..... pero este tubo no tuvo tubo.",
"Si la sierva que te sirve, no te sirve como ...... , de que sirve que te sirvas de una sierva que no ......",
"Treinta y tres ...... de troncos trozaron tres tristes .......... de troncos y triplicaron su trabajo.",
"Compadre de la capa ..... , no compre usted mas capa parda,que el que mucha .... parda compra, mucha capa parda paga.",
"De Guadalajara vengo, jara ...... , jara vendo, a medio doy cada jara. Que .... tan cara traigo de Guadalajara."]


import pilas
import pickle
import json
import random
from temporizador import Temporizador
from pilas.escena import Base

class Trabalenguas(Base):

	def __init__(self,nombre,datos):
		Base.__init__(self)
		self.nombre = nombre
		self.datos = datos

	def iniciar(self):
		self.fondo()
		self.explicacion()

	def fondo(self):
		pilas.fondos.Fondo('data/img/fondos/trabalenguas.jpg')

	def explicacion(self):
		self.titulo = pilas.actores.Actor("data/img/enunciados/trabalenguas.png",y= 200)
		self.titulo.escala = 0.5
		self.explicacion_texto = pilas.actores.Actor("data/img/interfaz/enunciado_trabalenguas.png")
		self.explicacion_texto.escala = 0.8
		pilas.mundo.agregar_tarea(7,self.mostrar)

	def mostrar(self):
		self.explicacion_texto.eliminar()
		self.indice = random.randrange(0,12)
		self.recuadro = pilas.actores.Actor("data/img/interfaz/recuadrito.png",x = -20,y = -20)
		self.recuadro.escala = 0.45
		self.texto = pilas.actores.Texto(trabalenguas[self.indice],fuente="data/fonts/American Captain.ttf",ancho = 256)
		self.texto.color = pilas.colores.negro
		pilas.mundo.agregar_tarea(10,self.seguir)

	def seguir(self):
		self.time = Temporizador(x=-300,y=300)
		self.time.setDatas(0)
		self.time.iniciar_aum()
		self.texto.eliminar()
		self.texto_nuevo = pilas.actores.Texto(problemas[self.indice],fuente="data/fonts/American Captain.ttf", ancho = 256)
		self.texto_nuevo.color = pilas.colores.negro
		self.personaje = pilas.actores.Actor("data/img/iconos/character.png",x=700)
		self.personaje.escala = 0.3
		self.personaje.x = [400]
		self.personaje.y = [-200]
		self.mostrar_incorrecto()

	def verificar(self,respuesta):
		respuestas = {
		"%s / %s"%(trabalenguas_solucion[self.indice][0],trabalenguas_solucion[self.indice][1]):"correcto",
		"%s / %s"%(trabalenguas_solucion[self.indice][0],trabalenguas_solucion[self.indice][2]):"incorrecto",
		"%s / %s"%(trabalenguas_solucion[self.indice][1],trabalenguas_solucion[self.indice][2]):"incorrecto"
		}
		if(respuestas[respuesta]== "correcto"):
			self.personaje.decir("Bien hecho , era la respuesta correcta")
			self.ener = True
		else:
			self.personaje.decir("Respuesta incorrecta , mejor suerte la proxima")
			self.ener = False
		pilas.mundo.agregar_tarea(2,self.volver)

	def mostrar_incorrecto(self):
		dialogo = pilas.actores.Dialogo()
		respuesta_correcta = "%s / %s"%(trabalenguas_solucion[self.indice][0],trabalenguas_solucion[self.indice][1])
		respuesta_incorrecta1 = "%s / %s"%(trabalenguas_solucion[self.indice][0],trabalenguas_solucion[self.indice][2])
		respuesta_incorrecta2 = "%s / %s"%(trabalenguas_solucion[self.indice][1],trabalenguas_solucion[self.indice][2])
		self.opciones = [respuesta_correcta,respuesta_incorrecta1,respuesta_incorrecta2]
		random.shuffle(self.opciones)
		dialogo.elegir(self.personaje,"Que palabras faltan?",self.opciones,self.verificar)
		pilas.mundo.agregar_tarea(2,dialogo.iniciar)

	def volver(self):
		self.time.stopTimer()
		self.datos[self.nombre]['tiempo_trabalenguas'][0] = self.datos[self.nombre]['tiempo_trabalenguas'][0] + self.time.getTime()
		self.datos[self.nombre]['tiempo_trabalenguas'][1] = self.datos[self.nombre]['tiempo_trabalenguas'][1] + 1
		if(self.ener == False):
			self.datos[self.nombre]['tiempo_trabalenguas'][2] = self.datos[self.nombre]['tiempo_trabalenguas'][2] + 1	
		f = open("data/archivos/estadisticas.json","w")
		f.write(json.dumps(self.datos))
		f.close()
		e = open("data/archivos/energia.txt",'wb')
		pickle.dump(self.ener,e)
		e.close()
		pilas.recuperar_escena()