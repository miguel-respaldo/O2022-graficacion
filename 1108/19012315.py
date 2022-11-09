import cv2 as cv
from cv2 import imshow

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
en_color = True
canny = False
sobelx = False
sobely = False
laplace = False
mouseX = 0
mouseY = 0
pausar = True

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(0,255,0),-1)
        mouseX,mouseY = x,y

while True:
    # Leemos la imagen de la camara
    if pausar:
        ret, imagen = camara.read()
        blur = cv.GaussianBlur(imagen,(3,3),0)

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    if en_color:
        cv.imshow("Camara", imagen)
    

    else:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)

    if canny:
        bordeCanny = cv.Canny(imagen, 100, 200)
        cv.imshow("Camara", bordeCanny)

    if sobelx:
        bordeSobelx = cv.Sobel(imagen, cv.CV_64F,1,0,ksize=5)
        cv.imshow("Camara", bordeSobelx)
    
    if sobely:
        bordeSobely = cv.Sobel(imagen, cv.CV_64F,0,1,ksize=5) 
        cv.imshow("Camara", bordeSobely)
    
    if laplace:
        bordeLaplace = cv.Laplacian(blur, cv.CV_64F)
        cv.imshow("Camara", bordeLaplace)

###################################################################

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

    elif teclado == ord('s') or teclado == ord('S'):
        nombre = "imagen-{:05d}.png".format(contador)
        print(f"Guardando imagen {nombre}")
        cv.imwrite(nombre,bordeCanny)
        contador += 1

    elif teclado == ord('b') or teclado == ord('B'):
        en_color = not en_color

    elif teclado == ord('1'):
        canny = not canny

    elif teclado == ord('2'):
        sobelx = not sobelx

    elif teclado == ord('3'):
        sobely = not sobely

    elif teclado == ord('4'):
        laplace = not laplace

    elif teclado == ord('a') or teclado == ord('A'):
        print (mouseX,mouseY)

    elif teclado == ord('p') or teclado == ord('P'):
        pausar = not pausar
        cv.namedWindow('Camara')
        cv.setMouseCallback('Camara',draw_circle)


camara.release()
cv.destroyAllWindows()