#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Gerardo Espinoza Sánchez
# No. Control: 19011271
# Calificación: XXX

import cv2 as cv
import os

mouseX, mouseY = (0,0)

camara = cv.VideoCapture(0)

directory = r'C:\Users\Gerry\Documents\Graficacion\O2022-graficacion\1108'

os.chdir(directory)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

border = True
circulo = True
color = True
contador = 1
grey = True
sobelX = True
sobelY = True
lapiciano = True

while True:

    ret, imagen = camara.read()

    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    bordesCanny = cv.Canny(imagen, 100, 200)

    x = cv.Sobel(imagen, cv.CV_16S,1,0)
    y = cv.Sobel(imagen, cv.CV_16S,0,1)

    absX = cv.convertScaleAbs(x)
    absY = cv.convertScaleAbs(y)

    dstLaplace = cv.Laplacian(gris, cv.CV_16S, ksize = 3)
    abs_dst = cv.convertScaleAbs(dstLaplace)

    def draw_circle(event, x, y, flags, param):
        global mouseX, mouseY
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img,(x,y), 200, (139,0,0), 3)
            mouseX,mouseY = x,y

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    if grey:
        cv.imshow("Camara", imagen)
        if border:
            cv.imshow("Camara", imagen)
            if sobelX:
                cv.imshow("Camara", imagen)
                if sobelY:
                    cv.imshow("Camara", imagen)
                    if lapiciano:
                        cv.imshow("Camara", imagen)
                    else:
                        cv.imshow("Camara", abs_dst)
                else:
                    cv.imshow("Camara", absY)
            else:
                cv.imshow("Camara", absX)
        else:
            cv.imshow("Camara", bordesCanny)
    else: 
        cv.imshow("Camara", gris)

    tecla = cv.waitKey(1)

    if tecla == 27:
        break
    
    elif tecla == ord('1'):
        grey = not grey
    
    elif tecla == ord('2'):
        border = not border
    
    elif tecla == ord('3'):
        sobelX = not sobelX
    
    elif tecla == ord('4'):
        sobelY = not sobelY

    elif tecla == ord('5'):
        lapiciano = not lapiciano
    
    elif tecla == ord('p') or tecla == ord('P'):
        cv.waitKey(0)
        while(tecla == ord('p') or tecla == ord('P')):
            img = imagen
            
            cv.setMouseCallback('Camara', draw_circle)
            cv.imshow('Camara',img)
            
            p = cv.waitKey(1)

            if p == ord('p') or p == ord('P'):
                circlo = not circulo
                break

    elif tecla == ord('a') or tecla == ord('A'):
        print (mouseX), mouseY
    
    elif tecla == ord('g') or tecla == ord('G'):
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)    
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen gris {nombre}")
        cv.imwrite(nombre, gris)

        print("After saving image:")  
        print(os.listdir(directory))
        
        print('Successfully saved')
        contador += 1

    elif tecla == ord('c') or tecla == ord('C'):
        cv.imshow("Camara", imagen)
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre, imagen)

        print("After saving image:")  
        print(os.listdir(directory))
        
        print('Successfully saved')
        contador += 1

camara.release()
cv.destroyAllWindows()