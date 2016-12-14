import pilas
import json

from pilas.escena import Base

class Casilleros(Base):

    def __init__(self, nombre):
        Base.__init__(self)
        self.nombre = nombre

    def fondo(self):
        pilas.fondos.Fondo("data/img/fondos/casilleros.jpg")

    def volver(self):
        self.sonido_boton.reproducir()
        pilas.recuperar_escena()
    
    def titulos(self):
        titulo = pilas.actores.Actor("data/img/enunciados/casilleros.png",y=250)
        titulo.escala = 0.3
        normal = pilas.actores.Texto("Normales: ",fuente="data/fonts/American Captain.ttf",y=150)
        naranja = pilas.actores.Texto("Naranjas: ",fuente="data/fonts/American Captain.ttf",y=70)
        verde = pilas.actores.Texto("Verdes: ",fuente="data/fonts/American Captain.ttf",y=-10)
        violeta = pilas.actores.Texto("Violetas: ",fuente="data/fonts/American Captain.ttf",y=-90)

    def casillero_normal(self):
        self.c1= pilas.interfaz.IngresoDeTexto(y=110)
        self.c1.solo_numeros()
        self.c1.texto = str(self.datos[self.nombre]['casillero_normal'])

    def casillero_naranja(self):
        self.c2= pilas.interfaz.IngresoDeTexto(y=30)
        self.c2.solo_numeros()
        self.c2.texto = str(self.datos[self.nombre]['casillero_naranja'])

    def casillero_verde(self):
        self.c3 = pilas.interfaz.IngresoDeTexto(y=-50)
        self.c3.solo_numeros()
        self.c3.texto = str(self.datos[self.nombre]['casillero_verde'])

    def casillero_violeta(self):
        self.c4 = pilas.interfaz.IngresoDeTexto(y=-130)
        self.c4.solo_numeros()
        self.c4.texto = str(self.datos[self.nombre]['casillero_violeta'])

    def guardar(self):
        self.sonido_boton.reproducir()
        archivo = open('data/archivos/usuarios.json', 'w')
        self.datos[self.nombre]['casillero_normal'] = int(self.c1.texto)
        self.datos[self.nombre]['casillero_naranja'] = int(self.c2.texto)
        self.datos[self.nombre]['casillero_verde'] = int(self.c3.texto)
        self.datos[self.nombre]['casillero_violeta'] = int(self.c4.texto)
        archivo.write(json.dumps(self.datos))
        pilas.avisar("Los datos se guardaron exitosamente")
        archivo.close

    def verificar(self):
        max = 42
        ca1 = int(self.c1.texto)
        ca2 = int(self.c2.texto)
        ca3 = int(self.c3.texto)
        ca4 = int(self.c4.texto)
        total = ca1+ca2+ca3+ca4
        if(total > max):
            self.c1.decir("La suma de todos los casilleros no puede ser mayor a 42")
            self.c1.texto = ""
            self.c2.texto = ""
            self.c3.texto = ""
            self.c4.texto = ""
        elif(total < max):
            ca1 = ca1 + (max - total)
            self.c1.texto = str(ca1)
            self.guardar()
        else:
            self.guardar()
    
    def opcion(self):
        opciones = [("Guardar", self.verificar), ("Atras", self.volver)]
        self.menu = pilas.actores.Menu(opciones, y=-250, fuente="data/fonts/American Captain.ttf")
        self.menu.escala = 1.4
    
    def iniciar(self):
        self.fondo()
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.titulos()
        archivo = open('data/archivos/usuarios.json', 'r')
        self.datos = json.load(archivo)
        archivo.close
        self.casillero_normal()
        self.casillero_naranja()
        self.casillero_verde()
        self.casillero_violeta()
        self.opcion()