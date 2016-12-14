import pilas
import json
import sys

from pilas.escena import Base
from menu import Menu

class Usuario(Base):
    
    def __init__(self):
        Base.__init__(self)
        self.nombre = ""

    def cambiar_escena(self):
        self.sonido_boton.reproducir()
        pilas.cambiar_escena(Menu(self.nombre))
    
    def fondo(self):
        pilas.fondos.Fondo("data/img/fondos/Principal.jpg")
    
    def salir(self):
        self.sonido_boton.reproducir()
        sys.exit(0)
    
    def default(self, usuarios,estadistica):
        archivo = open('data/archivos/usuarios.json', 'w')
        usuarios[self.nombre]["status"] = True
        usuarios[self.nombre]["casillero_normal"] = 10
        usuarios[self.nombre]["casillero_violeta"] = 10
        usuarios[self.nombre]["casillero_naranja"] = 11
        usuarios[self.nombre]["casillero_verde"] = 11
        usuarios[self.nombre]["tiempo"] = 1200
        usuarios[self.nombre]["tema_ahorcado"] = "Animales"
        archivo.write(json.dumps(usuarios))
        archivo.close()
        archivo1 = open('data/archivos/estadisticas.json','w')
        estadistica[self.nombre]['tiempo'] = 0
        estadistica[self.nombre]['tiempo_adivinanza'] = [0,0,0]
        estadistica[self.nombre]['tiempo_ahorcado'] = [0,0,0]
        estadistica[self.nombre]['tiempo_trabalenguas'] = [0,0,0]
        estadistica[self.nombre]['rayos'] = 0
        archivo1.write(json.dumps(estadistica))
        archivo1.close()
        self.cambiar_escena()

    def generar_archivo(self):
        archivo = open('data/archivos/usuarios.json', 'w')
        datos = {}
        archivo.write(json.dumps(datos))
        archivo.close()
        archivo1 = open('data/archivos/estadisticas.json', 'w')
        datos1 = {}
        archivo1.write(json.dumps(datos1))
        archivo1.close()
        
    def cargar_datos(self):
        try:
            archivo = open('data/archivos/usuarios.json', 'r')
            usuarios = json.load(archivo)
            archivo.close()
            archivo1 = open('data/archivos/estadisticas.json', 'r')
            estadistica = json.load(archivo1)
            archivo1.close()
        except:
            self.generar_archivo()
            archivo = open('data/archivos/usuarios.json', 'r')
            usuarios = json.load(archivo)
            archivo.close()
            archivo1 = open('data/archivos/estadisticas.json', 'r')
            estadistica = json.load(archivo1)
            archivo1.close()
        try:
            stat = usuarios[self.nombre]["status"]
        except KeyError:
            estadistica[self.nombre] = {}
            usuarios[self.nombre] = {}
            usuarios[self.nombre]["status"] = False
            stat = usuarios[self.nombre]["status"]
        finally:
            if(stat == False):
                self.default(usuarios,estadistica)
            else:
                self.cambiar_escena()
    
    def verificar(self):
        self.nombre = str(self.box.texto)
        self.box.desactivar()
        if (len(self.nombre)<4):
            self.box.activar()
            self.box.texto = ""
            self.box.decir("Ingresa un nombre mas largo. Al menos 4 letras.")
        elif self.nombre.isdigit():
            self.box.activar()
            self.box.texto = ""
            self.box.decir("El nombre no puede contener solamente numeros.")
        else:
            self.cargar_datos()
    
    def animacion(self):
        self.texto2 = pilas.actores.Texto("Porfavor ingrese su usuario a continuacion:",fuente="data/fonts/American Captain.ttf", x=-10, y=110)
    
    def opciones(self):
        self.box.mostrar()
        opciones = [("INGRESAR", self.verificar),("SALIR", self.salir)]
        self.menu = pilas.actores.Menu(opciones, y=-100, fuente="data/fonts/American Captain.ttf")
    
    def bienvenida(self):
        self.texto = pilas.actores.Texto("Bienvenido a Va de vuelta!",fuente="data/fonts/American Captain.ttf",x=220)
        self.texto.x = [0]
        self.texto.y = [140]
        pilas.mundo.agregar_tarea(2,self.animacion)
        pilas.mundo.agregar_tarea(3,self.opciones)
        
    def iniciar(self):
        self.fondo()
        self.sonido_boton = pilas.sonidos.cargar("data/audio/boton.ogg")
        self.box = pilas.interfaz.IngresoDeTexto(ancho=200)
        self.box.ocultar()
        self.box.escala = 1.5
        self.bienvenida()