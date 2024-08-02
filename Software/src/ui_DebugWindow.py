# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DebugWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(372, 50)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 331, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ip_input = QPlainTextEdit(self.layoutWidget)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_3.addWidget(self.ip_input)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.port_input = QPlainTextEdit(self.layoutWidget)
        self.port_input.setObjectName(u"port_input")
        self.port_input.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_3.addWidget(self.port_input)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.btn_connect = QPushButton(self.layoutWidget)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_connect)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ustawienia sieci", None))
        self.ip_input.setPlainText(QCoreApplication.translate("Dialog", u"192.168.4.1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"IP", None))
        self.port_input.setPlainText(QCoreApplication.translate("Dialog", u"8080", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.btn_connect.setText(QCoreApplication.translate("Dialog", u"Po\u0142\u0105cz", None))
    # retranslateUi

