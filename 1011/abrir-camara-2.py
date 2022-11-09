from email.mime import image
import cv2 as cv
import os as o



  

camara = cv.VideoCapture(0)

#

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)
contador = 1
while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    imagenflip = cv.flip(imagen, 1)
    gris = cv.cvtColor(imagenflip,cv.COLOR_BGR2GRAY,1)
    # 0 de cabeza
    # 1 espejo
    # -1 cabeza espejo

    # cv.imshow("Camara flip", imagenflip)
    cv.imshow("Camara", imagen)
    #cv.imshow("camara",gris)

    t =cv.waitKey(1)

    if  t == 27:
        break
    elif t == ord('g'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,gris)
        contador += 1
    elif t == ord('c'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
    elif t  == ord('b'):
        contador +=1

camara.release()
cv.destroyAllWindows()