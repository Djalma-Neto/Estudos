import cv2
import copy

# Abre image original
img = cv2.imread("imgca.jpg")

# Remove canal AZUL
img_no_blue = copy.copy(img)
img_no_blue[:,:,0] = 0

# Remove canal VERDE
img_no_green = copy.copy(img)
img_no_green[:,:,1] = 0

# Remove canal VERMELHO
img_no_red = copy.copy(img)
img_no_red[:,:,2] = 0

# Exibe as imagens
cv2.imshow('Imagem Original', img )
cv2.imshow('Azul Removido', img_no_blue )
cv2.imshow('Verde Removido', img_no_green )
cv2.imshow('Vermelho Removido', img_no_red )

cv2.waitKey(0)
cv2.destroyAllWindows()
