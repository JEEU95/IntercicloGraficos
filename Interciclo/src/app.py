import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

class app_GUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("Principal.ui", self)

if __name__== '__main__':
    app = QApplication(sys.argv)
    GUI = app_GUI()
    GUI.show()
    sys.exit(app.exec())