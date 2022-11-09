import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
en_color = True
filtro1 = False 
Gris = False
Sobelx = False
Sobely = False
Laplician = False
mouseX=0
mouseY=0
Pausar = True
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(66,41,36),2)
        mouseX,mouseY = x,y

while True:
    # Leemos la imagen de la camara
    if Pausar:
        ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    cv.imshow("Camara", imagen)
    cv.namedWindow('Camara')
    cv.setMouseCallback('Camara',draw_circle)

    if filtro1:
        edge = cv.Canny(imagen, 100, 200)
        cv.imshow('Camara', edge)
   
    if Gris:
        gris=cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow('Camara',gris)

    if Sobelx:
       sobelx = cv.Sobel(imagen,cv.CV_64F,1,0,ksize=5)  # x
       cv.imshow('Camara', sobelx)
    if Sobely:
        sobely = cv.Sobel(imagen,cv.CV_64F,0,1,ksize=5)  # y
        cv.imshow('Camara', sobely)
    if Laplician:
        laplacian = cv.Laplacian(imagen,cv.CV_64F)
        cv.imshow('Camara',laplacian)

    


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

    elif teclado == ord('b'):
        Gris = not Gris

    elif teclado == ord('1'):
        filtro1 = not filtro1
    elif teclado == ord('2'):
        Sobelx = not Sobelx
    elif teclado == ord('3'):
        Sobely = not Sobely
    elif teclado == ord('4'):
        Laplician = not Laplician
    elif teclado == ord('a'):
        print (mouseX,mouseY)
    elif teclado == ord('p'):
        Pausar = not Pausar

camara.release()
cv.destroyAllWindows()
