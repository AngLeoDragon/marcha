# Libraries

import cv2
from cvzone.PoseModule import PoseDetector

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Variables
cap = cv2.VideoCapture('Video.mp4')

detector = PoseDetector()
posList = []
x_list = []
y_list = []
z_list = []
datos_x = []
datos_y = []

#Funcion para crear las graficas
def make_graphics(datos_x, datos_y):
    while True:
        # Graficas
        # Creamos la figura
        fig = plt.figure()

        # Impresion de grafias en 3D
        #ax1 = fig.add_subplot(111,projection='3d')
        #ax1.scatter(x_list, y_list, z_list, c='g', marker='o')
        #ax1.scatter(x_list, y_list, z_list, c='g', marker='o')

        # Impresion de graficas en 2D
        plt.plot(datos_x, datos_y, "o")
        plt.xlabel('Distancia recorrida en el eje x')
        plt.ylabel('Movimiento en el eje y')
        plt.title('Movimiento de la cadera')
        plt.show()
        plt.savefig("mygraph.png")

def video_reader():
    while True:
        # Lectura del video por frames
        success, img = cap.read()
        img = detector.findPose(img)
        # bboxInfo nos da el dato de la cadera que se resalta
        # en el punto azul del video
        lmList, bboxInfo = detector.findPosition(img)
        #print(img)

        # Lectura de datos
        if bboxInfo:
            print(bboxInfo)
            lmString = ''
            #lmX = ''
            #lmY = ''
            #lmZ = ''
            for lm in lmList:
                lmString += f'{lm[1]},{lm[2]},{lm[3]},'
                lmX = lm[1]
                x_list.append(lmX)
                lmY = lm[2]
                y_list.append(lmY)
                lmZ = lm[3]
                z_list.append(lmZ)

            # Obtencion de datos del centro de la cadera
            for dato_x in bboxInfo:
                dato_x = bboxInfo["center"][0]
                datos_x.append(dato_x)

            for dato_y in bboxInfo:
                dato_y = bboxInfo["center"][1]
                datos_y.append(dato_y)

            # Impresion de datos en consola
            print(datos_x)
            print(len(datos_x))
            print(datos_y)
            print(len(datos_y))

            posList.append(lmString)

        else:
            False

        #print('Lista de X: ', x_list)
        #print(len(x_list))
        #print('Lista de Y: ', y_list)
        #print(len(y_list))
        #print('Lista de Z: ', z_list)
        #print(len(z_list))

        # Impresion del video en pantalla
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)

        # Orden para obtener las graficas (Tecla 's')
        if key == ord('s'):
            make_graphics(datos_x, datos_y)
            with open("AnimationFile.txt", 'w') as f:
                f.writelines(["%s\n" % item for item in posList])
        else:
            with open("AnimationFile.txt", 'w') as f:
                f.writelines(["%s\n" % item for item in posList])


    #print('Lista de X: ', x_list)
    #print(len(x_list))
    #print('Lista de Y: ', y_list)
    #print(len(y_list))
    #print('Lista de Z: ', z_list)
    #print(len(z_list))

       #cv2.imshow("Image", img)
        #cv2.waitKey(1)
        #key = cv2.waitKey(1)

        # if key == ord('s'):
        #with open("AnimationFile.txt", 'w') as f:
         #   f.writelines(["%s\n" % item for item in posList])

    # make_graphics(x_list,y_list,z_list)

video_reader()