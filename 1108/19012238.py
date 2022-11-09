#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Enrique Irazoqui Ruelas
# No. Control: 19012238
# Calificación: XXX

from email.mime import image
from multiprocessing.connection import wait
from pickle import FALSE
from signal import pause
import numpy as np 
import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)
    

contador = 1
en_color = False
filtro1 = False
filtro2 = False
filtro3 = False
filtro4 = False
pausar = True
mouseX=0
mouseY=0 

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(255,0,0), 5)
        mouseX,mouseY = x,y
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(imagen,(x,y),100,(0,0,255), 5)
        mouseX,mouseY = x,y

def onMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
       # draw circle here (etc...)
       print('x = %d, y = %d'%(x, y))


def on_click(event, x, y, p1, p2):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(imagen, (x, y), 3, (255, 0, 0), -1)


    
    

#P dejar de capturar imagenes
#A codigo de stack overflow con codigo a para mostrar coordenadas

cv.namedWindow('Camara')
cv.setMouseCallback('Camara',draw_circle)
aux = 0
while True:
# Leemos la imagen de la camara

    if pausar:
        ret, imagen = camara.read()
        #aux += 1
        #print(aux)

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    
    cv.imshow("Camara", imagen)
    
    if en_color:
        #cv.imshow("Camara", imagen)
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)
    #else:
        #gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        #cv.imshow("Camara", gris)

    if filtro1:
        canny = cv.Canny(imagen, 100, 200)
        cv.imshow("Camara", canny)

    if filtro2:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        laplacian = cv.Laplacian(gris,cv.CV_64F)
        cv.imshow("Camara", laplacian)

    if filtro3:
        x = cv.Sobel(imagen,cv.CV_16S,1,0) 
        absX = cv.convertScaleAbs(x)
        cv.imshow("Camara", absX)

    if filtro4:
        y = cv.Sobel(imagen,cv.CV_16S,0,1)
        absY = cv.convertScaleAbs(y)
        cv.imshow("Camara", absY)
    
        
    
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
        filtro1 = not filtro1
    elif teclado == ord('2'):
        filtro2 = not filtro2
    elif teclado == ord('3'):
        filtro3 = not filtro3
    elif teclado == ord('4'):
        filtro4 = not filtro4
    elif teclado == ord('p') or teclado == ord('P'):
        pausar = not pausar
        cv.setMouseCallback('Camara',draw_circle)
        #cv.waitKey(0)
    elif teclado == ord('a')or teclado == ord('A'):
        print (mouseX , mouseY)



camara.release()
cv.destroyAllWindows()
