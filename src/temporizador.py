# -*- encoding: utf-8 -*-

import pilas
from pilas.actores import Texto

class Temporizador(Texto):

	def __init__(self, x=0, y=0, color=pilas.colores.blanco, fuente="data/fonts/American Captain.ttf"):
		Texto.__init__(self, '0', x=x, y=y, fuente=fuente)
		self.gameTime = 0
		self.color = color

	def setDatas(self, gameTime):
		self.gameTime = gameTime

	def getTime(self):
		return self.time

	def stopTimer(self):
		self.myCounter.terminar()

	def continuar(self):
		self.myCounter = pilas.mundo.agregar_tarea_siempre(1, self._restCounter)

	def defineTimeText(self):
		minutes=(int(self.time / 60))
		seconds=self.time-(minutes * 60)
		secondsStr=str(seconds)
		minutesStr=str(minutes)
		if (len(str(seconds)) < 2): 
			secondsStr = '0'+secondsStr
		if (len(str(minutes)) < 2): 
			minutesStr = '0'+minutesStr
		self.texto = str(minutesStr) + ":" + str(secondsStr)

	def _aumCounter(self):
		self.time += 1
		self.defineTimeText()
		return True

	def _restCounter(self):
		if self.time != 0:
			self.time -= 1
			self.defineTimeText()
			return True

	def iniciar(self):
		self.time = self.gameTime
		self.defineTimeText()
		self.myCounter = pilas.mundo.agregar_tarea_siempre(1, self._restCounter)

	def iniciar_aum(self):
		self.time = self.gameTime
		self.defineTimeText()
		self.myCounter = pilas.mundo.agregar_tarea_siempre(1,self._aumCounter)