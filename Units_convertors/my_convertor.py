# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'units_convertor.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(351, 235)
        MainWindow.setStyleSheet(u"background-color: rgb(31, 53, 64);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 311, 191))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 49, 16))
        self.label_2.setStyleSheet(u"font: 700 11pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.c_unit_from = QComboBox(self.groupBox)
        self.c_unit_from.addItem("")
        self.c_unit_from.addItem("")
        self.c_unit_from.addItem("")
        self.c_unit_from.addItem("")
        self.c_unit_from.setObjectName(u"c_unit_from")
        self.c_unit_from.setGeometry(QRect(10, 80, 121, 22))
        self.c_unit_from.setStyleSheet(u"background-color: rgb(168,190,201);\n"
"border-radius: 5px; ")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 60, 49, 16))
        self.label_3.setStyleSheet(u"font: 700 11pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 49, 16))
        self.label_4.setStyleSheet(u"font: 700 11pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.linE_input = QLineEdit(self.groupBox)
        self.linE_input.setObjectName(u"linE_input")
        self.linE_input.setGeometry(QRect(10, 130, 121, 21))
        self.linE_input.setStyleSheet(u"background-color: rgb(168,190,201);\n"
"border-radius: 5px; ")
        self.linE_output = QLineEdit(self.groupBox)
        self.linE_output.setObjectName(u"linE_output")
        self.linE_output.setGeometry(QRect(180, 130, 121, 21))
        self.linE_output.setStyleSheet(u"background-color: rgb(168,190,201);\n"
"\n"
"border-radius: 5px; ")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 110, 49, 16))
        self.label_5.setStyleSheet(u"font: 700 11pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(148, 130, 21, 20))
        self.label_6.setStyleSheet(u"font: 700 11pt \"Calibri\";\n"
"color: rgb(255, 255, 255);")
        self.c_unit_to = QComboBox(self.groupBox)
        self.c_unit_to.addItem("")
        self.c_unit_to.addItem("")
        self.c_unit_to.addItem("")
        self.c_unit_to.addItem("")
        self.c_unit_to.setObjectName(u"c_unit_to")
        self.c_unit_to.setGeometry(QRect(180, 80, 121, 22))
        self.c_unit_to.setStyleSheet(u"border-radius: 5px; \n"
"background-color: rgb(168,190,201);")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 291, 41))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(49, 196, 190);\n"
"border-radius: 5px; ")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 49, 16))
        self.label.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.c_units = QComboBox(self.groupBox_2)
        self.c_units.setObjectName(u"c_units")
        self.c_units.setGeometry(QRect(80, 10, 201, 22))
        self.c_units.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_calculate = QPushButton(self.groupBox)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setGeometry(QRect(230, 160, 71, 24))
        self.btn_calculate.setStyleSheet(u"background-color: rgb(242, 178, 55);\n"
"border-radius: 5px;\n"
"font: 700 11pt \"Calibri\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"from:", None))
        self.c_unit_from.setItemText(0, QCoreApplication.translate("MainWindow", u"Gram", None))
        self.c_unit_from.setItemText(1, QCoreApplication.translate("MainWindow", u"Kilogram", None))
        self.c_unit_from.setItemText(2, QCoreApplication.translate("MainWindow", u"Pound", None))
        self.c_unit_from.setItemText(3, QCoreApplication.translate("MainWindow", u"Ton", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"to:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.linE_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.linE_output.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.c_unit_to.setItemText(0, QCoreApplication.translate("MainWindow", u"Gram", None))
        self.c_unit_to.setItemText(1, QCoreApplication.translate("MainWindow", u"Kilogram", None))
        self.c_unit_to.setItemText(2, QCoreApplication.translate("MainWindow", u"Pound", None))
        self.c_unit_to.setItemText(3, QCoreApplication.translate("MainWindow", u"Ton", None))

        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.btn_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi

