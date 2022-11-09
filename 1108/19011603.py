

#Norika Isabel Ramirez Valdez 
# Graficación


import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

contador = 1
color = True
sobelX = True
sobelY = True
canny = True 

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

     #canny
    edge = cv.Canny(imagen, 10, 1)

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    cv.imshow("Camara", imagen)

    gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)

    sobelx = cv.Sobel(imagen, cv.CV_16S, 1, 0) 
    sobely = cv.Sobel(imagen, cv.CV_16S, 0, 1)

    absx = cv.convertScaleAbs(sobelx)
    absy = cv.convertScaleAbs(sobely)

    if color:
        cv.imshow("Camara", imagen)
        if sobelX:
            cv.imshow("Camara", imagen)
            if sobelY: 
                cv.imshow("Camara", imagen)
            else:
                cv.imshow("Camara", absx)
        else:
            cv.imshow("Camara", absy)
    else:
        cv.imshow("Camara", gris)

        teclado = cv.waitKey(1)
        if teclado == 27:
          break
    
        elif teclado == ord('g') or teclado == ord('G'):
            nombre = "imagen-{:05d}.png".format(contador)
            print(f"Guardando imagen {nombre}")
            cv.imwrite(nombre,imagen)
            img_grey = cv.imread(nombre, cv.IMREAD_GRAYSCALE)
            img_binary = cv.threshold(img_grey, 100, 255, cv.THRESH_BINARY)[1]
            cv.imwrite(nombre,img_binary)
            contador += 1

        elif teclado == ord('c') or teclado == ord('C'):
            nombre = "imagen-{:05d}.png".format(contador)
            print(f"Guardando imagen {nombre}")      
            cv.imwrite(nombre,imagen)
            contador += 1 

        elif teclado == ord('b') or teclado == ord('B'):
            color = not color
        elif teclado == ord('b') or teclado == ord('B'):    
            color = True
        elif teclado == ord('1'):
            sobelX = not sobelX
        elif teclado == ord('1'):    
            sobelX = True
        elif teclado == ord('2'):
            sobelY = not sobelY
        elif teclado == ord('2'):    
            sobelY = True 

camara.release()
cv.destroyAllWindows()
