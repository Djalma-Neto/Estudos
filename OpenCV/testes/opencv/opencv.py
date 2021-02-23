import cv2
imagem = cv2.VideoCapture(0)

while True:

    conectado, imgs = imagem.read()

    img1 = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)

    img = cv2.flip(img1, 180)

    altura = img.shape[0]
    largura = img.shape[1]
    variancia = 15

    for x in range(1,largura-1):
    	for y in range(1,altura-1):

    		cor = img[y,x]

    		if(img[y,x+1] > (cor+variancia) or img[y,x+1] < (cor-variancia)):
    			img[y,x] = 255


    cv2.imshow('imagem', img)

    if cv2.waitKey(1) == ord('q'):
        break


video.release()
cv2.destroyAllWindows()