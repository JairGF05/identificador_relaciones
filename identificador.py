# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'identificador.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from functions import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.entrada_relacion.setGeometry(QtCore.QRect(140, 170, 450, 101))
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
        self.salida_relacion = QtWidgets.QTextEdit(self.centralwidget)
        self.salida_relacion.setReadOnly(True)
        self.salida_relacion.setGeometry(QtCore.QRect(40, 310, 451, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.salida_relacion.setFont(font)
        self.salida_relacion.setText("")
        self.salida_relacion.setObjectName("salida_relacion")
        
        '''
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
        '''

        #boton iniciar
        self.iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.iniciar.setGeometry(QtCore.QRect(40, 540, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.iniciar.setFont(font)
        self.iniciar.setObjectName("Iniciar")

        #boton ejemplo 1
        self.ejemplo1 = QtWidgets.QPushButton(self.centralwidget)
        self.ejemplo1.setGeometry(QtCore.QRect(620, 100, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ejemplo1.setFont(font)
        self.ejemplo1.setObjectName("Ej. Orden parcial")

        #boton ejemplo 2
        self.ejemplo2 = QtWidgets.QPushButton(self.centralwidget)
        self.ejemplo2.setGeometry(QtCore.QRect(620, 135, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ejemplo2.setFont(font)
        self.ejemplo2.setObjectName("Ej. Equivalencia")

        #boton ejemplo 3
        self.ejemplo3 = QtWidgets.QPushButton(self.centralwidget)
        self.ejemplo3.setGeometry(QtCore.QRect(620, 170, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ejemplo3.setFont(font)
        self.ejemplo3.setObjectName("Ej. Neutro")
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #aqui linkeamos el boton
        self.iniciar.clicked.connect(self.relaciones)
        self.ejemplo1.clicked.connect(self.button_ejemplo1)
        self.ejemplo2.clicked.connect(self.button_ejemplo2)
        self.ejemplo3.clicked.connect(self.button_ejemplo3)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "RELACIONES MATEMÁTICAS"))
        self.conjunto.setText(_translate("MainWindow", "Conjunto: "))
        self.relacion.setText(_translate("MainWindow", "Relación:"))
        self.resultado.setText(_translate("MainWindow", "Resultado:"))
        #self.grafo.setText(_translate("MainWindow", "Grafo:"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.ejemplo1.setText(_translate("MainWindow", "Ej.Orden parcial"))
        self.ejemplo2.setText(_translate("MainWindow", "Ej.Equivalencia"))
        self.ejemplo3.setText(_translate("MainWindow", "Ej.Neutro"))

    #obtener relacion y conjunto de entrada
    def relaciones(self):
        conjuntoString = self.entrada_conjunto.text()
        relationString = self.entrada_relacion.toPlainText()
        self.analisis_relacion(conjuntoString,relationString)



    def analisis_relacion(self,conjuntoString, relationString):
        conjuntoString = conjuntoString.replace('(', '').replace(')','')
        conjunto = conjuntoString.split(',')
        if (relationString != ''):
            relation = relationString.split('),(')
            for position in range(0,len(relation)):
                subrelation = relation[position].replace('(', '').replace(')','').split(',')
                relation[position] = turnToNumberSet(subrelation)
        conjunto = turnToNumberSet(conjunto)
        #combrobar las relaciones
        orden_equivalencia = orden_o_equivalencia(conjunto,relation)
        self.salida_relacion.setText(str(comprobar_relaciones(relation,conjunto)) + str(orden_equivalencia))
        if (is_parcial_order_relation(conjunto, relation)):
            draw_hasse(relation, conjunto)

    def button_ejemplo1(self):
    # Orden parcial
        conjunto = "2,4,6,9,12,18,27,36,48,60,72"
        relacion = "(2,2),(2,4),(2,6),(2,12),(2,18),(2,36),(2,48),(2,60),(2,72),(4,4),(4,12),(4,36),(4,48),(4,60),(4,72),(6,6),(6,12),(6,18),(6,36),(6,48),(6,60),(6,72),(9,9),(9,18),(9,36),(9,72),(12,12),(12,36),(12,48),(12,60),(12,72),(18,18),(18,36),(18,72),(27,27),(36,36),(36,72),(48,48),(60,60),(72,72)"
        #conjunto = "1,2,3,5,6,10,15,30"
        #relacion = "(1,1),(1,2),(1,3),(1,5),(1,6),(1,10),(1,15),(1,30),(2,2),(2,6),(2,10),(2,30),(3,3),(3,6),(3,15),(3,30),(5,5),(5,10),(5,15),(5,30),(6,6),(6,30),(10,10),(10,30),(15,15),(15,30),(30,30)" 
        self.entrada_conjunto.setText(str(conjunto))
        self.entrada_relacion.setText(str(relacion))
        self.analisis_relacion(conjunto,relacion)

    def button_ejemplo2(self):
    # equivalencia
        conjunto ="a,b,c,d"
        relacion ="(a,a),(a,d),(d,d),(d,a),(b,b),(b,c),(c,c),(c,b)"
        self.entrada_conjunto.setText(str(conjunto))
        self.entrada_relacion.setText(str(relacion))
        self.analisis_relacion(conjunto,relacion)
 
    def button_ejemplo3(self):
    # Orden parcial
        conjunto = "0,1,2,3"
        relacion = "(1,1),(2,2),(3,3),(4,4),(6,6),(12,12),(1,2),(1,3),(1,4),(1,6),(1,12),(2,3),(2,4),(2,6),(2,12),(3,4),(3,6),(3,12),(4,6),(4,12),(6,12)"
        self.entrada_conjunto.setText(str(conjunto))
        self.entrada_relacion.setText(str(relacion))
        self.analisis_relacion(conjunto,relacion)

    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
