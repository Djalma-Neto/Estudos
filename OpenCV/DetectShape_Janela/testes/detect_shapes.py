def imagem(tolerancia):

	import cv2
	altura = input('INFORME A ALTITUDE: ')
	if (altura == '1'):
		valor = 25.9
	elif(altura == 2):
		valor = 12.476
	elif(altura == '3'):
		valor = 8.473
	elif(altura == '4'):
		valor = 6.255
	elif(altura == '5'):
		valor = 5.018
	elif(altura == '6'):
		valor = 4.218
	else:
		print('ESSE VALOR NAO CONSTA NO REGISTRO, ALTITUDE PADRAO DEFINIDA EM: 1m')
		valor = 25.9

	img = input('INFORME A IMAGEM:  ')

	imagem = cv2.imread(img)
	imagem = cv2.GaussianBlur(imagem, (5, 5), 0)
	A = imagem.shape[0]
	L = imagem.shape[1]
	X = (10)
	Y = (10)

	(B,G,R) = imagem[X,Y]

	
	for x in range (A):
		for y in range(L):
			(b, g, r) = imagem[x, y]

			if((b<(B+tolerancia)and b>(B-tolerancia)) and (g<(G+tolerancia) and g>(G-tolerancia)) and (r<(R+tolerancia) and r>(R-tolerancia))):
				imagem[x,y] = (0,0,0)
			else: 
				pass

						
	return imagem, valor
#-----------------------------------------------------------------------------------------------------------------------------

from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2

image,valor = imagem(input('INFORME A TAXA DE VARIACAO(95): '))

resized = imutils.resize(image, width = 3264)
ratio = image.shape[0] / float(resized.shape[0])


print ("Altura (height): {} pixels").format(image.shape[0])
print ("Largura (width): {} pixels").format(image.shape[1])
print ("Canais (channels): {}").format(image.shape[2])


gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)[1]

a,cnts,b= cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

sd = ShapeDetector()


for c in cnts:
	
	M = cv2.moments(c)
	

	cX = int((M["m10"] / (M["m00"]+1)) * ratio)
	cY = int((M["m01"] / (M["m00"]+1)) * ratio)
	
	X = int((M["m10"] ))
	Y = int((M["m01"] ))
	Z = int((M["m00"] ))
	

	shape,w,h = sd.detect(c)
	area = cv2.contourArea(c)

	area = (area/valor)

	perimeter = cv2.arcLength(c,True)
	perimeter = (perimeter/valor)

	larg = (w/valor)  
	halt = (h/valor)   

	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (7, 0, 146), 2)
	image[0:75,0:155] = (255,255,255)
	cv2.putText(image, "ALTURA:"+str(round(halt,1)), (0, 15), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 150, 150), 1)
	cv2.putText(image, "LARGURA:"+str(round(larg,1)), (0,30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 150, 150), 1)
	cv2.putText(image, "AREA:"+str(round(area,1)), (0, 47), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 150, 150), 1)
	cv2.putText(image, "PERIMETRO:"+str(round(perimeter,1)), (0,65), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 150, 150), 1)


	print ("Identificacao imagem: {}").format(shape)
	print ("Area aprocimada: {} cm2").format(area)

	if(shape == 'Circulo'):
		print ("Circunferencia aprocimada: {} cm \n").format(perimeter)
	else:
		print ("perimetro aprocimado: {} cm").format(perimeter)

	print("Altura: {} cm".format(halt))
	print("Largura: {} cm".format(larg))
	cv2.imshow("Image", image)

	cv2.waitKey(0)
