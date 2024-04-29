# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Line_break_removal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(821, 696)
        MainWindow.setStyleSheet(u"background-color: rgb(251, 243, 237);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 171, 16))
        self.label.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 40, 301, 16))
        self.r_btn_paragraph = QRadioButton(self.centralwidget)
        self.r_btn_paragraph.setObjectName(u"r_btn_paragraph")
        self.r_btn_paragraph.setGeometry(QRect(30, 70, 301, 20))
        self.r_btn_line = QRadioButton(self.centralwidget)
        self.r_btn_line.setObjectName(u"r_btn_line")
        self.r_btn_line.setGeometry(QRect(30, 90, 291, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 341, 41))
        self.btn_remove_line = QPushButton(self.centralwidget)
        self.btn_remove_line.setObjectName(u"btn_remove_line")
        self.btn_remove_line.setGeometry(QRect(30, 340, 121, 31))
        self.btn_remove_line.setStyleSheet(u"background-color: rgb(232, 96, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 1px solid black;")
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(170, 340, 51, 31))
        self.btn_reset.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 1px solid black;\n"
"background-color: rgb(172,126, 108);")
        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setGeometry(QRect(30, 620, 121, 31))
        self.btn_copy.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"font: 700 9pt \"Segoe UI\";\n"
"border: 1px solid black;\n"
"background-color: rgb(66, 119, 178);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 390, 231, 31))
        self.label_4.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 430, 401, 16))
        self.txt_input = QTextEdit(self.centralwidget)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setGeometry(QRect(30, 170, 771, 161))
        self.txt_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_result = QTextEdit(self.centralwidget)
        self.txt_result.setObjectName(u"txt_result")
        self.txt_result.setGeometry(QRect(30, 450, 771, 161))
        self.txt_result.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 821, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Choose one of these line break options.", None))
        self.r_btn_paragraph.setText(QCoreApplication.translate("MainWindow", u" Remove some line breaks (preserve paragraphs)", None))
        self.r_btn_line.setText(QCoreApplication.translate("MainWindow", u" Remove ALL line breaks", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Paste your text in the box below and then click the button.\n"
"The new text will appear in the box at the bottom of the page.", None))
        self.btn_remove_line.setText(QCoreApplication.translate("MainWindow", u"Remove Line Breaks", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"New Text without Line Breaks", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Copy your new text without line breaks from the box below.", None))
    # retranslateUi

