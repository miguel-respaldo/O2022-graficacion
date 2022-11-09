import numpy as np 
import cv2 as cv

camara = cv.VideoCapture(0)

faceClas=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)
    

contador = 1
filtro=0
negro=False
filtroEdge=False
filtroGrand=False
filtroGrandY=False
filtroGrandX=False
filtroLap=False
filtroFace=False
recorde=True
mouseX=0
mouseY=0 

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(255,0,0), 5)
        mouseX,mouseY = x,y


cv.namedWindow('Camara')
cv.setMouseCallback('Camara',draw_circle)


while True:

    if recorde:
        ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
   
    #cv.imshow("Camara", imagen)

    imagenflip = cv.flip(imagen, 1)
    
    imagenCabeza = cv.VideoCapture(-1)
    gris=cv.cvtColor(imagen, cv.COLOR_BGR2GRAY,1)

    #edge deteccion
    edge=cv.Canny(imagen,100,200)

    #sobel 
    grad_x=cv.Sobel(gris,cv.CV_64F, 1, 0, ksize=3)
    grad_y=cv.Sobel(gris,cv.CV_64F, 0, 1, ksize=3)

    abs_grand_x=cv.convertScaleAbs(grad_x)
    abs_grand_y=cv.convertScaleAbs(grad_y)

    grand=cv.addWeighted(abs_grand_x, 0.5, abs_grand_y, 0.5, 0)

    #laplace
    lap=cv.Laplacian(gris,cv.CV_64F)

    if filtro==0:
        cv.imshow("Camara",imagen)
    
    elif filtro==1:
        if(negro):
            #gris=cv.cvtColor(imagenflip, cv.COLOR_BGR2GRAY,1)
            cv.imshow("Camara",gris)
        else:
            filtro=0
    
    elif filtro==2:
        if(filtroEdge):
            cv.imshow("Camara",edge)
        else:
            filtro=0

    elif filtro==3:
        if(filtroGrand):
            cv.imshow("Camara",grand)
        else:
            filtro=0

    elif filtro==4:
        if(filtroGrandY):
            cv.imshow("Camara",abs_grand_y)
        else:
            filtro=0

    elif filtro==5:
        if(filtroGrandX):
            cv.imshow("Camara",abs_grand_x)
        else:
            filtro=0

    elif filtro==6:
        if(filtroLap):
            lap=cv.Laplacian(gris,cv.CV_64F)
            cv.imshow("Camara",lap)
        else:
            filtro=0

    elif filtro==7:
        if(filtroFace):
            faces=faceClas.detectMultiScale(gris,1.3,5)

            for (x,y,w,h) in faces:
                cv.rectangle(imagen,(x,y),(x+w,y+h),(255,0,0),2)
            
            cv.imshow("Camara",imagen)
        else:
            filtro=0
    
    tecla=cv.waitKey(1)

    if tecla == 27:
        break

    elif tecla == ord('g') or tecla == ord('G'):
        nombre="imagen-{:05d}.png".format(contador)
        contador+=1
        cv.imwrite(nombre,gris)

    elif tecla == ord('c') or tecla == ord('C'):
        nombre="imagen-{:05d}.png".format(contador)
        contador+=1
        cv.imwrite(nombre,imagenflip)

    elif tecla == ord('b'):
        filtro=1
        negro=not negro
        filtroEdge=False
        filtroGrand=False
        filtroGrandY=False
        filtroGrandX=False
        filtroLap=False
        filtroFace=False

    elif tecla == ord('1'):
        filtro=2
        filtroEdge=not filtroEdge
        negro=False
        filtroGrand=False
        filtroGrandY=False
        filtroGrandX=False
        filtroLap=False
        filtroFace=False


    elif tecla == ord('2'):
        filtro=3
        filtroGrand=not filtroGrand
        negro=False
        filtroEdge=False
        filtroGrandY=False
        filtroGrandX=False
        filtroLap=False
        filtroFace=False


    elif tecla == ord('3'):
        filtro=4
        filtroGrandY=not filtroGrandY
        negro=False
        filtroEdge=False
        filtroGrand=False
        filtroGrandX=False
        filtroLap=False
        filtroFace=False

    elif tecla == ord('4'):
        filtro=5
        filtroGrandX=not filtroGrandX
        negro=False
        filtroEdge=False
        filtroGrand=False
        filtroGrandY=False
        filtroLap=False
        filtroFace=False

    elif tecla == ord('5'):
        filtro=6
        filtroLap=not filtroLap
        negro=False
        filtroEdge=False
        filtroGrand=False
        filtroGrandY=False
        filtroGrandX=False
        filtroFace=False
    
    elif tecla== ord('p'):
        recorde=not recorde
        cv.setMouseCallback('Camara',draw_circle)

    elif tecla== ord('a'):
        print(mouseX, mouseY)

    elif tecla== ord('f'):
        filtro=7
        filtroFace=not filtroFace
        negro=False
        filtroEdge=False
        filtroGrand=False
        filtroGrandY=False
        filtroGrandX=False
        filtroLap=False



camara.release()
cv.destroyAllWindows()