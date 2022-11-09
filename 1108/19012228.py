import cv2 as cv


def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)
    



flag = True
pause = True
contador = 1
#canny = False
#laplace = False
blanco = False
negro = False
#circle = False

while True:
    
    
    # Leemos la imagen de la camara
    if pause:
        ret, imagen = camara.read()
        
  
    
    
    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    if not ret:
        print("No podemos capturar la imagen de la camara")
        break
    
   
    teclado = cv.waitKey(1)
    if teclado == 27:
        break
    elif (teclado == ord('q') or teclado == ord('Q')) and pause: #Pausar la imagen
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara',draw_circle)   
        pause = not pause
    elif (teclado == ord('q') or teclado == ord('Q')) and pause is not pause: #Pausar la imagen  
        pause = pause
    elif (teclado == ord('b') or teclado == ord('B')) and flag == True:  #Cambia bandera
        flag = False 
    elif (teclado == ord('b') or teclado == ord('B')) and flag == False:  
        flag = True
    elif (teclado == ord('p') or teclado == ord('P')) and flag == True:  # Guarda foto en color
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
    elif (teclado == ord('p') or teclado == ord('P')) and flag == False:   # Guarda foto en blanco y negro
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,gris)
        contador += 1
             
    if flag == True:                            # Bandera colo / Blanco y negro
        cv.imshow("Camara", imagen)
    elif flag == False:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)  
        cv.imshow("Camara", gris)
  

    if (teclado == ord('c') or teclado == ord('C')) and flag == True:  
        img = cv.imread("imagen-00001.png")  
        t_lower = 50  
        t_upper = 150  
        edge = cv.Canny(imagen, t_lower, t_upper)
        nombre = "imagen-{:05d}.png".format(contador+10)
        cv.imwrite(nombre,edge)
        
    if (teclado == ord('s') or teclado == ord('S')) and flag == True: 
        img = cv.imread("imagen-00002.png")  # Read image
        edge = cv.Sobel(imagen,cv.CV_64F,1,0,ksize=5)
        nombre = "imagen-{:05d}.png".format(contador+20)
        cv.imwrite(nombre,edge)
        
    if (teclado == ord('y') or teclado == ord('Y')) and flag == True: 
        img = cv.imread("imagen-00003.png")  # Read image
        edge = cv.Sobel(imagen,cv.CV_64F,0,1,ksize=5)     
        nombre = "imagen-{:05d}.png".format(contador+30)
        cv.imwrite(nombre,edge)
             
'''
    elif teclado == ord('g') or teclado == ord('G'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,gris)
        contador += 1
    elif teclado == ord('c') or teclado == ord('C'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
    '''       
     
camara.release()
cv.destroyAllWindows()



    