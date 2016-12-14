import pilas
import json

from pilas.escena import Base

class Tiempo(Base):

    def __init__(self, nombre):
        Base.__init__(self)
        self.nombre = nombre

    def fondo(self):
        pilas.fondos.Fondo("data/img/fondos/Tiempo.jpg")

    def volver(self):
        self.sonido_boton.reproducir()
        pilas.recuperar_escena()
    
    def titulo(self):
        titulo = pilas.actores.Actor("data/img/enunciados/tiempo.png",y=250)
        titulo.escala = 0.3
        guia = pilas.actores.Texto("Ingrese los minutos que desea que dure su partida: ",fuente="data/fonts/American Captain.ttf",y=80)

    def ingreso_tiempo(self):
        self.box= pilas.interfaz.IngresoDeTexto(ancho=150)
        self.box.escala = 1.5
        self.box.solo_numeros()
        self.box.texto = str(self.datos[self.nombre]['tiempo']/60)

    def guardar(self):
        self.sonido_boton.reproducir()
        if(int(self.box.texto)>60):
            self.box.decir('La duracion del juego no puede ser mayor a 1 hora')
            self.box.texto = ''
        else:
            archivo = open('data/archivos/usuarios.json', 'w')
            self.datos[self.nombre]['tiempo'] = (int(self.box.texto)*60)
            archivo.write(json.dumps(self.datos))
            pilas.avisar("Los datos se guardaron exitosamente")
            archivo.close()

    def opcion(self):
        opciones = [("Guardar", self.guardar), ("Atras", self.volver)]
        self.menu = pilas.actores.Menu(opciones, y=-100, fuente="data/fonts/American Captain.ttf")
        self.menu.escala = 1.4
    
    def iniciar(self):
        self.fondo()
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.titulo()
        archivo = open('data/archivos/usuarios.json', 'r')
        self.datos = json.load(archivo)
        archivo.close
        self.ingreso_tiempo()
        self.opcion()