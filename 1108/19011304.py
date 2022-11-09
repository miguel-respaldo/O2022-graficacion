#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Luis Isael Campos Luna
# No. Control: 19011304
# Calificación: XXX
import cv2 as cv

#mouseX,mouseY = (0,0)
camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo")
    exit(1)

contador = 1
filtro = 1
before_filt = 1
lastFiltro = 1

while True:

    ret, img = camara.read()
    #img = imagen
    #cv.imshow("camara", img)
    if not ret:
        print("Mi no poder capturar la imagen de la camara")
        break

    def Lectura(num):
        cv.waitKey(num)
    
    def leyendo(val):
        return cv.waitKey(val)

    def cap(name, valor):
        return cv.imshow(name , valor)


    pause = False

    #sobel
    def sobelx(name):
        x=cv.Sobel(img,cv.CV_16S,1,0)
        absx=cv.convertScaleAbs(x)
        cap(name, absx)
        return absx
    def sobely(name):
        y=cv.Sobel(img,cv.CV_16S,0,1)
        absy=cv.convertScaleAbs(y)
        cap(name, absy)
        return absy
    #laplaciano
    def laplaciano(name):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        laplacian = cv.Laplacian(gray, cv.CV_16S, ksize=3)
        s = cv.convertScaleAbs(laplacian)
        cap(name, s)
        return s
    #blanco y negro
    def blancoynegro(name):
        gris = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cap(name, gris)
        return gris
    #canny
    def canny(name):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5, 5), 0)
        canny = cv.Canny(blur, 10, 70)
        cap(name, canny)
        return canny   
    #circulo
    def draw_circle(event,x,y,flags,param):
        global mouseX,mouseY
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img,(x,y),100,(255,0,0),-1)
            mouseX,mouseY = x,y
    #img = np.zeros((512,512,3), np.uint8)#eliminar linea?
    #cv.namedWindow("cap")
    #cv.setMouseCallback("cap",draw_circle)

    if filtro == 1:
        lastFiltro = cap("camara", img)   
    elif filtro == 2:
        lastFiltro = blancoynegro("camara")
    elif filtro == 3:
         lastFiltro = canny("camara")
    elif filtro ==4:
        lastFiltro = sobelx("camara")
    elif filtro == 5:
        lastFiltro = sobely("camara")
    elif filtro == 6:
        lastFiltro = laplaciano("camara")
    #cv.imshow("camara",img)
    teclado = leyendo(1)

    if teclado == 27:
        break

    elif teclado == ord('g') or teclado == ord('G'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imwrite(nombre,gris)
        contador += 1
    elif teclado == ord('c') or teclado == ord('C'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,img)
        contador += 1
    elif teclado == ord('1'): #a color
        before_filt = filtro
        filtro = 1
    elif teclado == ord('2'): #blanco y negro
        before_filt = filtro
        filtro = 2
    elif teclado == ord('3'): #Canny
        before_filt = filtro
        filtro = 3
    elif teclado == ord('4'): #sobelx
        before_filt = filtro
        filtro = 4
    elif teclado == ord('5'): #sobely
        before_filt = filtro
        filtro = 5
    elif teclado == ord('6'): #lapla
        before_filt = filtro
        filtro = 6
    elif teclado == ord('7'): #crear circulo
        before_filt = filtro
        filtro= 7
        while(filtro == 7):
            #img = np.zeros((512,512,3), np.uint8)
            cv.setMouseCallback("camara",draw_circle)

            cv.imshow("camara",img)
            
            k= cv.waitKey(1)
            if k == ord('r'):
                break
            elif k == ord('7'):
                filtro = before_filt
                break
        
    
camara.release()
cv.destroyAllWindows()
