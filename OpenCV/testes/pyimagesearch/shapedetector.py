class ShapeDetector:

	def detect(self, c):
		
		import cv2  

		forma = "Indistinguivel"

		perimetro = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.032 * perimetro, True)
		x, y, w, h = cv2.boundingRect(c)
		


		if len(approx) == 3:
			forma = "Triangulo"

		elif len(approx) == 4:
		    forma = "Quadrado" if (w >= h-20) and (w <= h+20) else "Retangulo"

		elif len(approx) == 5:
		    forma = "Pentagono"

		elif len(approx) == 6:
		    forma = "Hexagono"

		else:
			forma = "Circulo"

		

		return forma,w,h