import pilas
from aplicacion import App

pilas.iniciar(ancho = 1280, alto = 800, titulo = "Aplicadion para Docente")
pilas.cambiar_escena(App())
pilas.ejecutar()