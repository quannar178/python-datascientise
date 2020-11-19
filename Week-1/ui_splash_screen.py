# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'splash-screenGJLBHx.ui'
##
# Created by: Qt User Interface Compiler version 5.14.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(1000, 600)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"QFrame{\n"
                                           "	background-color: rgb(56, 58, 89);\n"
                                           "	\n"
                                           "	color: rgb(220, 220, 220);\n"
                                           "\n"
                                           "	border-radius: 20px;\n"
                                           "}")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.DropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 102, 981, 151))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(35)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.DropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 222, 981, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.DropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 378, 921, 51))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "	\n"
                                       "	background-color: rgb(94, 114, 164);\n"
                                       "\n"
                                       "	\n"
                                       "	color: rgb(200, 200, 200);\n"
                                       "\n"
                                       "	border-style: none;\n"
                                       "	\n"
                                       "	border-radius: 20px;\n"
                                       "	\n"
                                       "	text-align: center;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "	\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.488636, x2:1, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
                                       "border-radius: 20px;\n"
                                       "}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.DropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(-10, 438, 981, 61))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_created = QLabel(self.DropShadowFrame)
        self.label_created.setObjectName(u"label_created")
        self.label_created.setGeometry(QRect(200, 510, 741, 61))
        self.label_created.setFont(font2)
        self.label_created.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_created.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.DropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate(
            "SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate(
            "SplashScreen", u"<strong>YOUR</strong> APP NAME", None))
        self.label_description.setText(QCoreApplication.translate(
            "SplashScreen", u"<strong>APP</strong> DESCRIPTION", None))
        self.label_loading.setText(QCoreApplication.translate(
            "SplashScreen", u"loading ...", None))
        self.label_created.setText(QCoreApplication.translate(
            "SplashScreen", u"Created: Nguyen Ba Quan", None))
    # retranslateUi
