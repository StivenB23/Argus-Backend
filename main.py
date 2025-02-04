import cv2

imagen=cv2.imread('open.png', 0) #leer imagen, parameto 0 despues de l aimgen para trnasofrmar en escala de grises
cv2.imshow('Prueba Imagen', imagen)
cv2.imwrite('logo_gris.jpg', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()