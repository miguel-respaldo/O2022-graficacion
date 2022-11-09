import numpy as np
import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
filtro = 1
before_filt = 1
lastFiltro = 1

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    
    def Lectura(num):
        cv.waitKey(num)
        
    def EstadoLec(val):
        return cv.waitKey(val)
        
    def Camara(name, valor):
        return cv.imshow(name , valor)
    
    pause = False
    
    #sin_filtro = cv.flip(imagen,2)

    
    #variables de sobel
    def SobelX(name):
        x=cv.Sobel(imagen, cv.CV_16S,1,0)
        absX = cv.convertScaleAbs(x)
        #dst = cv.addWeighted (absX,1, absY, 0.5,0)
        Camara(name, absX)
        return absX
    
    def SobelY(name):
        y=cv.Sobel(imagen, cv.CV_16S,0,1)
        absY = cv.convertScaleAbs(y)
        #dst = cv.addWeighted (absX,1, absY, 0.5,0)
        Camara(name, absY)
        return  absY
    
    #variables laplaciano
    def Laplaciano(name):
        kernel_size = 3
        ddepth = cv.CV_16S
        nimagen = cv.GaussianBlur(imagen,(3,3),0)
        gris_laplace = cv.cvtColor(nimagen, cv.COLOR_BGR2GRAY)
        dstLaplace = cv.Laplacian(gris_laplace, ddepth, ksize =kernel_size)
        abs_dst = cv.convertScaleAbs(dstLaplace)
        Camara(name, abs_dst)
        return abs_dst
        
    def BlackAndWhite(name):
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        Camara(name, gris)
        return gris
    
    def Canny(name):
        edge = cv.Canny(imagen, 50, 150)
        Camara(name, edge)
        return edge

    
    #circle en python
    def draw_circle(event, x, y, flags, param):
        global mouseX, mouseY
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(img,(x,y), 100, (255,0,0), -1)
            mouseX,mouseY = x,y
            
    
            

     
    if filtro == 1:
        lastFiltro = Camara("Camara", imagen)   
    elif filtro == 2:
        lastFiltro = BlackAndWhite("Camara")
    elif filtro == 3:
         lastFiltro = Canny("Camara")
    elif filtro ==4:
        lastFiltro = SobelY("Camara")
    elif filtro == 5:
        lastFiltro = SobelX("Camara")
    elif filtro == 6:
        lastFiltro = Laplaciano("Camara")

    
    teclado = EstadoLec(1)
    
    if teclado == 27:
        break
    
    elif teclado == ord('g') or teclado == ord('G'): #Captura de la camara en blanco y negro
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imwrite(nombre,gris)
        contador += 1
        
    elif teclado == ord('c') or teclado == ord('C'): #captura de la camara
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
        
    elif teclado == ord('1'): #Sin filtro
        before_filt = filtro
        filtro = 1
    elif teclado == ord('2'): #Blanco o negro
        before_filt = filtro
        filtro = 2
    elif teclado == ord('3'): #Canny
        before_filt = filtro
        filtro = 3
    elif teclado == ord('4'): #Sobel X
        before_filt = filtro
        filtro = 4
    elif teclado == ord('5'): #Sobel Y
        before_filt = filtro
        filtro = 5
    elif teclado == ord('6'): #Laplaciano
        before_filt = filtro
        filtro = 6
    elif teclado == ord('P') or teclado == ord('p'): #Circulo
        before_filt = filtro
        filtro= 7
        while(filtro == 7):
            img = imagen
            #img = np.zeros((512,512,3), np.uint8)
            cv.setMouseCallback('Camara',draw_circle)

            cv.imshow('Camara',img)
            
            k= cv.waitKey(1)
            if k == ord('r'):
                break
            elif k == ord('P') or k == ord('p'):
                filtro = before_filt
                break
        
    
camara.release()
cv.destroyAllWindows()
