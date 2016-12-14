import pilas
import pickle
import random
from pilas.actores import Boton

class Sonido(Boton):

    def __init__(self, musica, x=0, y=0, estado=True ,imagen1 = "data/img/interfaz/on.png",imagen2 ="data/img/interfaz/off.png" ):
        Boton.__init__(self, x=x, y=y)
        self.on = pilas.imagenes.cargar(imagen1)
        self.on.escala = 0.5
        self.off = pilas.imagenes.cargar(imagen2)
        self.off.escala = 0.5
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.musica = musica 
        self.est = estado
        if estado:
            self.imagen = self.on
        else:
            self.apagar()
        self.conectar_presionado(self.funcion)

    def funcion (self):
        if self.est:
            self.sonido_boton.reproducir() 
            self.apagar()
        else:
            self.sonido_boton.reproducir() 
            self.encender()

    def apagar(self):
        self.imagen = self.off
        pilas.mundo.deshabilitar_sonido()
        self.musica.detener()
        self.est = False
        f = open("data/archivos/musica.txt",'wb')
        pickle.dump(self.est,f)
        f.close()

    def encender(self):
        self.imagen = self.on
        pilas.mundo.deshabilitar_sonido(False)
        self.musica.reproducir(repetir=True)
        self.est = True
        f = open("data/archivos/musica.txt",'wb')
        pickle.dump(self.est,f)
        f.close()

    def solo_detener(self):
        self.musica.detener()
        
    def ver_estado(self):
        return self.est