# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'METODOSIMPLEX.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setEnabled(True)
        dialog.resize(680, 540)
        font = QtGui.QFont()
        font.setPointSize(9)
        dialog.setFont(font)
        dialog.setStyleSheet("background-color: rgb(134, 134, 134);")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.calcular = QtWidgets.QPushButton(dialog)
        self.calcular.setGeometry(QtCore.QRect(120, 500, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.calcular.setFont(font)
        self.calcular.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.calcular.setObjectName("calcular")
        self.nuevo = QtWidgets.QPushButton(dialog)
        self.nuevo.setGeometry(QtCore.QRect(220, 500, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nuevo.setFont(font)
        self.nuevo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.nuevo.setObjectName("nuevo")
        self.mostrar = QtWidgets.QPushButton(dialog)
        self.mostrar.setGeometry(QtCore.QRect(10, 500, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mostrar.setFont(font)
        self.mostrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.mostrar.setObjectName("mostrar")
        self.numRestricciones = QtWidgets.QSpinBox(dialog)
        self.numRestricciones.setGeometry(QtCore.QRect(420, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.numRestricciones.setFont(font)
        self.numRestricciones.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.numRestricciones.setObjectName("numRestricciones")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(280, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.modelo = QtWidgets.QPushButton(dialog)
        self.modelo.setGeometry(QtCore.QRect(400, 100, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.modelo.setFont(font)
        self.modelo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.modelo.setObjectName("modelo")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(290, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_8.setGeometry(QtCore.QRect(480, 230, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_funObj = QtWidgets.QLabel(dialog)
        self.label_funObj.setGeometry(QtCore.QRect(400, 260, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_funObj.setFont(font)
        self.label_funObj.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.label_funObj.setText("")
        self.label_funObj.setObjectName("label_funObj")
        self.label_varEntra = QtWidgets.QLabel(dialog)
        self.label_varEntra.setGeometry(QtCore.QRect(400, 330, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_varEntra.setFont(font)
        self.label_varEntra.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.label_varEntra.setText("")
        self.label_varEntra.setObjectName("label_varEntra")
        self.label_varSale = QtWidgets.QLabel(dialog)
        self.label_varSale.setGeometry(QtCore.QRect(400, 360, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_varSale.setFont(font)
        self.label_varSale.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.label_varSale.setText("")
        self.label_varSale.setObjectName("label_varSale")
        self.tablaRestriccion = QtWidgets.QTableWidget(dialog)
        self.tablaRestriccion.setGeometry(QtCore.QRect(490, 100, 181, 121))
        self.tablaRestriccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tablaRestriccion.setObjectName("tablaRestriccion")
        self.tablaRestriccion.setColumnCount(0)
        self.tablaRestriccion.setRowCount(0)
        self.label_iterador = QtWidgets.QLabel(dialog)
        self.label_iterador.setGeometry(QtCore.QRect(70, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_iterador.setFont(font)
        self.label_iterador.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.label_iterador.setText("")
        self.label_iterador.setObjectName("label_iterador")
        self.label_13 = QtWidgets.QLabel(dialog)
        self.label_13.setGeometry(QtCore.QRect(500, 290, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.valorZ = QtWidgets.QLabel(dialog)
        self.valorZ.setGeometry(QtCore.QRect(400, 390, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.valorZ.setFont(font)
        self.valorZ.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.valorZ.setText("")
        self.valorZ.setObjectName("valorZ")
        self.valorZ3 = QtWidgets.QLabel(dialog)
        self.valorZ3.setGeometry(QtCore.QRect(400, 420, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.valorZ3.setFont(font)
        self.valorZ3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.valorZ3.setText("")
        self.valorZ3.setObjectName("valorZ3")
        self.funObjX1 = QtWidgets.QPlainTextEdit(dialog)
        self.funObjX1.setGeometry(QtCore.QRect(140, 100, 41, 31))
        self.funObjX1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.funObjX1.setObjectName("funObjX1")
        self.funObjX2 = QtWidgets.QPlainTextEdit(dialog)
        self.funObjX2.setGeometry(QtCore.QRect(240, 100, 41, 31))
        self.funObjX2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(104, 104, 104);")
        self.funObjX2.setObjectName("funObjX2")
        self.matriz = QtWidgets.QTableWidget(dialog)
        self.matriz.setGeometry(QtCore.QRect(10, 200, 381, 281))
        self.matriz.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.matriz.setObjectName("matriz")
        self.matriz.setColumnCount(0)
        self.matriz.setRowCount(0)
        self.imprimir = QtWidgets.QPushButton(dialog)
        self.imprimir.setGeometry(QtCore.QRect(320, 500, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.imprimir.setFont(font)
        self.imprimir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.imprimir.setObjectName("imprimir")
        self.label_9 = QtWidgets.QLabel(dialog)
        self.label_9.setGeometry(QtCore.QRect(450, 510, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "METODO SIMPLEX"))
        self.label_2.setText(_translate("dialog", "Cantidad de Restricciones:"))
        self.label_3.setText(_translate("dialog", "Función Objetivo :"))
        self.label_5.setText(_translate("dialog", "Matriz :"))
        self.calcular.setText(_translate("dialog", "Siguiente"))
        self.nuevo.setText(_translate("dialog", "Nuevo"))
        self.mostrar.setText(_translate("dialog", "Mostar Datos"))
        self.label_6.setText(_translate("dialog", "METODO SIMPLEX"))
        self.modelo.setText(_translate("dialog", "Restriccione:"))
        self.label_4.setText(_translate("dialog", "  x1 + "))
        self.label_7.setText(_translate("dialog", "  x2 "))
        self.label_8.setText(_translate("dialog", "Función Objetivo:"))
        self.label_13.setText(_translate("dialog", "Resultados:"))
        self.imprimir.setText(_translate("dialog", "Imprimir "))
        self.label_9.setText(_translate("dialog", "Mendoza Paz Manuel Arturo        7 / \"A\""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())