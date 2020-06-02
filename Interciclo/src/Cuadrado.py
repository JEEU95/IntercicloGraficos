import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    cv2.imwrite("original.jpg", frame)
    image= cv2.imread('original.jpg')
    
    img = cv2.imread('original.jpg')
    
    cv2.imshow('Original',image)

    edges = cv2.Canny(image, 100, 100)
    
    cv2.imshow('Bordes', edges)

    contours,_= cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        cv2.drawContours(img,[cnt],0,(0,255,0),3)
    
    cv2.imshow("Deteccion", img)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()