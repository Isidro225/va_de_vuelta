import pilas
import json

from pilas.escena import Base
from conf_casilleros import Casilleros
from conf_ahorcado import ConfAhorcado
from conf_tiempo import Tiempo

class Config(Base):

    def __init__(self, nombre):
        Base.__init__(self)
        self.nombre = nombre

    def fondo(self):
        pilas.fondos.Fondo("data/img/fondos/menu.jpg")

    def colores_casilleros(self):
        self.sonido_boton.reproducir()
        pilas.almacenar_escena(Casilleros(self.nombre))

    def tema_ahorcado(self):
        self.sonido_boton.reproducir()
        pilas.almacenar_escena(ConfAhorcado(self.nombre))

    def tiempo(self):
        self.sonido_boton.reproducir()
        pilas.almacenar_escena(Tiempo(self.nombre))

    def volver(self):
        self.sonido_boton.reproducir()
        pilas.recuperar_escena()
    
    def iniciar_menu(self):
        menu_titulo = pilas.actores.Texto("MENU",fuente="data/fonts/American Captain.ttf",y=120)
        menu_titulo.escala = 2
        menu_titulo.color = pilas.colores.gris
        opciones = [("Casilleros", self.colores_casilleros),("Tema del ahorcado", self.tema_ahorcado),("Tiempo de juego", self.tiempo),("Volver", self.volver)]
        menu = pilas.actores.Menu(opciones, fuente="data/fonts/American Captain.ttf",x=20,y=20)
        menu.escala = 1.4

    def iniciar(self):
        self.fondo()
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.iniciar_menu()
        #Titulo
        titulo = pilas.actores.Actor("data/img/enunciados/configuracion.png",x=15,y=280)
        titulo.escala= 0.4