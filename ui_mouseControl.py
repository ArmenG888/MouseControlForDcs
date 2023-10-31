# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mouseControlAbeHTk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 609)
        MainWindow.setStyleSheet(u"background-color:#18181b;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 859, 571))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(30)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 1px solid #323239; color:white; border-right:none;")

        self.horizontalLayout.addWidget(self.label_2)

        self.sens = QLineEdit(self.verticalLayoutWidget)
        self.sens.setObjectName(u"sens")
        self.sens.setFont(font1)
        self.sens.setStyleSheet(u"border: 1px solid #323239; color:white;")

        self.horizontalLayout.addWidget(self.sens)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border: 1px solid #323239; color:white; border-right:none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.key = QLineEdit(self.verticalLayoutWidget)
        self.key.setObjectName(u"key")
        self.key.setFont(font1)
        self.key.setStyleSheet(u"border: 1px solid #323239; color:white;")

        self.horizontalLayout_2.addWidget(self.key)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.startBtn = QPushButton(self.verticalLayoutWidget)
        self.startBtn.setObjectName(u"startBtn")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(19)
        self.startBtn.setFont(font2)
        self.startBtn.setStyleSheet(u"background-color:#772ce8; color:white; outline:none; border:none;")
        self.startBtn.setFlat(False)

        self.verticalLayout.addWidget(self.startBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.startBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mouse Control For DCS World", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sensitivity    ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key To Center", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

