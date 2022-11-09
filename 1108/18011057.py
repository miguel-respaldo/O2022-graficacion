#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Mauricio Basurto Jacobo
# No. Control: 18011057
# Calificación: XXX

import cv2 as cv
import numpy as np

camara = cv.VideoCapture(0)
contador = 1
bnw = False
canny = False
laplace = False
sobelx = False
sobely = False

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

def draw_circle(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv.EVENT_LBUTTONDOWN:
        print('x = %d, y = %d'%(x,y))
        cv.circle(imagen,(x, y), 50, (255,0,0), 3)
        cv.imshow("Camara", imagen)

global imagen

while True:
    ret, imagen = camara.read()
    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    cannyCam = cv.Canny(imagen, 100, 200)
    laplaceCam = cv.Laplacian(imagen, cv.CV_64F)
    sobelCamx = cv.Sobel(imagen, cv.CV_64F, 1, 0, ksize=5)
    sobelCamy = cv.Sobel(imagen, cv.CV_64F, 0, 1, ksize=5)

    if bnw: cv.imshow("Camara", gris)
    elif canny: cv.imshow("Camara", cannyCam)
    elif laplace: cv.imshow("Camara", laplaceCam)
    elif sobelx: cv.imshow("Camara", sobelCamx)
    elif sobely: cv.imshow("Camara", sobelCamy)
    else: cv.imshow("Camara", imagen)

    key = cv.waitKey(1) 
    if key == 27: break
    elif key == ord('g') or key == ord('G'):
        cv.imwrite('imagenCV' + str(contador) + '.jpg', gris)
        contador += 1
    elif key == ord('c') or key == ord('C'):
        cv.imwrite('imagenCV' + str(contador) + '.jpg', imagen)
        contador += 1
    elif key == ord('1'):
        canny = not canny
        laplace = False
        sobelx = False
        sobely = False
        bnw = False
    elif key == ord('2'):
        laplace = not laplace
        canny = False
        sobelx = False
        sobely = False
        bnw = False
    elif key == ord('3'):
        sobelx = not sobelx
        laplace = False
        canny = False
        sobely = False
        bnw = False
    elif key == ord('4'):
        sobely = not sobely
        laplace = False
        sobelx = False
        canny = False
        bnw = False               
    elif key == ord('b') or key == ord('B'):
        bnw = not bnw
        laplace = False
        sobelx = False
        sobely = False
        canny = False
    elif key == ord('p') or key == ord('p'):
        bnw = False
        laplace = False
        sobelx = False
        sobely = False
        canny = False
        cv.setMouseCallback("Camara", draw_circle)
        cv.waitKey()


camara.release()
cv.destroyAllWindows()