import pilas
from carga_usuario import Usuario

pilas.iniciar(ancho = 1280, alto = 800, titulo = "Va de vuelta")
pilas.cambiar_escena(Usuario())
pilas.ejecutar()
