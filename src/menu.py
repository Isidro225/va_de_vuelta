import pilas
import pickle
import sys
import json

from pilas.escena import Base
from tablero import Tablero
from musica import Sonido
from conf import Config
from creds import Credits
from ayuda import Ayuda

class Menu(Base):
    
    def __init__(self, nombre):
        Base.__init__(self)
        self.nombre = nombre

    def fondo(self):
        pilas.fondos.Fondo("data/img/fondos/menu.jpg")
    
    def iniciar_juego(self):
        self.sonido_boton.reproducir()
        self.m.detener()
        pilas.almacenar_escena(Tablero(self.nombre,self.musica))
        
    def configurar(self):
        self.sonido_boton.reproducir()
        pilas.almacenar_escena(Config(self.nombre))
        
    def creditos(self):
        self.sonido_boton.reproducir()
        pilas.almacenar_escena(Credits())

    def escena_ayuda(self):
        self.sonido_boton.reproducir()
        pilas.almacenar_escena(Ayuda())
    
    def salir(self):
        self.sonido_boton.reproducir()
        sys.exit(0)

    def iniciar_sonido(self):
        try:
            musica = open("data/archivos/musica.txt",'rb')
            est = pickle.load(musica)
            musica.close()
        except :
            est = True
            musica = open("data/archivos/musica.txt",'wb')
            pickle.dump(est,musica)
            musica.close()
        self.m = pilas.sonidos.cargar("data/audio/Medieval Rondo.ogg")
        if est:
            self.m.reproducir(repetir=True)
        self.musica = Sonido(musica=self.m, y=-220,estado=est)
    
    def iniciar_menu(self):
        menu_titulo = pilas.actores.Texto("MENU",fuente="data/fonts/American Captain.ttf",y=120)
        menu_titulo.escala = 2
        menu_titulo.color = pilas.colores.gris
        opciones = [("Jugar", self.iniciar_juego),("Configuracion", self.configurar),("Ayuda", self.escena_ayuda),("Creditos", self.creditos),("Salir", self.salir)]
        menu = pilas.actores.Menu(opciones, y=40, fuente="data/fonts/American Captain.ttf")
        menu.escala = 1.4

    def iniciar(self):
        self.fondo()
        self.iniciar_menu()
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.iniciar_sonido()
        #Titulo
        titulo = pilas.actores.Actor("data/img/enunciados/Va de vuelta.png", x=20,y=270)
        titulo.escala = [0.8,0.5],1
    