import cv2
import numpy as np
def dibujar(mask,color):
  contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if area > 3000:
        if len(approx) > 10:
            #cv2.putText(frame, 'Circulo', (x, y - 5), 1, 1, (0, 255, 0), 1)
            M = cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x = int(M["m10"]/M["m00"])
            y = int(M['m01']/M['m00'])
            nuevoContorno = cv2.convexHull(c)
            cv2.circle(frame,(x,y),7,(0,255,0),-1)
            cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
            cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
cap = cv2.VideoCapture(0)

colorRng=[[100,100,20],[125,255,255],[15,100,20],[45,255,255],[0,100,20],[5,255,255],[175,100,20],[179,255,255]]
color =[(255,0,0),(0,255,255),(0,0,255)]

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
  ret,frame = cap.read()
  if ret == True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    for i in range(3):
        colorBajo=np.array(colorRng[i],np.uint8)
        colorAlto=np.array(colorRng[i+1],np.uint8)
        maskColor= cv2.inRange(frameHSV,colorBajo,colorAlto)
        dibujar(maskColor,color[i])
    '''
    maskAzul = cv2.inRange(frameHSV,azulBajo,azulAlto)
    maskAmarillo = cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
    maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
    maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
    maskRed = cv2.add(maskRed1,maskRed2)
    dibujar(maskAzul,(255,0,0))
    dibujar(maskAmarillo,(0,255,255))
    dibujar(maskRed,(0,0,255))'''
    cv2.imshow('frame',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()
