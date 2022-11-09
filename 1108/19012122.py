import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
en_color = True
t_lower= 100
t_upper= 100
sobelx=False
sobely=False
laplacian=False
canny=False
global mouse1
global mouseY
edge=False
def draw_circle(event,x,y,flags,param):
     if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(imagen,(x,y),100,(255,0,0),-1)
        mouse1 = x
        mouseY = y

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    if en_color: 
        cv.imshow("Camara", imagen)
    else:
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
        cv.imshow("Camara", gris)
   
    if sobelx:
     sob1= cv.Sobel(imagen, cv.CV_64F, 1, 0, ksize=5)
     cv.imshow("Camara", sob1) 
    if sobely:
      sob2= cv.Sobel(imagen, cv.CV_64F, 0, 1, ksize=5) 
      cv.imshow("Camara", sob2)
    if laplacian:
      sob3= cv.Sobel(imagen,cv.CV_64F,1,1,ksize=5)     
      cv.imshow("Camara", sob3)
    if edge:
        edge2 = cv.Canny(imagen, t_lower, t_upper)
        cv.imshow("Camara",edge2)
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
    elif teclado == ord('b') or teclado == ord('B'):
        en_color = not en_color
    elif teclado == ord('1'):
        edge = not edge
    elif teclado == ord('2'):
        sobelx = not sobelx
    elif teclado == ord('3'):
        sobely = not sobely
    elif teclado == ord('4'):
        laplacian = not laplacian
    elif teclado == ord('p'):
        cv.waitKey(-1)
    elif teclado == ord('a'):
        print(mouse1,mouseY)
    
camara.release()
cv.destroyAllWindows()
