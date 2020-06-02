import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QDialog, QFileDialog

#COMENTARIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

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
        print ("Items in the list are :")

        for count in range(self.cmbOpciones.count()):
            print (self.cmbOpciones.itemText(count))
        print ("Current index", i, "selection changed ", self.cmbOpciones.currentText())
        cambio = self.cmbOpciones.currentText()
        if cambio == "Subir un video desde el ordenador":
            self.btnVideo.setEnabled(True)
        else:
            self.btnVideo.setEnabled(False)



    def conectar(self):
        video=dialogVideo()
        video.exec()


    def buscarArchivo(self):
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
        print("textooooo")
        import Circulo


if __name__== '__main__':
    app = QApplication(sys.argv)
    GUI = dialogPrincipal()
    #GUIVideo = dialogVideo()
    GUI.show()
    #GUIVideo.show()
    sys.exit(app.exec())