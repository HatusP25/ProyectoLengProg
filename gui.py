from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtCore
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar()

    def inicializar(self):

        self.setWindowTitle("Analizador de Ruby")
        self.setGeometry(100,100,900,600)

        self.contenedor = QVBoxLayout(self)
        self.titulo = QLabel("Analizador de Ruby")
        self.titulo.setFont(QtGui.QFont("Sanserif", 18))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.contenedor.addWidget(self.titulo)

        self.setLayout(self.contenedor)
        # show all the widgets
        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
