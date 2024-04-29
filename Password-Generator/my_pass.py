# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pass-generator.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(414, 444)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 91, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(u"pics/unnamed.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 381, 20))
        self.label_2.setStyleSheet(u"font: 700 18pt \"Calibri\";\n"
"qproperty-alignment: AlignCenter;")
        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setGeometry(QRect(340, 160, 41, 31))
        self.btn_copy.setStyleSheet(u"\n"
"border-radius: 10px; \n"
"\n"
"border: 1px solid black;\n"
"")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 150, 361, 51))
        self.lineEdit.setStyleSheet(u"\n"
"border-radius: 10px; \n"
"\n"
"font: 700 16pt \"Consolas\";\n"
"font-weight: bold; \n"
"color: black; \n"
"border: 1px solid black;\n"
"")
        self.h_Slider = QSlider(self.centralwidget)
        self.h_Slider.setObjectName(u"h_Slider")
        self.h_Slider.setGeometry(QRect(50, 220, 321, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.h_Slider.sizePolicy().hasHeightForWidth())
        self.h_Slider.setSizePolicy(sizePolicy1)
        self.h_Slider.setMinimumSize(QSize(0, 0))
        self.h_Slider.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 300, 371, 131))
        self.chB_upper = QCheckBox(self.groupBox)
        self.chB_upper.setObjectName(u"chB_upper")
        self.chB_upper.setGeometry(QRect(20, 14, 331, 20))
        self.chB_upper.setLayoutDirection(Qt.RightToLeft)
        self.chB_upper.setStyleSheet(u"font: 700 12pt \"Calibri\";\n"
"\n"
"")
        self.chB_nums = QCheckBox(self.groupBox)
        self.chB_nums.setObjectName(u"chB_nums")
        self.chB_nums.setGeometry(QRect(20, 66, 331, 20))
        self.chB_nums.setLayoutDirection(Qt.RightToLeft)
        self.chB_nums.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.chB_chr = QCheckBox(self.groupBox)
        self.chB_chr.setObjectName(u"chB_chr")
        self.chB_chr.setGeometry(QRect(20, 92, 331, 20))
        self.chB_chr.setLayoutDirection(Qt.RightToLeft)
        self.chB_chr.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.chB_lower = QCheckBox(self.groupBox)
        self.chB_lower.setObjectName(u"chB_lower")
        self.chB_lower.setGeometry(QRect(20, 40, 331, 20))
        self.chB_lower.setLayoutDirection(Qt.RightToLeft)
        self.chB_lower.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 250, 111, 31))
        self.label_3.setStyleSheet(u"\n"
"font: 11pt \"Calibri\";")
        self.lbl_length = QLabel(self.centralwidget)
        self.lbl_length.setObjectName(u"lbl_length")
        self.lbl_length.setGeometry(QRect(140, 250, 49, 31))
        self.lbl_length.setStyleSheet(u"\n"
"font: 11pt \"Calibri\";")
        self.lbl_msg = QLabel(self.centralwidget)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setGeometry(QRect(160, 250, 241, 31))
        self.lbl_msg.setStyleSheet(u"qproperty-alignment: AlignCenter;\n"
"color: rgb(255, 0, 0);\n"
"font: 11pt \"Calibri\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btn_copy.raise_()
        self.h_Slider.raise_()
        self.groupBox.raise_()
        self.label_3.raise_()
        self.lbl_length.raise_()
        self.lbl_msg.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PASSWORD GENERATOR", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"copy", None))
        self.groupBox.setTitle("")
        self.chB_upper.setText(QCoreApplication.translate("MainWindow", u"Uppercase                                                                  ", None))
        self.chB_nums.setText(QCoreApplication.translate("MainWindow", u"Numbers                                                                     ", None))
        self.chB_chr.setText(QCoreApplication.translate("MainWindow", u"Special Characters                                                     ", None))
        self.chB_lower.setText(QCoreApplication.translate("MainWindow", u"Lowercase                                                                  ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password length:", None))
        self.lbl_length.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.lbl_msg.setText(QCoreApplication.translate("MainWindow", u"* YOU CREATE A WEAK PASSWORD", None))
    # retranslateUi

