def Negativas():
	'''
	esta funcao tem a finalidade de baixar imagens negativas(que nao possui o objeto a ser identificado) e
	redimencionar salvando-as no diretorio 'negativas'
	'''
	import urllib.request
	import urllib
	import numpy as np
	import cv2
	import os

	link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
	urls_imagens_negativas = urllib.request.urlopen(link_imagens_negativas).read().decode()

	if not os.path.exists('negativas'):
		os.makedirs('negativas')

	numero_imagem = 1

	for i in urls_imagens_negativas.splitlines():
		try:

			print(i)

			urllib.request.urlretrieve(i, "negativas/"+str(numero_imagem)+".jpg")

			img = cv2.imread("negativas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)

			imagem_redimensionada = cv2.resize(img, (100,100))

			cv2.imwrite("negativas/"+str(numero_imagem)+".jpg",imagem_redimensionada)

			numero_imagem += 1

		except Exception as e:

			print(str(e))

def Positivas():
	'''
	esta funcao tem a finalidade de baixar imagens positivas(que nao possui o objeto a ser identificado) e
	redimencionar salvando-as no diretorio 'positivas'
	'''
	import urllib.request
	import urllib
	import numpy as np
	import cv2
	import os

	link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02783161'
	urls_imagens_negativas = urllib.request.urlopen(link_imagens_negativas).read().decode()

	if not os.path.exists('positivas'):
		os.makedirs('positivas')

	numero_imagem = 1

	for i in urls_imagens_negativas.splitlines():
		try:

			print(i)

			urllib.request.urlretrieve(i, "positivas/"+str(numero_imagem)+".jpg")

			img = cv2.imread("positivas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)

			imagem_redimensionada = cv2.resize(img, (100,100))

			cv2.imwrite("positivas/"+str(numero_imagem)+".jpg",imagem_redimensionada)

			numero_imagem += 1

		except Exception as e:

			print(str(e))

def Feias():
	'''
	essa funcao retira de 'negativas' as imagens feias(Com erro)
	'''
	import numpy as np
	import cv2
	import os

	igual = False

	for file_type in ['positivas']:
		for img in os.listdir(file_type):
			for feia in os.listdir('feias'):
				try:

					caminho_imagem = str(file_type)+'/'+str(img)
					feia = cv2.imread('feias/'+str(feia))
					pergunta = cv2.imread(caminho_imagem)

					if feia.shape == pergunta.shape and not(np.bitwise_xor(feia,pergunta).any()):

						print('Apagando imagem feia!')
						print(caminho_imagem)
						os.remove(caminho_imagem)

				except Exception as e:
					print(str(e))


def Listar():
	import urllib
	import numpy as np
	import cv2
	import os

	for file_type in ['negativas']:
		for img in os.listdir(file_type):
			if file_type == 'negativas':

				line = file_type+'/'+img+'\n'
				with open('bg.txt','a') as f:
					f.write(line)


			elif file_type == 'positivas':

				line = file_type+'/'+img+' 1 0 0 150 150\n'
				with open('info.dat','a') as f:
					f.write(line)

Feias()

