import cv2 as cv
import numpy as np


camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)
contador =1
en_color =True 
sobbelx =False
sobbely=False
laplacian=False
edge= False 
Canny= False 
cir=False 
t_lower = 100  # Lower Threshold
t_upper = 200  # Upper threshold
x = int 
y = int 
 




def draw_circle(event,x,y,flags,param):
    global mX, mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(255,0,0),-1)
        mX,mouseY = x,y     

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    imagenflip = cv.flip(imagen, 1)
    # 0 de cabeza
    # 1 espejo
    # -1 cabeza espejo
 

    

    if en_color:
        cv.imshow("Camara",imagen)
        
    else:
        gris=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)    
        cv.imshow("Camara", gris)
        gris= cv.cvtColor(imagenflip, cv.COLOR_RGB2GRAY)
   
    if cir: 
        """"imagen=np.zeros((480,640,3),np.uint8)"""
    cv.namedWindow('Camara')
    cv.setMouseCallback('Camara',draw_circle)
    if  edge:
     edge2 = cv.Canny(imagen, t_lower, t_upper)
     cv.imshow("Camara", edge2)
    if sobbelx:
     sob1= cv.Sobel(imagen, cv.CV_64F, 1, 0, ksize=5)
     cv.imshow("Camara", sob1) 
    if sobbely:
      sob2= cv.Sobel(imagen, cv.CV_64F, 0, 1, ksize=5) 
      cv.imshow("Camara", sob2)
    if laplacian:
      sob3= cv.Sobel(imagen,cv.CV_64F,1,1,ksize=5)     
      cv.imshow("Camara", sob3)

    teclado = cv.waitKey(1)
    if teclado == 27:
        break
    elif teclado == ord('g') or teclado == ord('G'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        gris=cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
        cv.imwrite(nombre,gris)
        contador += 1
    elif teclado== ord('c') or teclado== ord('C'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
    elif teclado==ord('b') or teclado== ord('B'):
        en_color = not en_color
    elif teclado==ord('1') or teclado==ord('!'):
        edge = not edge
    elif teclado==ord('2'):
        sobbelx= not sobbelx
    elif teclado==ord('3'):
        sobbely= not sobbely
    elif teclado==ord('4'):
        laplacian= not laplacian
    elif teclado== ord ('p') or teclado== ord('P'):
     cv.waitKey(-1)
    elif teclado== ord('a') or teclado ==ord('A'):
        cir = not cir   
        print(mX,mouseY)      
               
   

    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()