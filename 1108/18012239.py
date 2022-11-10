#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Jose Angel Cardona Garcia
# No. Control: 18012239
# Calificación: XXX

import numpy as np
import cv2 as cv
from turtle import circle

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
filtro = 1
visual = 1

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    
    def draw_circle(event, x, y, flags, param):
        global mouseX, mouseY
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img,(x,y), 100, (255,0,0), -1)
            mouseX,mouseY = x,y
    
    def Lectura(num):
        cv.waitKey(num)
        
    def EstadoLec(val):
        return cv.waitKey(val)
        
    def Camara(name, valor):
        return cv.imshow(name , valor)
    
    pause = False

    def Sobelx(name):
        x=cv.Sobel(imagen, cv.CV_64F,1,0 )
        absX = cv.convertScaleAbs(x)
        Camara(name, absX)
        return absX
    
    def Sobely(name):
        y=cv.Sobel(imagen, cv.CV_64F,0,1)
        absY = cv.convertScaleAbs(y)
        Camara(name, absY)
        return  absY
    
    def Laplaciano(name):
        kernel_size = 3
        ddepth = cv.CV_64F
        nimagen = cv.GaussianBlur(imagen,(3,3),0)
        gris_laplace = cv.cvtColor(nimagen, cv.COLOR_BGR2GRAY)
        dstLaplace = cv.Laplacian(gris_laplace, ddepth, ksize =kernel_size)
        abs_dst = cv.convertScaleAbs(dstLaplace)
        Camara(name, abs_dst)
        return abs_dst
        
    def gris(name):
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        Camara(name, gris)
        return gris
    
    def Canny(name):
        edge = cv.Canny(imagen, 50, 150)
        Camara(name, edge)
        return edge
    
    if filtro == 1:
        Camara("Camara", imagen)   
    elif filtro == 2:
        gris("Camara")
    elif filtro == 3:
        Canny("Camara")
    elif filtro ==4:
        Sobely("Camara")
    elif filtro == 5:
        Sobelx("Camara")
    elif filtro == 6:
        Laplaciano("Camara")

    
    teclado = EstadoLec(1)
    
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
        visual = filtro
        filtro = 1
    elif teclado == ord('2'): 
        visual = filtro
        filtro = 2
    elif teclado == ord('3'): 
        visual = filtro
        filtro = 3
    elif teclado == ord('4'): 
        visual = filtro
        filtro = 4
    elif teclado == ord('5'): 
        visual = filtro
        filtro = 5
    elif teclado == ord('6'): 
        visual = filtro
        filtro = 6
    elif teclado == ord('P') or teclado == ord('p'):
        visual = filtro
        filtro= 7
        while(filtro == 7):
            img = imagen
            cv.setMouseCallback('Camara',draw_circle)

            cv.imshow('Camara',img)
            
            k= cv.waitKey(1)
            if k == ord('r'):
                break
            elif k == ord('P') or k == ord('p'):
                filtro = visual
                break

camara.release()
cv.destroyAllWindows()