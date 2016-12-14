import pilas
from pilas.escena import Base

class Credits(Base):
    
    def iniciar(self):
        self.fondo()
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.texto1()
        self.texto2()
        self.texto3()
        self.texto4()
        self.opcion()

    def fondo(self):
        pilas.fondos.Fondo("data/img/fondos/Principal.jpg")

    def texto1(self):
    	imagen = pilas.imagenes.cargar("data/img/enunciados/hecho.png")
    	hechoo= pilas.actores.Actor(imagen)
    	hechoo.y = 250
        hechoo.escala =[1.5,0.7],2

    def texto2(self):
    	imagen2 = pilas.imagenes.cargar("data/img/enunciados/isidro.png")
        isidroo= pilas.actores.Actor(imagen2)
        isidroo.y= 100
        isidroo.escala = 0.5

    def texto3(self):
    	imagen1 = pilas.imagenes.cargar("data/img/enunciados/Y.png")
        yy = pilas.actores.Actor(imagen1)
        yy.y=0
        yy.escala = 0.5

    def texto4(self):
        imagen3= pilas.imagenes.cargar("data/img/enunciados/german.png")
        germann= pilas.actores.Actor(imagen3)
        germann.y= -100
        germann.escala = 0.5

    def opcion(self):
    	menu_titulo= pilas.actores.Texto("",fuente="data/fonts/American Captain.ttf",y=50)
        opciones = [("ATRAS", self.volver)]
        menu = pilas.actores.Menu(opciones, y=-250, fuente="data/fonts/American Captain.ttf")
        menu.escala = 1.4

    def volver(self):
        self.sonido_boton.reproducir()
    	pilas.recuperar_escena()