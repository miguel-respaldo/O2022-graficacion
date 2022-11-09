#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Solorzano Castañon Axel Ian
# No. Control: 19011294
# Calificación: XXX

import cv2 as cv

camara = cv.VideoCapture(0)
if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)
    
color=True
canny=True
sobelwithx=True
sobelwithy=True
sobelwithxy=True
laplas=True
contador = 1

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()
    #color gris
    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    
    #canny
    edge = cv.Canny(imagen, 10, 1)
    
    #sobel
    x = cv.Sobel(imagen,cv.CV_16S,1,0)  
    y = cv.Sobel(imagen,cv.CV_16S,0,1)
    absX = cv.convertScaleAbs(x)
    absY = cv.convertScaleAbs(y)
    dst = cv.addWeighted(absX,0.5,absY,0.5,0)
    
    #laplacian
    s = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    s = cv.Laplacian(s, cv.CV_16S, ksize=3)
    s = cv.convertScaleAbs(s)

    #circle
    def draw_circle(event, x, y, flags, param):
        global mouseX, mouseY
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img,(x,y), 100, (255,0,0), -1)
            mouseX,mouseY = x,y
            print(x," ",y)
    
    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    if color:
        cv.imshow("Camara", imagen)
        if canny:
            cv.imshow("Camara", imagen)
            if sobelwithx:
                cv.imshow("Camara", imagen)
                if sobelwithy:
                    cv.imshow("Camara", imagen)
                    if sobelwithxy:
                        cv.imshow("Camara", imagen)
                        if laplas:
                            cv.imshow("Camara", imagen)
                        else:
                            cv.imshow("Camara", s)
                    else:
                        cv.imshow("Camara", dst)
                else:
                    cv.imshow("Camara", absY)
            else:
                cv.imshow("Camara", absX)            
        else:
            cv.imshow("Camara", edge)
    else:
        cv.imshow("Camara", gris)
    
        
    teclado = cv.waitKey(1) 
    if teclado == 27:
        break
    elif teclado == ord('g') or teclado == ord('G') :
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
        
    elif teclado == ord('1'): 
        color = not color
        canny = True
        sobelwithx= True
        sobelwithy= True
        sobelwithxy= True
        laplas = True
    elif teclado == ord('1'):
        color=True
        canny=True
        sobelwithx= True
        sobelwithy= True
        sobelwithxy= True
        laplas = True
    elif teclado == ord('2'):
        canny = not canny
        color= True
        sobelwithx= True
        sobelwithy= True
        sobelwithxy= True 
        laplas = True   
    elif teclado == ord('2'): 
        color = True
        canny = True
        sobelwithx= True
        sobelwithy= True
        sobelwithxy= True
        laplas = True
    elif teclado == ord('3'):
        sobelwithx = not sobelwithx
        color= True
        canny= True   
        sobelwithy= True
        sobelwithxy= True
        laplas = True 
    elif teclado == ord('3'): 
        color = True
        canny = True
        sobelwithx= True 
        sobelwithy= True
        sobelwithxy= True
        laplas = True
    elif teclado == ord('4'):
        sobelwithy = not sobelwithy
        color= True
        canny= True   
        sobelwithx= True
        sobelwithxy= True 
        laplas = True
    elif teclado == ord('4'): 
        color = True
        canny = True
        sobelwithx= True 
        sobelwithy= True
        sobelwithxy= True
        laplas = True
    elif teclado == ord('5'):
        sobelwithxy = not sobelwithxy
        color= True
        canny= True   
        sobelwithy= True
        sobelwithx= True 
        laplas = True
    elif teclado == ord('5'): 
        color = True
        canny = True
        sobelwithx= True 
        sobelwithy= True
        sobelwithxy= True
        laplas = True
    elif teclado == ord('6'):
        laplas = not laplas
        color= True
        canny= True   
        sobelwithy= True
        sobelwithx= True 
    elif teclado == ord('6'): 
        color = True
        laplas = True
        canny = True
        sobelwithx= True 
        sobelwithy= True
        sobelwithxy= True
    elif teclado == ord('p') or teclado == ord('P'):
        cv.waitKey(0)
        while(teclado == ord('p') or teclado == ord('P')):
            img = imagen
            cv.setMouseCallback('Camara',draw_circle)
            cv.imshow('Camara',img)  
            p= cv.waitKey(1) 
            if(p == ord('p') or teclado == ord('P')):
                cv.imshow('Camara',imagen)
                break     
camara.release()
cv.destroyAllWindows()