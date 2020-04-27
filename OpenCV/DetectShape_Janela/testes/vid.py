from Func import func
import cv2
import numpy as np
from threading import Thread

img = cv2.VideoCapture(0)

#------------------------------------------------------------------------------------------
while True:

    conectado, imagem = img.read()
    imagem = cv2.flip(imagem, 180)

    largura = 300
    altura = 200
    imagem = cv2.resize(imagem, (largura,altura), interpolation = cv2.INTER_AREA)

    array = np.array(imagem)

    A = imagem.shape[0]
    L = imagem.shape[1]
#-------------------------------------------------------------------------------------------
    meioL = int(L/2)
    meioA = int(A/2)
    imagem[0:A,meioL:(meioL+1)] = (0,0,255)
    imagem[meioA:(meioA+1),0:L] = (0,0,255)

#-------------------------------------------------------------------------------------------

    ES = np.array(array[0:meioA,0:meioL])
    EI = np.array(array[meioA:A,0:meioL])

    DS = np.array(array[0:meioA,meioL:L])
    DI = np.array(array[meioA:A,meioL:L])

    ES = func.Detecta1(ES)
    EI = func.Detecta1(EI)
    DS = func.Detecta1(DS)
    DI = func.Detecta1(DI)


    if(ES == True):
        imagem[0:10,0:10] = (0,255,0)
    else:
        imagem[0:10,0:10] = (0,0,255)

    if(EI == True):
        imagem[(A - 10):A,0:10] = (0,255,0)
    else:
        imagem[(A - 10):A,0:10] = (0,0,255)

    if(DS == True):
        imagem[0:10,(L-10):L] = (0,255,0)
    else:
        imagem[0:10,(L-10):L] = (0,0,255)
        
    if(DI == True):
        imagem[(A- 10):A,(L-10):L] = (0,255,0)
    else:
        imagem[(A- 10):A,(L-10):L] = (0,0,255)

#-------------------------------------------------------------------------------------------
    cv2.imshow('imagem', imagem)

    if cv2.waitKey(1) == ord('q'):
        break
        
#-------------------------------------------------------------------------------------------
















