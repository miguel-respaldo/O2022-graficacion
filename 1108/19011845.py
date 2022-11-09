#!/usr/bin/env python3
# vi: establezca shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Maria Guadalupe Garcia Baltazar
# N° Control: 19011845
# Calificación: XXX

from email.mime import image
from turtle import circle
import cv2 as cv

def dibujando(evento,x,y,flags,param):
    global mouseX,mouseY
    if evento == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
en_color = True
canny = False
laplaciano = False
sobelx = False
sobrio = False 
pausa = True

while True:
    if pausa:
        # Leemos la imagen de la camara
        ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    if en_color:
        cv.imshow("Camara", imagen)
    else:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)
    if canny:
        border = cv.Canny(imagen, 100, 200)
        cv.imshow('Camara', border)
    if laplaciano:
        laplaciano2 = cv.Laplacian (imagen,cv.CV_64F)
        cv.imshow('Camara', laplaciano2)
    if sobelx:
        sobelxx = cv.Sobel (imagen,cv.CV_64F, 1,0 , ksize=5) # x
        cv.imshow('Camara', sobelxx)
    if sobrio:
        sobrioy = cv.Sobel (imagen,cv.CV_64F,0, 1 ,ksize=5) # y
        cv.imshow('Camara', sobrioy)
    if pausa:
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara',dibujando)
       
    """if circle:
        circulo = cv.circle(imagen,(x,y),20,(255,255,255),2)
        cv.imshow('Camara', circulo)"""

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
        canny = not canny
    elif teclado == ord('2'):
        laplaciano = not laplaciano
    elif teclado == ord('3'):
        sobelx = not sobelx
    elif teclado == ord('4'):
        sobrio = not sobrio
    elif teclado == ord('p') or teclado == ord('P'):
        pausa = not pausa
    elif teclado == ord('a') or teclado == ord('A'):
        def dibujando(evento,x,y,flags,param):
            global mouseX,mouseY
            cv.circle(imagen,(x,y),100,(255,0,0),-1)
            mouseX,mouseY = x,y
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara',dibujando)
        print()
   
      
camara.release()
cv.destroyAllWindows()