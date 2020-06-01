import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    #cv2.imwrite("cuadrado.jpg", frame)
    #image = cv2.imread('cuadrado.jpg',0)
    #img = cv2.imread('cuadrado.jpg',0)

    image = frame
    img = frame
    
    #Algoritmo del tablero de ajedrez
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 170, apertureSize=3)
    cv2.imshow("Bordes", edges)

    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    for x in range(0, len(lines)):
        for rho, theta in lines[x]:
            print(rho, theta)
            a=np.cos(theta)
            b=np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 2)

    cv2.imshow("Hough Lines", img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()