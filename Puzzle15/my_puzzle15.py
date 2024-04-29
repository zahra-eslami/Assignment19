# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'puzzle15.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(354, 589)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(u"applications-games"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(55, 38, 72);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_pause = QPushButton(self.centralwidget)
        self.btn_pause.setObjectName(u"btn_pause")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_pause.sizePolicy().hasHeightForWidth())
        self.btn_pause.setSizePolicy(sizePolicy1)
        self.btn_pause.setMinimumSize(QSize(40, 40))
        self.btn_pause.setStyleSheet(u"background-color: rgb(227,71, 59);\n"
"border-radius: 5px; \n"
"")

        self.gridLayout_2.addWidget(self.btn_pause, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMinimumSize(QSize(10, 10))
        self.lineEdit_3.setStyleSheet(u"border: 0px ;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color: rgb(55, 38, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 0, 1, 6)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: 0px ;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color: rgb(55, 38, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 6)

        self.btn_new = QPushButton(self.centralwidget)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy1.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy1)
        self.btn_new.setMinimumSize(QSize(40, 40))
        self.btn_new.setStyleSheet(u"background-color: rgb(227,71, 59);\n"
"border-radius: 5px; ")

        self.gridLayout_2.addWidget(self.btn_new, 0, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(55, 38, 72);\n"
"border: 0px ;")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_12 = QPushButton(self.groupBox)
        self.btn_12.setObjectName(u"btn_12")
        sizePolicy.setHeightForWidth(self.btn_12.sizePolicy().hasHeightForWidth())
        self.btn_12.setSizePolicy(sizePolicy)
        self.btn_12.setStyleSheet(u"background-color: rgb(0,151,136);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_12, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.groupBox)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet(u"background-color: rgb(104, 159, 57);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_9, 2, 0, 1, 1)

        self.btn_2 = QPushButton(self.groupBox)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"background-color: rgb(255, 151, 0);\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QPushButton(self.groupBox)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet(u"background-color: rgb(103,59,183);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; \n"
"")

        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_6 = QPushButton(self.groupBox)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setStyleSheet(u"background-color: rgb(63, 81, 181);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_6, 1, 1, 1, 1)

        self.btn_10 = QPushButton(self.groupBox)
        self.btn_10.setObjectName(u"btn_10")
        sizePolicy.setHeightForWidth(self.btn_10.sizePolicy().hasHeightForWidth())
        self.btn_10.setSizePolicy(sizePolicy)
        self.btn_10.setStyleSheet(u"background-color: rgb(171, 70,188);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_10, 2, 1, 1, 1)

        self.btn_5 = QPushButton(self.groupBox)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet(u"background-color: rgb(67, 160, 81);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_5, 1, 0, 1, 1)

        self.btn_4 = QPushButton(self.groupBox)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setStyleSheet(u"background-color: rgb(245, 81, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_4, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.groupBox)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setStyleSheet(u"background-color: rgb(21,100, 192);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_7, 1, 2, 1, 1)

        self.btn_1 = QPushButton(self.groupBox)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet(u"background-color: rgb(176, 180, 44);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; \n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_13 = QPushButton(self.groupBox)
        self.btn_13.setObjectName(u"btn_13")
        sizePolicy.setHeightForWidth(self.btn_13.sizePolicy().hasHeightForWidth())
        self.btn_13.setSizePolicy(sizePolicy)
        self.btn_13.setStyleSheet(u"background-color: rgb(1, 151, 166);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_13, 3, 0, 1, 1)

        self.btn_11 = QPushButton(self.groupBox)
        self.btn_11.setObjectName(u"btn_11")
        sizePolicy.setHeightForWidth(self.btn_11.sizePolicy().hasHeightForWidth())
        self.btn_11.setSizePolicy(sizePolicy)
        self.btn_11.setStyleSheet(u"background-color: rgb(229, 57,53);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_11, 2, 2, 1, 1)

        self.btn_8 = QPushButton(self.groupBox)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setStyleSheet(u"background-color: rgb(236,64,122);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_8, 1, 3, 1, 1)

        self.btn_15 = QPushButton(self.groupBox)
        self.btn_15.setObjectName(u"btn_15")
        sizePolicy.setHeightForWidth(self.btn_15.sizePolicy().hasHeightForWidth())
        self.btn_15.setSizePolicy(sizePolicy)
        self.btn_15.setStyleSheet(u"background-color: rgb(131,118,24);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_15, 3, 2, 1, 1)

        self.btn_16 = QPushButton(self.groupBox)
        self.btn_16.setObjectName(u"btn_16")
        sizePolicy.setHeightForWidth(self.btn_16.sizePolicy().hasHeightForWidth())
        self.btn_16.setSizePolicy(sizePolicy)
        self.btn_16.setStyleSheet(u"background-color: rgb(0, 255, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_16, 3, 3, 1, 1)

        self.btn_14 = QPushButton(self.groupBox)
        self.btn_14.setObjectName(u"btn_14")
        sizePolicy.setHeightForWidth(self.btn_14.sizePolicy().hasHeightForWidth())
        self.btn_14.setSizePolicy(sizePolicy)
        self.btn_14.setStyleSheet(u"background-color: rgb(2, 136, 209);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"\n"
"border-radius: 10px; ")

        self.gridLayout.addWidget(self.btn_14, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 4, 0, 1, 6)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"border: 0px ;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color: rgb(55, 38, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_4, 5, 0, 1, 6)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(55, 38, 72);\n"
"border: 0px ;")

        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 5, 1, 1)

        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(40, 40))
        self.btn_close.setStyleSheet(u"background-color: rgb(227,71, 59);\n"
"border-radius: 5px; ")

        self.gridLayout_2.addWidget(self.btn_close, 0, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMinimumSize(QSize(10, 10))
        self.lineEdit_2.setStyleSheet(u"border: 0px ;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color: rgb(55, 38, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Calibri\";\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 0, 1, 6)

        self.btn_info = QPushButton(self.centralwidget)
        self.btn_info.setObjectName(u"btn_info")
        sizePolicy1.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy1)
        self.btn_info.setMinimumSize(QSize(40, 40))
        self.btn_info.setStyleSheet(u"background-color: rgb(227,71, 59);\n"
"border-radius: 5px; ")

        self.gridLayout_2.addWidget(self.btn_info, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Puzzle 15", None))
#if QT_CONFIG(tooltip)
        self.btn_pause.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#ffff00;\">\u062a\u0648\u0642\u0641 \u0645\u0648\u0642\u062a \u0628\u0627\u0632\u06cc</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pause.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit.setText("")
#if QT_CONFIG(tooltip)
        self.btn_new.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#ffff00;\">\u0634\u0631\u0648\u0639 \u0645\u062c\u062f\u062f \u0628\u0627\u0632\u06cc</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_new.setText("")
        self.groupBox.setTitle("")
        self.btn_12.setText("")
        self.btn_9.setText("")
        self.btn_2.setText("")
        self.btn_3.setText("")
        self.btn_6.setText("")
        self.btn_10.setText("")
        self.btn_5.setText("")
        self.btn_4.setText("")
        self.btn_7.setText("")
        self.btn_1.setText("")
        self.btn_13.setText("")
        self.btn_11.setText("")
        self.btn_8.setText("")
        self.btn_15.setText("")
        self.btn_16.setText("")
        self.btn_14.setText("")
        self.lineEdit_4.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#ffff00;\">\u062e\u0631\u0648\u062c\u06cc \u0627\u0632 \u0628\u0627\u0632\u06cc</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.lineEdit_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700; color:#ffff00;\">\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u0628\u0627\u0632\u06cc</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_info.setText("")
    # retranslateUi

