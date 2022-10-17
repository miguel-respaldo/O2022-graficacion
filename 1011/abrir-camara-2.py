import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print("No puedo abrir la camara")
    exit(1)

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

    cv.imshow("Camara flip", imagenflip)
    cv.imshow("Camara", imagen)


    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()