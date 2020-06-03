import cv2
import numpy as np

def seguimiento(video, figuras):
    def dibujar(mask, color):
        contornos, hirarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            area = cv2.contourArea(c)
            epsilon = 0.01 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            x, y, w, h = cv2.boundingRect(approx)

            def dib():
                # cv2.putText(frame, 'Circulo', (x, y - 5), 1, 1, (0, 255, 0), 1)
                M = cv2.moments(c)
                if (M["m00"] == 0): M["m00"] = 1
                x = int(M["m10"] / M["m00"])
                y = int(M['m01'] / M['m00'])
                nuevoContorno = cv2.convexHull(c)
                cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
                cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.drawContours(frame, [nuevoContorno], 0, color, 3)

            for figura in figuras:
                if area > 5000:
                    if figura == 3:
                        if len(approx) == 3:
                            print("3333333333333")
                            dib()

                    if figura == 41:
                        if len(approx) == 4:
                            aspect_ratio = float(w) / h
                            print('aspect_ratio= ', aspect_ratio)
                            if aspect_ratio == 1:
                                dib()

                    if figura == 42:
                        if len(approx) == 4:
                            aspect_ratio = float(w) / h
                            print('aspect_ratio= ', aspect_ratio)
                            if aspect_ratio != 1:
                                dib()


                    if figura > 10:
                        if len(approx) > 10:
                            dib()



    cap = cv2.VideoCapture(video)
    salida =cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))

    colorRng = [[100, 100, 20], [125, 255, 255], [15, 100, 20], [45, 255, 255], [0, 100, 20], [5, 255, 255],
                [175, 100, 20], [179, 255, 255]]
    color = [(255, 0, 0), (0, 255, 255), (0, 0, 255)]
    # figura

    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, frame = cap.read()
        if ret == True:
            frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            cv2.imshow('frameHSV', frameHSV)
            for i in range(3):
                colorBajo = np.array(colorRng[i], np.uint8)
                colorAlto = np.array(colorRng[i + 1], np.uint8)
                maskColor = cv2.inRange(frameHSV, colorBajo, colorAlto)
                dibujar(maskColor, color[i])
            cv2.imshow('frame', frame)
            salida.write(frame)       
            
            k = cv2.waitKey(5) & 0xFF
            if k == 27 or k == ord('s'):
                break
    cap.release()
    cv2.destroyAllWindows()



