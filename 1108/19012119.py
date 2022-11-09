#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Noe Misael Antonio Figueroa
# No. Control: 19012119
# Calificación: XXX

import cv2 as cv

def dibujando(event,x,y,flags,param):
    global coordX,coordY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(0,255,0),4)
        coordX,coordY = x,y

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
t_bajo=100
t_alto=200
en_color = True
edge=False
sobelx=False
sobely=False
laplacian=False
circle=False
pause = True


while True:
    if pause:
        ret, imagen = camara.read()

    
    # Leemos la imagen de la camara
    

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break


    if en_color:
        cv.imshow("Camara",imagen)
    else:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)
    if edge:
        edge2 = cv.Canny(imagen, t_bajo, t_alto)
        cv.imshow("Camara",edge2)
    if sobelx:
        sobelX = cv.Sobel(imagen,cv.CV_64F,1,0,ksize=5)
        cv.imshow("Camara",sobelX) 
    if sobely:
        sobelY = cv.Sobel(imagen,cv.CV_64F,0,1,ksize=5)
        cv.imshow("Camara",sobelY)   
    if laplacian:
        laplace = cv.Laplacian(imagen,cv.CV_64F)
        cv.imshow("Camara",laplace)     
    if pause:
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara', dibujando)


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
    elif teclado == ord('b') or teclado == ord('B'):
        en_color = not en_color
    elif teclado == ord('1'):
        edge= not edge
    elif teclado == ord('2'):
        sobelx = not sobelx
    elif teclado == ord ('3'):
        sobely = not sobely
    elif teclado == ord('4'):
        laplacian = not laplacian
    elif teclado == ord('p') or teclado == ord('P'):
        pause = not pause
    elif teclado == ord('A') or teclado == ord('a'):
        cv.setMouseCallback('Camara',dibujando)
        print("Coord X: ", coordX)
        print("Coord Y: ",coordY)
    

camara.release()
cv.destroyAllWindows()
