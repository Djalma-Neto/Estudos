def Imagem(img):
    altura = img.shape[0]
    largura = img.shape[1]
    variancia = 15
    pixel = ''
    valor = []

    for y in range(1,altura-1):
        for x in range(1,largura-1):

            cor = img[y,x]

            if(img[y,x] <= 255):

                if(img[y-1,x-1] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y-1,x] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y-1,x+1] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y,x+1] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y+1,x+1] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y+1,x] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y+1,x-1] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                if(img[y,x-1] > img[y,x]):
                    pixel += '1'
                else:
                    pixel += '0'

                valor.append(pixel)
                pixel = ''
    return 0
  

def Func(img):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Imagem, img)
        result = future.result()
        print(result)


import cv2
import _thread
import concurrent.futures

imagem = cv2.VideoCapture(0)

while True:
    conectado, imgs = imagem.read()
    img1 = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
    img = cv2.flip(img1, 180)

    _thread.start_new_thread(Func, (img,))
    
    cv2.imshow('imagem', img)

    if cv2.waitKey(1) == ord('q'):
        break
