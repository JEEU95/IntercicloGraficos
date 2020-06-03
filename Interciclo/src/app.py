import sys
import reconocimiento
import img.Seleccion_rc
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QDialog, QFileDialog

OpVideo=0
url=''
figuras=[]


class dialogPrincipal(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Principal.ui", self)
        self.btnVideo.setEnabled(False)
        self.btnVideo.setVisible(False)
        self.lblRuta.setVisible(False)
        self.lblWebCam.setVisible(True)
        self.lblVideo.setVisible(False)
        self.btnSiguiente.clicked.connect(self.conectar)
        self.btnSalir.clicked.connect(self.Salir)
        self.btnVideo.clicked.connect(self.buscarArchivo)
        combo = self.cmbOpciones.currentText()
        print(combo)
        self.cmbOpciones.currentIndexChanged.connect(self.selectionchange)
    def Salir(self):
        sys.exit(0)
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
            self.btnVideo.setVisible(True)
            self.btnSiguiente.setEnabled(False)
            self.lblWebCam.setVisible(False)
            self.lblVideo.setVisible(True)
            OpVideo=1
        else:
            self.btnVideo.setEnabled(False)
            self.btnVideo.setVisible(False)
            self.btnSiguiente.setEnabled(True)
            self.lblRuta.setVisible(False)
            self.lblWebCam.setVisible(True)
            self.lblVideo.setVisible(False)
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
            self.lblRuta.setVisible(True)
            self.lblRuta.setText(url)
            self.btnSiguiente.setEnabled(True)

class dialogVideo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Video.ui", self)
        self.btnSalir.clicked.connect(self.Salir)
        self.btnPlay.clicked.connect(self.play)
        self.btnAtras.clicked.connect(self.conectar)
        self.cbCir.stateChanged.connect(self.opciones)
        self.cbTri.stateChanged.connect(self.opciones)
        self.cbRec.stateChanged.connect(self.opciones)
        self.cbCua.stateChanged.connect(self.opciones)
        self.lblError.setVisible(False)
    def conectar(self):
        print (OpVideo)
        video=dialogPrincipal()
        video.exec()
    def opciones(self):
        global figuras
        figuras=[]
        if self.cbCir.isChecked() == True:
            print("Circulo")
            figuras.append(10)

        if self.cbTri.isChecked() == True:
            print("Triangulo")
            figuras.append(3)

        if self.cbRec.isChecked() == True:
            print("Rectangulo")
            figuras.append(42)

        if self.cbCua.isChecked() == True:
            print("Cuadrado")
            figuras.append(41)
        
        print(figuras)
    
    def Salir(self):
        sys.exit(0)

    def play(self):
        if figuras ==[]:
            self.lblError.setVisible(True)
        else:
            self.lblError.setVisible(False)
            if OpVideo == 0 :
                reconocimiento.seguimiento(0,figuras)
            else:
                print(url)
                reconocimiento.seguimiento(url,figuras)

if __name__== '__main__':
    app = QApplication(sys.argv)
    GUI = dialogPrincipal()
    #GUIVideo = dialogVideo()
    GUI.show()
    #GUIVideo.show()
    sys.exit(app.exec())