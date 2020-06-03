import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QDialog

OpVideo=0
import sys
import reconocimiento
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QDialog, QFileDialog

#COMENTARIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
OpVideo=0
url=''
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
        self.pushButton.clicked.connect(self.texto)

    def texto(self):
        if OpVideo == 0 :
            reconocimiento.seguimiento(0,11)
        else:
            print(url)
            reconocimiento.seguimiento(url,11)
        print("textooooo")
        


if __name__== '__main__':
    app = QApplication(sys.argv)
    GUI = dialogPrincipal()
    #GUIVideo = dialogVideo()
    GUI.show()
    #GUIVideo.show()
    sys.exit(app.exec())