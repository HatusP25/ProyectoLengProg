from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from lexer import getTokenizado
from sintactico import getSintactico


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar()

    def inicializar(self):

        self.setWindowTitle("Analizador de Ruby")
        self.setWindowIcon(QtGui.QIcon('ruby.png'))
        self.setFixedSize(900,600)
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background:rgb(245, 245, 245)")

        # Contenedor Vbox para todos los elementos
        self.contenedor = QVBoxLayout(self)
        # Label del titulo
        self.titulo = QLabel("Analizador de Ruby")
        self.titulo.setFont(QtGui.QFont("Sanserif", 18))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        # Contenedor Editor de Texto
        self.cont_Texto = QHBoxLayout(self)
        # Editor de Texto
        self.editor = QPlainTextEdit(self)
        self.editor.setPlaceholderText("Escriba aqui...")
        self.editor.setStyleSheet("border-color:black")
        self.editor.setMaximumWidth(600)
        self.editor.setMaximumHeight(300)

        # Contenedor botones
        self.cont_botones = QHBoxLayout(self)

        # Botones
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setMaximumHeight(50)
        self.botonLimpiar.clicked.connect(self.limpiar)
        self.botonLexico = QPushButton("Lexico")
        self.botonLexico.setMaximumHeight(50)
        self.botonLexico.clicked.connect(self.lexico)
        self.botonSintactico = QPushButton("Sintactico")
        self.botonSintactico.setMaximumHeight(50)
        self.botonSintactico.clicked.connect(self.sintactico)

        #Contenedor Output
        self.cont_out = QHBoxLayout(self)

        #Outputs Text

        self.textLex = QPlainTextEdit(self)
        self.textLex.setReadOnly(True)
        self.textLex.setPlaceholderText("Aqui aparecera el resultado del analizador Lexico")
        self.textSint = QPlainTextEdit(self)
        self.textSint.setReadOnly(True)
        self.textSint.setPlaceholderText("Aqui aparecera el resultado del analizador sintactico y semantico")

        # Agregando a contenedor padre
        self.contenedor.addWidget(self.titulo)
        self.cont_Texto.addWidget(self.editor)
        self.contenedor.addLayout(self.cont_Texto)
        self.cont_botones.addWidget(self.botonLexico)
        self.cont_botones.addWidget(self.botonLimpiar)
        self.cont_botones.addWidget(self.botonSintactico)
        self.contenedor.addLayout(self.cont_botones)
        self.cont_out.addWidget(self.textLex)
        self.cont_out.addWidget(self.textSint)
        self.contenedor.addLayout(self.cont_out)
        self.setLayout(self.contenedor)
        # show all the widgets
        self.show()

    #Limpiar Contenedores de Texto
    def limpiar(self):
        self.editor.clear()
        self.textLex.clear()
        self.textSint.clear()

    def lexico(self):
        self.textLex.clear()
        self.textLex.insertPlainText(getTokenizado(self.editor.toPlainText()))

    def sintactico(self):
        self.textSint.clear()
        res = getSintactico(self.editor.toPlainText())
        if  len(res) > 0:
            self.textSint.insertPlainText(res)
        else:
            self.textSint.insertPlainText("Todo Semanticamente Correcto!")
        pass

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
