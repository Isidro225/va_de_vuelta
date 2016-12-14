import pilas
import json

from pilas.escena import Base
from pilas.actores import Boton

class Tipo(Boton):

    def __init__(self, elemento='Animal', x=0, y=0):
        Boton.__init__(self, x=x, y=y)
        self.elemento = elemento
        self.fruta =  pilas.imagenes.cargar('data/img/iconos/fruta.png')
        self.animal = pilas.imagenes.cargar('data/img/iconos/animal.png')
        self.mes = pilas.imagenes.cargar('data/img/iconos/mes.png')
        self.instrumento = pilas.imagenes.cargar('data/img/iconos/instrumento.png')
        self.definir_tipo()

    def definir_tipo(self):
    	if(self.elemento == 'Frutas'):
    		self.imagen = self.fruta
    	elif(self.elemento == 'Animales'):
    		self.imagen = self.animal
    	elif(self.elemento == 'Meses'):
    		self.imagen = self.mes
    	elif(self.elemento == 'Instrumentos'):
    		self.imagen = self.instrumento

    def getElemento(self):
    	return self.elemento

class ConfAhorcado(Base):

	def __init__(self, nombre):
		Base.__init__(self)
		self.nombre = nombre

	def titulo(self):
		titulo = pilas.actores.Actor("data/img/enunciados/ahorcado2.png",y=250)
		titulo.escala = 0.3

	def fondo(self):
		pilas.fondos.Fondo("data/img/fondos/ahorcado.jpg")

	def volver(self):
		self.sonido_boton.reproducir()
		pilas.recuperar_escena()

	def guardar(self,seleccion):
		archivo = open('data/archivos/usuarios.json', 'w')
		self.datos[self.nombre]["tema_ahorcado"] = seleccion
		archivo.write(json.dumps(self.datos))
		archivo.close()
		pilas.avisar("Ha seleccionado la opcion: " + seleccion)
	
	def cuando_selecciona(self, x):
		self.sonido_boton.reproducir()
		self.elemento = self.lista_elemento[x]
		seleccion = self.elemento.getElemento()
 		self.guardar(seleccion)

	def generar(self):
		self.lista_elemento = []
		lista = ['Frutas','Animales','Meses','Instrumentos']
		coor = [(-110,115),(115,115),(-110,-70),(115,-70)]
		for x in range(len(lista)):
			self.elemento = Tipo(elemento=lista[x],x=coor[x][0],y=coor[x][1])
			self.elemento.escala = 0.5
			palabra = pilas.actores.Texto(lista[x],fuente="data/fonts/American Captain.ttf",x=coor[x][0],y=coor[x][1]-70)
			self.lista_elemento.append(self.elemento)
			self.elemento.activar()
			self.elemento.conectar_presionado(self.cuando_selecciona, arg=x)
		
	def iniciar(self):
		self.titulo()
		self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
		self.fondo()
		archivo = open('data/archivos/usuarios.json', 'r')
		self.datos = json.load(archivo)
		archivo.close
		self.generar()
		#Opcion para volver
		opciones = [("Volver", self.volver)]
		self.menu = pilas.actores.Menu(opciones, y=-220, fuente="data/fonts/American Captain.ttf")