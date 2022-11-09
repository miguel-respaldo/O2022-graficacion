#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Nicolas Bañuelos Hernandez
# No. Control: 19012207
# Calificación: XXX
import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        """cv.circle(imagen,(x,y),100,(255,0,0),3)"""
        cv.circle(imagen,(x,y),50,(0,0,255),3)
        mouseX,mouseY = x,y
        
"""img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)"""

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
en_color = False
canny = False
laplacian = False
sobelX = False
sobelY = False
pausa = False
video = True
list = []
mouseX = 0
mouseY = 0
while True:
    # Leemos la imagen de la camara
    if video:
        ret, imagen = camara.read()
    """ret, imagen = camara.read()"""

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    cv.imshow("Camara", imagen)

    """if video:
        cv.imshow("Camara", imagen)"""
        
    """if en_color:
        cv.imshow("Camara", imagen)
    else:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)"""

    if en_color:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)

    if canny:
        edge = cv.Canny(imagen, 100, 200, apertureSize = 3)
        cv.imshow("Camara", edge)

    if laplacian:
        lap = cv.Laplacian(imagen,cv.CV_64F)
        cv.imshow("Camara", lap)

    if sobelX:
        sobelx = cv.Sobel(imagen,cv.CV_64F,1,0,ksize=5)
        cv.imshow("Camara", sobelx)

    if sobelY:
        sobely = cv.Sobel(imagen,cv.CV_64F,0,1,ksize=5)
        cv.imshow("Camara", sobely)

    teclado = cv.waitKey(1)
    if teclado == 27:
        break
    elif teclado == ord('g') or teclado == ord('G'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imwrite(nombre,gris)
        contador += 1
    elif teclado == ord('c') or teclado == ord('C'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
    elif teclado == ord('1'):
        canny = not canny
    elif teclado == ord('2'):
        sobelX = not sobelX
    elif teclado == ord('3'):
        sobelY = not sobelY
    elif teclado == ord('4'):
        laplacian = not laplacian
    elif teclado == ord('b') or teclado == ord('B'):
        en_color = not en_color
    elif teclado == ord('p') or teclado == ord('P'):
        """pausa = not pausa"""
        """nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        list.append(nombre)
        imagen=cv.imread(list[-1])"""
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara',draw_circle)
        """cv.imshow('Camara',img)
        cv.namedWindow('image')
        cv.setMouseCallback('image',draw_circle)
        video = not video"""
        video = not video
    elif teclado == ord('a') or teclado == ord('A'):
        print (mouseX,mouseY)

camara.release()
cv.destroyAllWindows()
