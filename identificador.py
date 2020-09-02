# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'identificador.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #en este label va la imagen de fondo
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 791, 581))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("tree.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        
        #este label tiene el titulo 
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(140, 20, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        
        #esta es la etiqueta conjunto
        self.conjunto = QtWidgets.QLabel(self.centralwidget)
        self.conjunto.setGeometry(QtCore.QRect(40, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.conjunto.setFont(font)
        self.conjunto.setObjectName("conjunto")
        
        #esta es la etiqueta relacion
        self.relacion = QtWidgets.QLabel(self.centralwidget)
        self.relacion.setGeometry(QtCore.QRect(40, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.relacion.setFont(font)
        self.relacion.setObjectName("relacion")
        
        #aqui es donde se ingresa el conjunto
        self.entrada_conjunto = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_conjunto.setGeometry(QtCore.QRect(140, 120, 411, 31))
        self.entrada_conjunto.setObjectName("entrada_conjunto")
        
        #aqui se ingresa la relacion
        self.entrada_relacion = QtWidgets.QTextEdit(self.centralwidget)
        self.entrada_relacion.setGeometry(QtCore.QRect(140, 170, 411, 101))
        self.entrada_relacion.setObjectName("entrada_relacion")
        
        #esta es la etiqueta resultado
        self.resultado = QtWidgets.QLabel(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(40, 280, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.resultado.setFont(font)
        self.resultado.setObjectName("resultado")
        
        #aqui se mostrara el resultado de que tipo de relacion es
        self.salida_relacion = QtWidgets.QLabel(self.centralwidget)
        self.salida_relacion.setGeometry(QtCore.QRect(20, 310, 151, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.salida_relacion.setFont(font)
        self.salida_relacion.setText("")
        self.salida_relacion.setObjectName("salida_relacion")
        
        #esta es la etiqueta grafo
        self.grafo = QtWidgets.QLabel(self.centralwidget)
        self.grafo.setGeometry(QtCore.QRect(290, 290, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.grafo.setFont(font)
        self.grafo.setObjectName("grafo")
        
        #aqui es donde se imprimira el grafo
        self.salida_grafo = QtWidgets.QLabel(self.centralwidget)
        self.salida_grafo.setGeometry(QtCore.QRect(270, 320, 301, 261))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.salida_grafo.setFont(font)
        self.salida_grafo.setText("")
        self.salida_grafo.setObjectName("salida_grafo")
        
        #boton iniciar
        self.iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.iniciar.setGeometry(QtCore.QRect(40, 540, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.iniciar.setFont(font)
        self.iniciar.setObjectName("iniciar")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #aqui linkeamos el boton
        self.iniciar.clicked.connect(self.relaciones)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "RELACIONES MATEMÁTICAS"))
        self.conjunto.setText(_translate("MainWindow", "Conjunto: "))
        self.relacion.setText(_translate("MainWindow", "Relación:"))
        self.resultado.setText(_translate("MainWindow", "Resultado:"))
        self.grafo.setText(_translate("MainWindow", "Grafo:"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))

    #obtener conjunto de entrada_conjunto
    #obtener relacion de entrada_relacion
    def relaciones(self):
        set = []
        cadena = self.entrada_conjunto.text()
        cadena = cadena.replace(',', '')
        #agregando cadena a lista
        
        for letra in cadena:
               set.append(letra)
               
        #conversion de la lisa de cadenas a lista de numeros
        conjunto = list(map(int, set))
        # print(cadena)   
        # print(set)
        # print(conjunto)
        
        #ahora obtenemos la entrada de la relacion
        relation = []
        
        
       
        
    
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
