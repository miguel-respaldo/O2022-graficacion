import cv2 as cv

camara = cv.VideoCapture(0)

def dC(event,x,y,flags,param):
    global mX,mY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),50,(0,0,255),3)
        mX,mY = x,y

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
color = False
canny = False
laplacian = False
sobelX = False
sobelY = False
video = True
mX = 0
mY = 0

while True:
    # Leemos la imagen de la camara
    if video:
        ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    cv.imshow("Camara", imagen)

    if color:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)

    if canny:
        e = cv.Canny(imagen, 100, 200, apertureSize = 3)
        cv.imshow("Camara", e)

    if laplacian:
        lap = cv.Laplacian(imagen,cv.CV_64F)
        cv.imshow("Camara", lap)

    if sobelX:
        sobelx = cv.Sobel(imagen,cv.CV_64F,1,0,ksize=5)
        cv.imshow("Camara", sobelx)

    if sobelY:
        sobely = cv.Sobel(imagen,cv.CV_64F,0,1,ksize=5)
        cv.imshow("Camara", sobely)

    teclado = cv.waitKey(1)
    teclaG = teclado == ord('g') or teclado == ord('G')
    teclaC = teclado == ord('c') or teclado == ord('C')
    teclaB = teclado == ord('b') or teclado == ord('B')
    teclaP = teclado == ord('p') or teclado == ord('P')
    teclaA = teclado == ord('a') or teclado == ord('A')
    tecla1 = teclado == ord('1')
    tecla2 = teclado == ord('2')
    tecla3 = teclado == ord('3')
    tecla4 = teclado == ord('4')
    
    if teclado == 27:
        break
    elif teclaG:
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imwrite(nombre,gris)
        contador += 1
    elif teclaC:
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,imagen)
        contador += 1
    elif teclaB:
        color = not color
    elif teclaP:
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara',dC)
        video = not video
    elif teclaA:
        print (mX,mY)
    elif tecla1:
        canny = not canny
    elif tecla2:
        sobelX = not sobelX
    elif tecla3:
        sobelY = not sobelY
    elif tecla4:
        laplacian = not laplacian


camara.release()
cv.destroyAllWindows()