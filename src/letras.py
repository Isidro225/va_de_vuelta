import pilas
from pilas.actores import Boton

class Letra(Boton):

    def __init__(self, letra='A', x=0, y=0):
        Boton.__init__(self, x=x, y=y)
        self.letra = letra
        self.a =  pilas.imagenes.cargar('data/img/letras/a.png')
        self.b =  pilas.imagenes.cargar('data/img/letras/b.png')
        self.c =  pilas.imagenes.cargar('data/img/letras/c.png')
        self.d =  pilas.imagenes.cargar('data/img/letras/d.png')
        self.e =  pilas.imagenes.cargar('data/img/letras/e.png')
        self.f =  pilas.imagenes.cargar('data/img/letras/f.png')
        self.g =  pilas.imagenes.cargar('data/img/letras/g.png')
        self.h =  pilas.imagenes.cargar('data/img/letras/h.png')
        self.i =  pilas.imagenes.cargar('data/img/letras/i.png')
        self.j =  pilas.imagenes.cargar('data/img/letras/j.png')
        self.k =  pilas.imagenes.cargar('data/img/letras/k.png')
        self.l =  pilas.imagenes.cargar('data/img/letras/l.png')
        self.m =  pilas.imagenes.cargar('data/img/letras/m.png')
        self.n =  pilas.imagenes.cargar('data/img/letras/n.png')
        self.o =  pilas.imagenes.cargar('data/img/letras/o.png')
        self.p =  pilas.imagenes.cargar('data/img/letras/p.png')
        self.q =  pilas.imagenes.cargar('data/img/letras/q.png')
        self.r =  pilas.imagenes.cargar('data/img/letras/r.png')
        self.s =  pilas.imagenes.cargar('data/img/letras/s.png')
        self.t =  pilas.imagenes.cargar('data/img/letras/t.png')
        self.u =  pilas.imagenes.cargar('data/img/letras/u.png')
        self.v =  pilas.imagenes.cargar('data/img/letras/v.png')
        self.w =  pilas.imagenes.cargar('data/img/letras/w.png')
        self.xx =  pilas.imagenes.cargar('data/img/letras/x.png')
        self.yy =  pilas.imagenes.cargar('data/img/letras/y.png')
        self.zz =  pilas.imagenes.cargar('data/img/letras/z.png')
        self.definir_letra()

    def definir_letra(self):
    	if(self.letra == 'A'):
    	   self.imagen = self.a
    	elif(self.letra == 'B'):
    	   self.imagen = self.b
    	elif(self.letra == 'C'):
    	   self.imagen = self.c
    	elif(self.letra == 'D'):
    	   self.imagen = self.d
    	elif(self.letra == 'E'):
    	   self.imagen = self.e
    	elif(self.letra == 'F'):
    	   self.imagen = self.f
    	elif(self.letra == 'G'):
    	   self.imagen = self.g
    	elif(self.letra == 'H'):
    	   self.imagen = self.h
    	elif(self.letra == 'I'):
    	   self.imagen = self.i
    	elif(self.letra == 'J'):
    	   self.imagen = self.j
    	elif(self.letra == 'K'):
    	   self.imagen = self.k
    	elif(self.letra == 'L'):
    	   self.imagen = self.l
    	elif(self.letra == 'M'):
    	   self.imagen = self.m
    	elif(self.letra == 'N'):
    	   self.imagen = self.n
    	elif(self.letra == 'O'):
    	   self.imagen = self.o
    	elif(self.letra == 'P'):
    	   self.imagen = self.p
    	elif(self.letra == 'Q'):
    	   self.imagen = self.q
    	elif(self.letra == 'R'):
    	   self.imagen = self.r
    	elif(self.letra == 'S'):
    	   self.imagen = self.s
    	elif(self.letra == 'T'):
    	   self.imagen = self.t
    	elif(self.letra == 'U'):
    	   self.imagen = self.u
    	elif(self.letra == 'V'):
    	   self.imagen = self.v
    	elif(self.letra == 'W'):
    	   self.imagen = self.w
    	elif(self.letra == 'X'):
    	   self.imagen = self.xx
    	elif(self.letra == 'Y'):
    	   self.imagen = self.yy
    	elif(self.letra == 'Z'):
    	   self.imagen = self.zz

    def getLetra(self):
    	return self.letra