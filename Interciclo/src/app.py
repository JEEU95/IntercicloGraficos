import sys

import reconocimiento
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QDialog, QFileDialog

#COMENTARIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OpVideo=0
url=''
figuras=[]
class dialogPrincipal(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Principal.ui", self)
        self.btnVideo.setEnabled(False)
        self.btnSiguiente.clicked.connect(self.conectar)
        self.btnVideo.clicked.connect(self.buscarArchivo)
        combo = self.cmbOpciones.currentText()
        print(combo)
        self.cmbOpciones.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self, i):
        global OpVideo
        print ("Items in the list are :")

        for count in range(self.cmbOpciones.count()):
            print (self.cmbOpciones.itemText(count))
        print ("Current index", i, "selection changed ", self.cmbOpciones.currentText())
        cambio = self.cmbOpciones.currentText()
        print(cambio)
        if cambio == "Subir un video desde el ordenador":
            self.btnVideo.setEnabled(True)
            OpVideo=1
        else:
            self.btnVideo.setEnabled(False)
            OpVideo=0

    def conectar(self):
        print (OpVideo)
        video=dialogVideo()
        video.exec()


    def buscarArchivo(self):
        global url
        print("buscar archivo")
        file, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo', QDir.homePath(),
                                              "All Files (*);;Text Files (*.txt)")
        if file:
            print("Archivo seleccionado: ", file)
            url = file
            self.lblRuta.setText(url)

class dialogVideo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Video.ui", self)
        self.btnPlay.clicked.connect(self.play)
        self.cbCir.stateChanged.connect(self.opciones)
        self.cbTri.stateChanged.connect(self.opciones)
        self.cbRec.stateChanged.connect(self.opciones)
        self.cbCua.stateChanged.connect(self.opciones)
        
    def opciones(self):
        global figuras
        figuras=[]
        if self.cbCir.isChecked() == True:
            print("Circulo")
            figuras.append(11)

        if self.cbTri.isChecked() == True:
            print("Triangulo")
            figuras.append(3)

        if self.cbRec.isChecked() == True:
            print("Rectangulo")
            figuras.append(41)

        if self.cbCua.isChecked() == True:
            print("Cuadrado")
            figuras.append(42)
        
        print(figuras)

    def play(self):
        if OpVideo == 0 :
            #Detectar webcam o video
            reconocimiento.capPantalla(0)
        else:
            reconocimiento.capPantalla(url)
        
        while(True):
            #repetir el bucle de trazado sobre la pantalla con cada opcion de figura activa
            for i in figuras:
                reconocimiento.trazar(i)
            
            k = cv2.waitKey(5) & 0xFF
            if k == 27 or k == ord('s'):
                break

        


if __name__== '__main__':
    app = QApplication(sys.argv)
    GUI = dialogPrincipal()
    #GUIVideo = dialogVideo()
    GUI.show()
    #GUIVideo.show()
    sys.exit(app.exec())