# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
        MainWindow.resize(896, 762)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(1)
        self.StartScreen = QWidget()
        self.StartScreen.setObjectName(u"StartScreen")
        self.verticalLayout_7 = QVBoxLayout(self.StartScreen)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(50, 50, 50, 50)
        self.BtnStartGame = QPushButton(self.StartScreen)
        self.BtnStartGame.setObjectName(u"BtnStartGame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnStartGame.sizePolicy().hasHeightForWidth())
        self.BtnStartGame.setSizePolicy(sizePolicy)
        self.BtnStartGame.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BtnStartGame.setFont(font)

        self.verticalLayout_7.addWidget(self.BtnStartGame)

        self.BtnLoadGame = QPushButton(self.StartScreen)
        self.BtnLoadGame.setObjectName(u"BtnLoadGame")
        self.BtnLoadGame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.BtnLoadGame.sizePolicy().hasHeightForWidth())
        self.BtnLoadGame.setSizePolicy(sizePolicy)
        self.BtnLoadGame.setMinimumSize(QSize(0, 100))
        self.BtnLoadGame.setFont(font)

        self.verticalLayout_7.addWidget(self.BtnLoadGame)

        self.BtnCreateTemplate = QPushButton(self.StartScreen)
        self.BtnCreateTemplate.setObjectName(u"BtnCreateTemplate")
        sizePolicy.setHeightForWidth(self.BtnCreateTemplate.sizePolicy().hasHeightForWidth())
        self.BtnCreateTemplate.setSizePolicy(sizePolicy)
        self.BtnCreateTemplate.setMinimumSize(QSize(0, 100))
        self.BtnCreateTemplate.setFont(font)

        self.verticalLayout_7.addWidget(self.BtnCreateTemplate)

        self.stackedWidget.addWidget(self.StartScreen)
        self.ChoseTemplate = QWidget()
        self.ChoseTemplate.setObjectName(u"ChoseTemplate")
        self.verticalLayout_5 = QVBoxLayout(self.ChoseTemplate)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.ChoseTemplate)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.TemplatesList = QListWidget(self.ChoseTemplate)
        self.TemplatesList.setObjectName(u"TemplatesList")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.TemplatesList.setFont(font2)

        self.verticalLayout_5.addWidget(self.TemplatesList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.ChoseTemplate)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4)

        self.num_of_players = QTextEdit(self.ChoseTemplate)
        self.num_of_players.setObjectName(u"num_of_players")
        self.num_of_players.setMaximumSize(QSize(50, 40))
        self.num_of_players.setFont(font1)

        self.horizontalLayout.addWidget(self.num_of_players)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.scrollArea_2 = QScrollArea(self.ChoseTemplate)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 324, 442))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.resource1_2 = QHBoxLayout()
        self.resource1_2.setObjectName(u"resource1_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_2.addItem(self.horizontalSpacer_5)

        self.g1_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g1_l.setObjectName(u"g1_l")
        font3 = QFont()
        font3.setPointSize(14)
        self.g1_l.setFont(font3)

        self.resource1_2.addWidget(self.g1_l)

        self.name_1 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_1.setObjectName(u"name_1")
        self.name_1.setMinimumSize(QSize(200, 0))
        self.name_1.setMaximumSize(QSize(16777215, 35))
        self.name_1.setFont(font3)

        self.resource1_2.addWidget(self.name_1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.resource1_2)

        self.resource1_3 = QHBoxLayout()
        self.resource1_3.setObjectName(u"resource1_3")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_3.addItem(self.horizontalSpacer_7)

        self.g2_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g2_l.setObjectName(u"g2_l")
        self.g2_l.setFont(font3)

        self.resource1_3.addWidget(self.g2_l)

        self.name_2 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setMinimumSize(QSize(200, 0))
        self.name_2.setMaximumSize(QSize(16777215, 35))
        self.name_2.setFont(font3)

        self.resource1_3.addWidget(self.name_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_6.addLayout(self.resource1_3)

        self.resource1_4 = QHBoxLayout()
        self.resource1_4.setObjectName(u"resource1_4")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_4.addItem(self.horizontalSpacer_9)

        self.g3_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g3_l.setObjectName(u"g3_l")
        self.g3_l.setFont(font3)

        self.resource1_4.addWidget(self.g3_l)

        self.name_3 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setMinimumSize(QSize(200, 0))
        self.name_3.setMaximumSize(QSize(16777215, 35))
        self.name_3.setFont(font3)

        self.resource1_4.addWidget(self.name_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addLayout(self.resource1_4)

        self.resource1_5 = QHBoxLayout()
        self.resource1_5.setObjectName(u"resource1_5")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_5.addItem(self.horizontalSpacer_11)

        self.g4_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g4_l.setObjectName(u"g4_l")
        self.g4_l.setFont(font3)

        self.resource1_5.addWidget(self.g4_l)

        self.name_4 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_4.setObjectName(u"name_4")
        self.name_4.setMinimumSize(QSize(200, 0))
        self.name_4.setMaximumSize(QSize(16777215, 35))
        self.name_4.setFont(font3)

        self.resource1_5.addWidget(self.name_4)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_5.addItem(self.horizontalSpacer_12)


        self.verticalLayout_6.addLayout(self.resource1_5)

        self.resource1_6 = QHBoxLayout()
        self.resource1_6.setObjectName(u"resource1_6")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_6.addItem(self.horizontalSpacer_13)

        self.g5_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g5_l.setObjectName(u"g5_l")
        self.g5_l.setFont(font3)

        self.resource1_6.addWidget(self.g5_l)

        self.name_5 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_5.setObjectName(u"name_5")
        self.name_5.setMinimumSize(QSize(200, 0))
        self.name_5.setMaximumSize(QSize(16777215, 35))
        self.name_5.setFont(font3)

        self.resource1_6.addWidget(self.name_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout_6.addLayout(self.resource1_6)

        self.resource1_7 = QHBoxLayout()
        self.resource1_7.setObjectName(u"resource1_7")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_7.addItem(self.horizontalSpacer_15)

        self.g6_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g6_l.setObjectName(u"g6_l")
        self.g6_l.setFont(font3)

        self.resource1_7.addWidget(self.g6_l)

        self.name_6 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_6.setObjectName(u"name_6")
        self.name_6.setMinimumSize(QSize(200, 0))
        self.name_6.setMaximumSize(QSize(16777215, 35))
        self.name_6.setFont(font3)

        self.resource1_7.addWidget(self.name_6)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_7.addItem(self.horizontalSpacer_16)


        self.verticalLayout_6.addLayout(self.resource1_7)

        self.resource1_8 = QHBoxLayout()
        self.resource1_8.setObjectName(u"resource1_8")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_8.addItem(self.horizontalSpacer_17)

        self.g7_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g7_l.setObjectName(u"g7_l")
        self.g7_l.setFont(font3)

        self.resource1_8.addWidget(self.g7_l)

        self.name_7 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_7.setObjectName(u"name_7")
        self.name_7.setMinimumSize(QSize(200, 0))
        self.name_7.setMaximumSize(QSize(16777215, 35))
        self.name_7.setFont(font3)

        self.resource1_8.addWidget(self.name_7)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_8.addItem(self.horizontalSpacer_18)


        self.verticalLayout_6.addLayout(self.resource1_8)

        self.resource1_9 = QHBoxLayout()
        self.resource1_9.setObjectName(u"resource1_9")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_9.addItem(self.horizontalSpacer_19)

        self.g8_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g8_l.setObjectName(u"g8_l")
        self.g8_l.setFont(font3)

        self.resource1_9.addWidget(self.g8_l)

        self.name_8 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_8.setObjectName(u"name_8")
        self.name_8.setMinimumSize(QSize(200, 0))
        self.name_8.setMaximumSize(QSize(16777215, 35))
        self.name_8.setFont(font3)

        self.resource1_9.addWidget(self.name_8)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_9.addItem(self.horizontalSpacer_20)


        self.verticalLayout_6.addLayout(self.resource1_9)

        self.resource1_10 = QHBoxLayout()
        self.resource1_10.setObjectName(u"resource1_10")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_10.addItem(self.horizontalSpacer_21)

        self.g9_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g9_l.setObjectName(u"g9_l")
        self.g9_l.setFont(font3)

        self.resource1_10.addWidget(self.g9_l)

        self.name_9 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_9.setObjectName(u"name_9")
        self.name_9.setMinimumSize(QSize(200, 0))
        self.name_9.setMaximumSize(QSize(16777215, 35))
        self.name_9.setFont(font3)

        self.resource1_10.addWidget(self.name_9)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_10.addItem(self.horizontalSpacer_22)


        self.verticalLayout_6.addLayout(self.resource1_10)

        self.resource1_11 = QHBoxLayout()
        self.resource1_11.setObjectName(u"resource1_11")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_11.addItem(self.horizontalSpacer_23)

        self.g10_l = QLabel(self.scrollAreaWidgetContents_2)
        self.g10_l.setObjectName(u"g10_l")
        self.g10_l.setFont(font3)

        self.resource1_11.addWidget(self.g10_l)

        self.name_10 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.name_10.setObjectName(u"name_10")
        self.name_10.setMinimumSize(QSize(200, 0))
        self.name_10.setMaximumSize(QSize(16777215, 35))
        self.name_10.setFont(font3)

        self.resource1_11.addWidget(self.name_10)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.resource1_11.addItem(self.horizontalSpacer_24)


        self.verticalLayout_6.addLayout(self.resource1_11)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BtnDelete_ChoseTemplate = QPushButton(self.ChoseTemplate)
        self.BtnDelete_ChoseTemplate.setObjectName(u"BtnDelete_ChoseTemplate")
        self.BtnDelete_ChoseTemplate.setMaximumSize(QSize(300, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.BtnDelete_ChoseTemplate.setFont(font4)

        self.horizontalLayout_6.addWidget(self.BtnDelete_ChoseTemplate)

        self.BtnStart_ChoseTemplate = QPushButton(self.ChoseTemplate)
        self.BtnStart_ChoseTemplate.setObjectName(u"BtnStart_ChoseTemplate")
        self.BtnStart_ChoseTemplate.setMaximumSize(QSize(300, 16777215))
        self.BtnStart_ChoseTemplate.setFont(font4)

        self.horizontalLayout_6.addWidget(self.BtnStart_ChoseTemplate)

        self.BtnReturn_ChoseTemplate = QPushButton(self.ChoseTemplate)
        self.BtnReturn_ChoseTemplate.setObjectName(u"BtnReturn_ChoseTemplate")
        self.BtnReturn_ChoseTemplate.setMaximumSize(QSize(300, 16777215))
        self.BtnReturn_ChoseTemplate.setFont(font4)

        self.horizontalLayout_6.addWidget(self.BtnReturn_ChoseTemplate)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.ChoseTemplate)
        self.GameInProgres = QWidget()
        self.GameInProgres.setObjectName(u"GameInProgres")
        self.verticalLayout_11 = QVBoxLayout(self.GameInProgres)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.player_option = QVBoxLayout()
        self.player_option.setObjectName(u"player_option")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.g_previous = QPushButton(self.GameInProgres)
        self.g_previous.setObjectName(u"g_previous")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.g_previous.sizePolicy().hasHeightForWidth())
        self.g_previous.setSizePolicy(sizePolicy2)
        self.g_previous.setMaximumSize(QSize(200, 50))
        self.g_previous.setFont(font3)

        self.horizontalLayout_9.addWidget(self.g_previous)

        self.g_curr_plr = QLabel(self.GameInProgres)
        self.g_curr_plr.setObjectName(u"g_curr_plr")
        sizePolicy2.setHeightForWidth(self.g_curr_plr.sizePolicy().hasHeightForWidth())
        self.g_curr_plr.setSizePolicy(sizePolicy2)
        self.g_curr_plr.setMinimumSize(QSize(200, 0))
        self.g_curr_plr.setMaximumSize(QSize(300, 50))
        font5 = QFont()
        font5.setPointSize(20)
        self.g_curr_plr.setFont(font5)
        self.g_curr_plr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.g_curr_plr)

        self.g_next = QPushButton(self.GameInProgres)
        self.g_next.setObjectName(u"g_next")
        sizePolicy1.setHeightForWidth(self.g_next.sizePolicy().hasHeightForWidth())
        self.g_next.setSizePolicy(sizePolicy1)
        self.g_next.setMaximumSize(QSize(200, 50))
        self.g_next.setFont(font3)

        self.horizontalLayout_9.addWidget(self.g_next)


        self.player_option.addLayout(self.horizontalLayout_9)


        self.verticalLayout_9.addLayout(self.player_option)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(35)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.g_res_layout_1 = QHBoxLayout()
        self.g_res_layout_1.setObjectName(u"g_res_layout_1")
        self.g_res1 = QLabel(self.GameInProgres)
        self.g_res1.setObjectName(u"g_res1")
        sizePolicy2.setHeightForWidth(self.g_res1.sizePolicy().hasHeightForWidth())
        self.g_res1.setSizePolicy(sizePolicy2)
        self.g_res1.setMinimumSize(QSize(300, 0))
        self.g_res1.setFont(font2)

        self.g_res_layout_1.addWidget(self.g_res1)

        self.g_v_res1 = QLabel(self.GameInProgres)
        self.g_v_res1.setObjectName(u"g_v_res1")
        sizePolicy2.setHeightForWidth(self.g_v_res1.sizePolicy().hasHeightForWidth())
        self.g_v_res1.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setWeight(50)
        self.g_v_res1.setFont(font6)

        self.g_res_layout_1.addWidget(self.g_v_res1)


        self.verticalLayout_4.addLayout(self.g_res_layout_1)

        self.g_res_layout_2 = QHBoxLayout()
        self.g_res_layout_2.setObjectName(u"g_res_layout_2")
        self.g_res2 = QLabel(self.GameInProgres)
        self.g_res2.setObjectName(u"g_res2")
        sizePolicy2.setHeightForWidth(self.g_res2.sizePolicy().hasHeightForWidth())
        self.g_res2.setSizePolicy(sizePolicy2)
        self.g_res2.setMinimumSize(QSize(300, 0))
        self.g_res2.setFont(font2)

        self.g_res_layout_2.addWidget(self.g_res2)

        self.g_v_res2 = QLabel(self.GameInProgres)
        self.g_v_res2.setObjectName(u"g_v_res2")
        sizePolicy2.setHeightForWidth(self.g_v_res2.sizePolicy().hasHeightForWidth())
        self.g_v_res2.setSizePolicy(sizePolicy2)
        self.g_v_res2.setFont(font6)

        self.g_res_layout_2.addWidget(self.g_v_res2)


        self.verticalLayout_4.addLayout(self.g_res_layout_2)

        self.g_res_layout_3 = QHBoxLayout()
        self.g_res_layout_3.setObjectName(u"g_res_layout_3")
        self.g_res3 = QLabel(self.GameInProgres)
        self.g_res3.setObjectName(u"g_res3")
        sizePolicy2.setHeightForWidth(self.g_res3.sizePolicy().hasHeightForWidth())
        self.g_res3.setSizePolicy(sizePolicy2)
        self.g_res3.setMinimumSize(QSize(300, 0))
        self.g_res3.setFont(font2)

        self.g_res_layout_3.addWidget(self.g_res3)

        self.g_v_res3 = QLabel(self.GameInProgres)
        self.g_v_res3.setObjectName(u"g_v_res3")
        sizePolicy2.setHeightForWidth(self.g_v_res3.sizePolicy().hasHeightForWidth())
        self.g_v_res3.setSizePolicy(sizePolicy2)
        self.g_v_res3.setFont(font6)

        self.g_res_layout_3.addWidget(self.g_v_res3)


        self.verticalLayout_4.addLayout(self.g_res_layout_3)

        self.g_res_layout_4 = QHBoxLayout()
        self.g_res_layout_4.setObjectName(u"g_res_layout_4")
        self.g_res4 = QLabel(self.GameInProgres)
        self.g_res4.setObjectName(u"g_res4")
        sizePolicy2.setHeightForWidth(self.g_res4.sizePolicy().hasHeightForWidth())
        self.g_res4.setSizePolicy(sizePolicy2)
        self.g_res4.setMinimumSize(QSize(300, 0))
        self.g_res4.setFont(font2)

        self.g_res_layout_4.addWidget(self.g_res4)

        self.g_v_res4 = QLabel(self.GameInProgres)
        self.g_v_res4.setObjectName(u"g_v_res4")
        sizePolicy2.setHeightForWidth(self.g_v_res4.sizePolicy().hasHeightForWidth())
        self.g_v_res4.setSizePolicy(sizePolicy2)
        self.g_v_res4.setFont(font6)

        self.g_res_layout_4.addWidget(self.g_v_res4)


        self.verticalLayout_4.addLayout(self.g_res_layout_4)

        self.g_res_layout_5 = QHBoxLayout()
        self.g_res_layout_5.setObjectName(u"g_res_layout_5")
        self.g_res5 = QLabel(self.GameInProgres)
        self.g_res5.setObjectName(u"g_res5")
        sizePolicy2.setHeightForWidth(self.g_res5.sizePolicy().hasHeightForWidth())
        self.g_res5.setSizePolicy(sizePolicy2)
        self.g_res5.setMinimumSize(QSize(300, 0))
        self.g_res5.setFont(font2)

        self.g_res_layout_5.addWidget(self.g_res5)

        self.g_v_res5 = QLabel(self.GameInProgres)
        self.g_v_res5.setObjectName(u"g_v_res5")
        sizePolicy2.setHeightForWidth(self.g_v_res5.sizePolicy().hasHeightForWidth())
        self.g_v_res5.setSizePolicy(sizePolicy2)
        self.g_v_res5.setFont(font6)

        self.g_res_layout_5.addWidget(self.g_v_res5)


        self.verticalLayout_4.addLayout(self.g_res_layout_5)

        self.g_res_layout_6 = QHBoxLayout()
        self.g_res_layout_6.setObjectName(u"g_res_layout_6")
        self.g_res6 = QLabel(self.GameInProgres)
        self.g_res6.setObjectName(u"g_res6")
        sizePolicy2.setHeightForWidth(self.g_res6.sizePolicy().hasHeightForWidth())
        self.g_res6.setSizePolicy(sizePolicy2)
        self.g_res6.setMinimumSize(QSize(300, 0))
        self.g_res6.setFont(font2)

        self.g_res_layout_6.addWidget(self.g_res6)

        self.g_v_res6 = QLabel(self.GameInProgres)
        self.g_v_res6.setObjectName(u"g_v_res6")
        sizePolicy2.setHeightForWidth(self.g_v_res6.sizePolicy().hasHeightForWidth())
        self.g_v_res6.setSizePolicy(sizePolicy2)
        self.g_v_res6.setFont(font6)

        self.g_res_layout_6.addWidget(self.g_v_res6)


        self.verticalLayout_4.addLayout(self.g_res_layout_6)

        self.g_res_layout_7 = QHBoxLayout()
        self.g_res_layout_7.setObjectName(u"g_res_layout_7")
        self.g_res7 = QLabel(self.GameInProgres)
        self.g_res7.setObjectName(u"g_res7")
        sizePolicy2.setHeightForWidth(self.g_res7.sizePolicy().hasHeightForWidth())
        self.g_res7.setSizePolicy(sizePolicy2)
        self.g_res7.setMinimumSize(QSize(300, 0))
        self.g_res7.setFont(font2)

        self.g_res_layout_7.addWidget(self.g_res7)

        self.g_v_res7 = QLabel(self.GameInProgres)
        self.g_v_res7.setObjectName(u"g_v_res7")
        sizePolicy2.setHeightForWidth(self.g_v_res7.sizePolicy().hasHeightForWidth())
        self.g_v_res7.setSizePolicy(sizePolicy2)
        self.g_v_res7.setFont(font6)

        self.g_res_layout_7.addWidget(self.g_v_res7)


        self.verticalLayout_4.addLayout(self.g_res_layout_7)

        self.g_res_layout_8 = QHBoxLayout()
        self.g_res_layout_8.setObjectName(u"g_res_layout_8")
        self.g_res8 = QLabel(self.GameInProgres)
        self.g_res8.setObjectName(u"g_res8")
        sizePolicy2.setHeightForWidth(self.g_res8.sizePolicy().hasHeightForWidth())
        self.g_res8.setSizePolicy(sizePolicy2)
        self.g_res8.setMinimumSize(QSize(300, 0))
        self.g_res8.setFont(font2)

        self.g_res_layout_8.addWidget(self.g_res8)

        self.g_v_res8 = QLabel(self.GameInProgres)
        self.g_v_res8.setObjectName(u"g_v_res8")
        sizePolicy2.setHeightForWidth(self.g_v_res8.sizePolicy().hasHeightForWidth())
        self.g_v_res8.setSizePolicy(sizePolicy2)
        self.g_v_res8.setFont(font6)

        self.g_res_layout_8.addWidget(self.g_v_res8)


        self.verticalLayout_4.addLayout(self.g_res_layout_8)

        self.g_res_layout_9 = QHBoxLayout()
        self.g_res_layout_9.setObjectName(u"g_res_layout_9")
        self.g_res9 = QLabel(self.GameInProgres)
        self.g_res9.setObjectName(u"g_res9")
        sizePolicy2.setHeightForWidth(self.g_res9.sizePolicy().hasHeightForWidth())
        self.g_res9.setSizePolicy(sizePolicy2)
        self.g_res9.setMinimumSize(QSize(300, 0))
        self.g_res9.setFont(font2)

        self.g_res_layout_9.addWidget(self.g_res9)

        self.g_v_res9 = QLabel(self.GameInProgres)
        self.g_v_res9.setObjectName(u"g_v_res9")
        sizePolicy2.setHeightForWidth(self.g_v_res9.sizePolicy().hasHeightForWidth())
        self.g_v_res9.setSizePolicy(sizePolicy2)
        self.g_v_res9.setFont(font6)

        self.g_res_layout_9.addWidget(self.g_v_res9)


        self.verticalLayout_4.addLayout(self.g_res_layout_9)

        self.g_res_layout_10 = QHBoxLayout()
        self.g_res_layout_10.setObjectName(u"g_res_layout_10")
        self.g_res10 = QLabel(self.GameInProgres)
        self.g_res10.setObjectName(u"g_res10")
        sizePolicy2.setHeightForWidth(self.g_res10.sizePolicy().hasHeightForWidth())
        self.g_res10.setSizePolicy(sizePolicy2)
        self.g_res10.setMinimumSize(QSize(300, 0))
        self.g_res10.setFont(font2)

        self.g_res_layout_10.addWidget(self.g_res10)

        self.g_v_res10 = QLabel(self.GameInProgres)
        self.g_v_res10.setObjectName(u"g_v_res10")
        sizePolicy2.setHeightForWidth(self.g_v_res10.sizePolicy().hasHeightForWidth())
        self.g_v_res10.setSizePolicy(sizePolicy2)
        self.g_v_res10.setFont(font6)

        self.g_res_layout_10.addWidget(self.g_v_res10)


        self.verticalLayout_4.addLayout(self.g_res_layout_10)


        self.verticalLayout_9.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.GameInProgres)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.CommandLogs = QListWidget(self.GameInProgres)
        self.CommandLogs.setObjectName(u"CommandLogs")
        self.CommandLogs.setFont(font)

        self.verticalLayout_10.addWidget(self.CommandLogs)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(0)
        self.buttons.setObjectName(u"buttons")
        self.BtnSave_inGame = QPushButton(self.GameInProgres)
        self.BtnSave_inGame.setObjectName(u"BtnSave_inGame")
        self.BtnSave_inGame.setEnabled(True)
        self.BtnSave_inGame.setMinimumSize(QSize(300, 50))
        self.BtnSave_inGame.setMaximumSize(QSize(300, 16777215))
        self.BtnSave_inGame.setFont(font2)

        self.buttons.addWidget(self.BtnSave_inGame)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.buttons.addItem(self.horizontalSpacer_25)

        self.BtnReturn_InGame = QPushButton(self.GameInProgres)
        self.BtnReturn_InGame.setObjectName(u"BtnReturn_InGame")
        self.BtnReturn_InGame.setMinimumSize(QSize(300, 50))
        self.BtnReturn_InGame.setMaximumSize(QSize(300, 16777215))
        self.BtnReturn_InGame.setFont(font2)

        self.buttons.addWidget(self.BtnReturn_InGame)


        self.verticalLayout_11.addLayout(self.buttons)

        self.stackedWidget.addWidget(self.GameInProgres)
        self.CreateTemplate = QWidget()
        self.CreateTemplate.setObjectName(u"CreateTemplate")
        self.verticalLayout_3 = QVBoxLayout(self.CreateTemplate)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.CreateTemplate)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.TempCreation_name = QTextEdit(self.CreateTemplate)
        self.TempCreation_name.setObjectName(u"TempCreation_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TempCreation_name.sizePolicy().hasHeightForWidth())
        self.TempCreation_name.setSizePolicy(sizePolicy3)
        self.TempCreation_name.setMinimumSize(QSize(500, 0))
        self.TempCreation_name.setMaximumSize(QSize(500, 40))
        self.TempCreation_name.setFont(font1)
        self.TempCreation_name.setFrameShape(QFrame.StyledPanel)
        self.TempCreation_name.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.TempCreation_name.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.TempCreation_name.setTabStopWidth(80)

        self.horizontalLayout_7.addWidget(self.TempCreation_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dice_checkBox = QCheckBox(self.CreateTemplate)
        self.dice_checkBox.setObjectName(u"dice_checkBox")
        self.dice_checkBox.setMinimumSize(QSize(0, 0))
        self.dice_checkBox.setFont(font1)
        self.dice_checkBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.dice_checkBox)

        self.dice_l1 = QLabel(self.CreateTemplate)
        self.dice_l1.setObjectName(u"dice_l1")
        self.dice_l1.setEnabled(True)
        self.dice_l1.setMaximumSize(QSize(16777215, 50))
        self.dice_l1.setFont(font1)

        self.horizontalLayout_4.addWidget(self.dice_l1)

        self.dice_walls = QTextEdit(self.CreateTemplate)
        self.dice_walls.setObjectName(u"dice_walls")
        self.dice_walls.setEnabled(True)
        self.dice_walls.setMinimumSize(QSize(0, 0))
        self.dice_walls.setMaximumSize(QSize(50, 40))
        self.dice_walls.setFont(font1)

        self.horizontalLayout_4.addWidget(self.dice_walls)

        self.dice_l2 = QLabel(self.CreateTemplate)
        self.dice_l2.setObjectName(u"dice_l2")
        self.dice_l2.setEnabled(True)
        self.dice_l2.setMaximumSize(QSize(16777215, 50))
        self.dice_l2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.dice_l2)

        self.dice_throws = QTextEdit(self.CreateTemplate)
        self.dice_throws.setObjectName(u"dice_throws")
        self.dice_throws.setEnabled(True)
        self.dice_throws.setMaximumSize(QSize(50, 40))
        self.dice_throws.setFont(font1)

        self.horizontalLayout_4.addWidget(self.dice_throws)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.CreateTemplate)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 50))
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.number_of_resources = QTextEdit(self.CreateTemplate)
        self.number_of_resources.setObjectName(u"number_of_resources")
        self.number_of_resources.setMaximumSize(QSize(50, 40))
        self.number_of_resources.setFont(font1)

        self.horizontalLayout_5.addWidget(self.number_of_resources)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.scrollArea = QScrollArea(self.CreateTemplate)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 817, 442))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.resource1 = QHBoxLayout()
        self.resource1.setObjectName(u"resource1")
        self.res1_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res1_l1.setObjectName(u"res1_l1")
        self.res1_l1.setFont(font3)

        self.resource1.addWidget(self.res1_l1)

        self.res1_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res1_name.setObjectName(u"res1_name")
        self.res1_name.setMinimumSize(QSize(200, 0))
        self.res1_name.setMaximumSize(QSize(16777215, 35))
        self.res1_name.setFont(font3)

        self.resource1.addWidget(self.res1_name)

        self.res1_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res1_l2.setObjectName(u"res1_l2")
        self.res1_l2.setFont(font3)

        self.resource1.addWidget(self.res1_l2)

        self.res1_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res1_min.setObjectName(u"res1_min")
        self.res1_min.setMaximumSize(QSize(16777215, 35))
        self.res1_min.setFont(font3)

        self.resource1.addWidget(self.res1_min)

        self.res1_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res1_l3.setObjectName(u"res1_l3")
        self.res1_l3.setFont(font3)

        self.resource1.addWidget(self.res1_l3)

        self.res1_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res1_max.setObjectName(u"res1_max")
        self.res1_max.setMaximumSize(QSize(16777215, 35))
        self.res1_max.setFont(font3)

        self.resource1.addWidget(self.res1_max)

        self.res1_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res1_l4.setObjectName(u"res1_l4")
        self.res1_l4.setFont(font3)

        self.resource1.addWidget(self.res1_l4)

        self.res1_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res1_curr.setObjectName(u"res1_curr")
        self.res1_curr.setMaximumSize(QSize(16777215, 35))
        self.res1_curr.setFont(font3)

        self.resource1.addWidget(self.res1_curr)


        self.verticalLayout.addLayout(self.resource1)

        self.resource2 = QHBoxLayout()
        self.resource2.setObjectName(u"resource2")
        self.res2_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res2_l1.setObjectName(u"res2_l1")
        self.res2_l1.setFont(font3)

        self.resource2.addWidget(self.res2_l1)

        self.res2_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res2_name.setObjectName(u"res2_name")
        self.res2_name.setMinimumSize(QSize(200, 0))
        self.res2_name.setMaximumSize(QSize(16777215, 35))
        self.res2_name.setFont(font3)

        self.resource2.addWidget(self.res2_name)

        self.res2_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res2_l2.setObjectName(u"res2_l2")
        self.res2_l2.setFont(font3)

        self.resource2.addWidget(self.res2_l2)

        self.res2_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res2_min.setObjectName(u"res2_min")
        self.res2_min.setMaximumSize(QSize(16777215, 35))
        self.res2_min.setFont(font3)

        self.resource2.addWidget(self.res2_min)

        self.res2_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res2_l3.setObjectName(u"res2_l3")
        self.res2_l3.setFont(font3)

        self.resource2.addWidget(self.res2_l3)

        self.res2_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res2_max.setObjectName(u"res2_max")
        self.res2_max.setMaximumSize(QSize(16777215, 35))
        self.res2_max.setFont(font3)

        self.resource2.addWidget(self.res2_max)

        self.res2_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res2_l4.setObjectName(u"res2_l4")
        self.res2_l4.setFont(font3)

        self.resource2.addWidget(self.res2_l4)

        self.res2_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res2_curr.setObjectName(u"res2_curr")
        self.res2_curr.setMaximumSize(QSize(16777215, 35))
        self.res2_curr.setFont(font3)

        self.resource2.addWidget(self.res2_curr)


        self.verticalLayout.addLayout(self.resource2)

        self.resource3 = QHBoxLayout()
        self.resource3.setObjectName(u"resource3")
        self.res3_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res3_l1.setObjectName(u"res3_l1")
        self.res3_l1.setFont(font3)

        self.resource3.addWidget(self.res3_l1)

        self.res3_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res3_name.setObjectName(u"res3_name")
        self.res3_name.setMinimumSize(QSize(200, 0))
        self.res3_name.setMaximumSize(QSize(16777215, 35))
        self.res3_name.setFont(font3)

        self.resource3.addWidget(self.res3_name)

        self.res3_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res3_l2.setObjectName(u"res3_l2")
        self.res3_l2.setFont(font3)

        self.resource3.addWidget(self.res3_l2)

        self.res3_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res3_min.setObjectName(u"res3_min")
        self.res3_min.setMaximumSize(QSize(16777215, 35))
        self.res3_min.setFont(font3)

        self.resource3.addWidget(self.res3_min)

        self.res3_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res3_l3.setObjectName(u"res3_l3")
        self.res3_l3.setFont(font3)

        self.resource3.addWidget(self.res3_l3)

        self.res3_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res3_max.setObjectName(u"res3_max")
        self.res3_max.setMaximumSize(QSize(16777215, 35))
        self.res3_max.setFont(font3)

        self.resource3.addWidget(self.res3_max)

        self.res3_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res3_l4.setObjectName(u"res3_l4")
        self.res3_l4.setFont(font3)

        self.resource3.addWidget(self.res3_l4)

        self.res3_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res3_curr.setObjectName(u"res3_curr")
        self.res3_curr.setMaximumSize(QSize(16777215, 35))
        self.res3_curr.setFont(font3)

        self.resource3.addWidget(self.res3_curr)


        self.verticalLayout.addLayout(self.resource3)

        self.resource4 = QHBoxLayout()
        self.resource4.setObjectName(u"resource4")
        self.res4_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res4_l1.setObjectName(u"res4_l1")
        self.res4_l1.setFont(font3)

        self.resource4.addWidget(self.res4_l1)

        self.res4_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res4_name.setObjectName(u"res4_name")
        self.res4_name.setMinimumSize(QSize(200, 0))
        self.res4_name.setMaximumSize(QSize(16777215, 35))
        self.res4_name.setFont(font3)

        self.resource4.addWidget(self.res4_name)

        self.res4_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res4_l2.setObjectName(u"res4_l2")
        self.res4_l2.setFont(font3)

        self.resource4.addWidget(self.res4_l2)

        self.res4_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res4_min.setObjectName(u"res4_min")
        self.res4_min.setMaximumSize(QSize(16777215, 35))
        self.res4_min.setFont(font3)

        self.resource4.addWidget(self.res4_min)

        self.res4_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res4_l3.setObjectName(u"res4_l3")
        self.res4_l3.setFont(font3)

        self.resource4.addWidget(self.res4_l3)

        self.res4_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res4_max.setObjectName(u"res4_max")
        self.res4_max.setMaximumSize(QSize(16777215, 35))
        self.res4_max.setFont(font3)

        self.resource4.addWidget(self.res4_max)

        self.res4_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res4_l4.setObjectName(u"res4_l4")
        self.res4_l4.setFont(font3)

        self.resource4.addWidget(self.res4_l4)

        self.res4_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res4_curr.setObjectName(u"res4_curr")
        self.res4_curr.setMaximumSize(QSize(16777215, 35))
        self.res4_curr.setFont(font3)

        self.resource4.addWidget(self.res4_curr)


        self.verticalLayout.addLayout(self.resource4)

        self.resource5 = QHBoxLayout()
        self.resource5.setObjectName(u"resource5")
        self.res5_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res5_l1.setObjectName(u"res5_l1")
        self.res5_l1.setFont(font3)

        self.resource5.addWidget(self.res5_l1)

        self.res5_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res5_name.setObjectName(u"res5_name")
        self.res5_name.setMinimumSize(QSize(200, 0))
        self.res5_name.setMaximumSize(QSize(16777215, 35))
        self.res5_name.setFont(font3)

        self.resource5.addWidget(self.res5_name)

        self.res5_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res5_l2.setObjectName(u"res5_l2")
        self.res5_l2.setFont(font3)

        self.resource5.addWidget(self.res5_l2)

        self.res5_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res5_min.setObjectName(u"res5_min")
        self.res5_min.setMaximumSize(QSize(16777215, 35))
        self.res5_min.setFont(font3)

        self.resource5.addWidget(self.res5_min)

        self.res5_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res5_l3.setObjectName(u"res5_l3")
        self.res5_l3.setFont(font3)

        self.resource5.addWidget(self.res5_l3)

        self.res5_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res5_max.setObjectName(u"res5_max")
        self.res5_max.setMaximumSize(QSize(16777215, 35))
        self.res5_max.setFont(font3)

        self.resource5.addWidget(self.res5_max)

        self.res5_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res5_l4.setObjectName(u"res5_l4")
        self.res5_l4.setFont(font3)

        self.resource5.addWidget(self.res5_l4)

        self.res5_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res5_curr.setObjectName(u"res5_curr")
        self.res5_curr.setMaximumSize(QSize(16777215, 35))
        self.res5_curr.setFont(font3)

        self.resource5.addWidget(self.res5_curr)


        self.verticalLayout.addLayout(self.resource5)

        self.resource6 = QHBoxLayout()
        self.resource6.setObjectName(u"resource6")
        self.res6_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res6_l1.setObjectName(u"res6_l1")
        self.res6_l1.setFont(font3)

        self.resource6.addWidget(self.res6_l1)

        self.res6_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res6_name.setObjectName(u"res6_name")
        self.res6_name.setMinimumSize(QSize(200, 0))
        self.res6_name.setMaximumSize(QSize(16777215, 35))
        self.res6_name.setFont(font3)

        self.resource6.addWidget(self.res6_name)

        self.res6_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res6_l2.setObjectName(u"res6_l2")
        self.res6_l2.setFont(font3)

        self.resource6.addWidget(self.res6_l2)

        self.res6_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res6_min.setObjectName(u"res6_min")
        self.res6_min.setMaximumSize(QSize(16777215, 35))
        self.res6_min.setFont(font3)

        self.resource6.addWidget(self.res6_min)

        self.res6_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res6_l3.setObjectName(u"res6_l3")
        self.res6_l3.setFont(font3)

        self.resource6.addWidget(self.res6_l3)

        self.res6_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res6_max.setObjectName(u"res6_max")
        self.res6_max.setMaximumSize(QSize(16777215, 35))
        self.res6_max.setFont(font3)

        self.resource6.addWidget(self.res6_max)

        self.res6_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res6_l4.setObjectName(u"res6_l4")
        self.res6_l4.setFont(font3)

        self.resource6.addWidget(self.res6_l4)

        self.res6_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res6_curr.setObjectName(u"res6_curr")
        self.res6_curr.setMaximumSize(QSize(16777215, 35))
        self.res6_curr.setFont(font3)

        self.resource6.addWidget(self.res6_curr)


        self.verticalLayout.addLayout(self.resource6)

        self.resource7 = QHBoxLayout()
        self.resource7.setObjectName(u"resource7")
        self.res7_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res7_l1.setObjectName(u"res7_l1")
        self.res7_l1.setFont(font3)

        self.resource7.addWidget(self.res7_l1)

        self.res7_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res7_name.setObjectName(u"res7_name")
        self.res7_name.setMinimumSize(QSize(200, 0))
        self.res7_name.setMaximumSize(QSize(16777215, 35))
        self.res7_name.setFont(font3)

        self.resource7.addWidget(self.res7_name)

        self.res7_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res7_l2.setObjectName(u"res7_l2")
        self.res7_l2.setFont(font3)

        self.resource7.addWidget(self.res7_l2)

        self.res7_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res7_min.setObjectName(u"res7_min")
        self.res7_min.setMaximumSize(QSize(16777215, 35))
        self.res7_min.setFont(font3)

        self.resource7.addWidget(self.res7_min)

        self.res7_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res7_l3.setObjectName(u"res7_l3")
        self.res7_l3.setFont(font3)

        self.resource7.addWidget(self.res7_l3)

        self.res7_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res7_max.setObjectName(u"res7_max")
        self.res7_max.setMaximumSize(QSize(16777215, 35))
        self.res7_max.setFont(font3)

        self.resource7.addWidget(self.res7_max)

        self.res7_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res7_l4.setObjectName(u"res7_l4")
        self.res7_l4.setFont(font3)

        self.resource7.addWidget(self.res7_l4)

        self.res7_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res7_curr.setObjectName(u"res7_curr")
        self.res7_curr.setMaximumSize(QSize(16777215, 35))
        self.res7_curr.setFont(font3)

        self.resource7.addWidget(self.res7_curr)


        self.verticalLayout.addLayout(self.resource7)

        self.resource8 = QHBoxLayout()
        self.resource8.setObjectName(u"resource8")
        self.res8_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res8_l1.setObjectName(u"res8_l1")
        self.res8_l1.setFont(font3)

        self.resource8.addWidget(self.res8_l1)

        self.res8_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res8_name.setObjectName(u"res8_name")
        self.res8_name.setMinimumSize(QSize(200, 0))
        self.res8_name.setMaximumSize(QSize(16777215, 35))
        self.res8_name.setFont(font3)

        self.resource8.addWidget(self.res8_name)

        self.res8_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res8_l2.setObjectName(u"res8_l2")
        self.res8_l2.setFont(font3)

        self.resource8.addWidget(self.res8_l2)

        self.res8_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res8_min.setObjectName(u"res8_min")
        self.res8_min.setMaximumSize(QSize(16777215, 35))
        self.res8_min.setFont(font3)

        self.resource8.addWidget(self.res8_min)

        self.res8_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res8_l3.setObjectName(u"res8_l3")
        self.res8_l3.setFont(font3)

        self.resource8.addWidget(self.res8_l3)

        self.res8_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res8_max.setObjectName(u"res8_max")
        self.res8_max.setMaximumSize(QSize(16777215, 35))
        self.res8_max.setFont(font3)

        self.resource8.addWidget(self.res8_max)

        self.res8_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res8_l4.setObjectName(u"res8_l4")
        self.res8_l4.setFont(font3)

        self.resource8.addWidget(self.res8_l4)

        self.res8_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res8_curr.setObjectName(u"res8_curr")
        self.res8_curr.setMaximumSize(QSize(16777215, 35))
        self.res8_curr.setFont(font3)

        self.resource8.addWidget(self.res8_curr)


        self.verticalLayout.addLayout(self.resource8)

        self.resource9 = QHBoxLayout()
        self.resource9.setObjectName(u"resource9")
        self.res9_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res9_l1.setObjectName(u"res9_l1")
        self.res9_l1.setFont(font3)

        self.resource9.addWidget(self.res9_l1)

        self.res9_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res9_name.setObjectName(u"res9_name")
        self.res9_name.setMinimumSize(QSize(200, 0))
        self.res9_name.setMaximumSize(QSize(16777215, 35))
        self.res9_name.setFont(font3)

        self.resource9.addWidget(self.res9_name)

        self.res9_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res9_l2.setObjectName(u"res9_l2")
        self.res9_l2.setFont(font3)

        self.resource9.addWidget(self.res9_l2)

        self.res9_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res9_min.setObjectName(u"res9_min")
        self.res9_min.setMaximumSize(QSize(16777215, 35))
        self.res9_min.setFont(font3)

        self.resource9.addWidget(self.res9_min)

        self.res9_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res9_l3.setObjectName(u"res9_l3")
        self.res9_l3.setFont(font3)

        self.resource9.addWidget(self.res9_l3)

        self.res9_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res9_max.setObjectName(u"res9_max")
        self.res9_max.setMaximumSize(QSize(16777215, 35))
        self.res9_max.setFont(font3)

        self.resource9.addWidget(self.res9_max)

        self.res9_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res9_l4.setObjectName(u"res9_l4")
        self.res9_l4.setFont(font3)

        self.resource9.addWidget(self.res9_l4)

        self.res9_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res9_curr.setObjectName(u"res9_curr")
        self.res9_curr.setMaximumSize(QSize(16777215, 35))
        self.res9_curr.setFont(font3)

        self.resource9.addWidget(self.res9_curr)


        self.verticalLayout.addLayout(self.resource9)

        self.resource10 = QHBoxLayout()
        self.resource10.setObjectName(u"resource10")
        self.res10_l1 = QLabel(self.scrollAreaWidgetContents)
        self.res10_l1.setObjectName(u"res10_l1")
        self.res10_l1.setFont(font3)

        self.resource10.addWidget(self.res10_l1)

        self.res10_name = QTextEdit(self.scrollAreaWidgetContents)
        self.res10_name.setObjectName(u"res10_name")
        self.res10_name.setMinimumSize(QSize(200, 0))
        self.res10_name.setMaximumSize(QSize(16777215, 35))
        self.res10_name.setFont(font3)

        self.resource10.addWidget(self.res10_name)

        self.res10_l2 = QLabel(self.scrollAreaWidgetContents)
        self.res10_l2.setObjectName(u"res10_l2")
        self.res10_l2.setFont(font3)

        self.resource10.addWidget(self.res10_l2)

        self.res10_min = QTextEdit(self.scrollAreaWidgetContents)
        self.res10_min.setObjectName(u"res10_min")
        self.res10_min.setMaximumSize(QSize(16777215, 35))
        self.res10_min.setFont(font3)

        self.resource10.addWidget(self.res10_min)

        self.res10_l3 = QLabel(self.scrollAreaWidgetContents)
        self.res10_l3.setObjectName(u"res10_l3")
        self.res10_l3.setFont(font3)

        self.resource10.addWidget(self.res10_l3)

        self.res10_max = QTextEdit(self.scrollAreaWidgetContents)
        self.res10_max.setObjectName(u"res10_max")
        self.res10_max.setMaximumSize(QSize(16777215, 35))
        self.res10_max.setFont(font3)

        self.resource10.addWidget(self.res10_max)

        self.res10_l4 = QLabel(self.scrollAreaWidgetContents)
        self.res10_l4.setObjectName(u"res10_l4")
        self.res10_l4.setFont(font3)

        self.resource10.addWidget(self.res10_l4)

        self.res10_curr = QTextEdit(self.scrollAreaWidgetContents)
        self.res10_curr.setObjectName(u"res10_curr")
        self.res10_curr.setMaximumSize(QSize(16777215, 35))
        self.res10_curr.setFont(font3)

        self.resource10.addWidget(self.res10_curr)


        self.verticalLayout.addLayout(self.resource10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BtnCreate_CreateTemplate = QPushButton(self.CreateTemplate)
        self.BtnCreate_CreateTemplate.setObjectName(u"BtnCreate_CreateTemplate")
        self.BtnCreate_CreateTemplate.setMinimumSize(QSize(0, 50))
        self.BtnCreate_CreateTemplate.setFont(font4)

        self.horizontalLayout_2.addWidget(self.BtnCreate_CreateTemplate)

        self.BtnReturn_CreateTemplate = QPushButton(self.CreateTemplate)
        self.BtnReturn_CreateTemplate.setObjectName(u"BtnReturn_CreateTemplate")
        self.BtnReturn_CreateTemplate.setMinimumSize(QSize(0, 50))
        self.BtnReturn_CreateTemplate.setFont(font4)

        self.horizontalLayout_2.addWidget(self.BtnReturn_CreateTemplate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.CreateTemplate)
        self.LoadGame = QWidget()
        self.LoadGame.setObjectName(u"LoadGame")
        self.verticalLayout_2 = QVBoxLayout(self.LoadGame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.LoadGame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.SavesList = QListWidget(self.LoadGame)
        self.SavesList.setObjectName(u"SavesList")
        self.SavesList.setFont(font2)

        self.verticalLayout_8.addWidget(self.SavesList)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BtnDelete_Chosen_Save = QPushButton(self.LoadGame)
        self.BtnDelete_Chosen_Save.setObjectName(u"BtnDelete_Chosen_Save")
        self.BtnDelete_Chosen_Save.setMaximumSize(QSize(300, 16777215))
        self.BtnDelete_Chosen_Save.setFont(font4)

        self.horizontalLayout_8.addWidget(self.BtnDelete_Chosen_Save)

        self.BtnStart_Chosen_Game = QPushButton(self.LoadGame)
        self.BtnStart_Chosen_Game.setObjectName(u"BtnStart_Chosen_Game")
        self.BtnStart_Chosen_Game.setMaximumSize(QSize(300, 16777215))
        self.BtnStart_Chosen_Game.setFont(font4)

        self.horizontalLayout_8.addWidget(self.BtnStart_Chosen_Game)

        self.BtnReturn_LoadGame = QPushButton(self.LoadGame)
        self.BtnReturn_LoadGame.setObjectName(u"BtnReturn_LoadGame")
        self.BtnReturn_LoadGame.setMaximumSize(QSize(300, 16777215))
        self.BtnReturn_LoadGame.setFont(font4)

        self.horizontalLayout_8.addWidget(self.BtnReturn_LoadGame)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.LoadGame)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DiceTech", None))
        self.BtnStartGame.setText(QCoreApplication.translate("MainWindow", u"NOWA GRA", None))
        self.BtnLoadGame.setText(QCoreApplication.translate("MainWindow", u"WCZYTAJ GR\u0118", None))
        self.BtnCreateTemplate.setText(QCoreApplication.translate("MainWindow", u"UTW\u00d3RZ SZABLON", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz szablon", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Liczba graczy:", None))
        self.num_of_players.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.g1_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 1: ", None))
        self.g2_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 2: ", None))
        self.g3_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 3: ", None))
        self.g4_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 4: ", None))
        self.g5_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 5: ", None))
        self.g6_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 6: ", None))
        self.g7_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 7: ", None))
        self.g8_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 8: ", None))
        self.g9_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 9: ", None))
        self.g10_l.setText(QCoreApplication.translate("MainWindow", u"Gracz 10: ", None))
        self.BtnDelete_ChoseTemplate.setText(QCoreApplication.translate("MainWindow", u"USU\u0143", None))
        self.BtnStart_ChoseTemplate.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.BtnReturn_ChoseTemplate.setText(QCoreApplication.translate("MainWindow", u"WR\u00d3\u0106", None))
        self.g_previous.setText(QCoreApplication.translate("MainWindow", u"Poprzedni", None))
        self.g_curr_plr.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.g_next.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pny", None))
        self.g_res1.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res1.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res2.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res2.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res3.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res3.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res4.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res4.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res5.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res5.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res6.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res6.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res7.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res7.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res8.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res8.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res9.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res9.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.g_res10.setText(QCoreApplication.translate("MainWindow", u"Resource:", None))
        self.g_v_res10.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Przebieg rozgrywki", None))
        self.BtnSave_inGame.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.BtnReturn_InGame.setText(QCoreApplication.translate("MainWindow", u"Wyjd\u017a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Podaj nazw\u0119 szablonu:", None))
        self.dice_checkBox.setText(QCoreApplication.translate("MainWindow", u"Kostka", None))
        self.dice_l1.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 \u015bcian:", None))
        self.dice_l2.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 rzut\u00f3w:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 zasob\u00f3w", None))
        self.number_of_resources.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.res1_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res1_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res1_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res1_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res2_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res2_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res2_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res2_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res3_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res3_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res3_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res3_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res4_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res4_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res4_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res4_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res5_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res5_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res5_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res5_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res6_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res6_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res6_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res6_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res7_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res7_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res7_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res7_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res8_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res8_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res8_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res8_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res9_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res9_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res9_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res9_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.res10_l1.setText(QCoreApplication.translate("MainWindow", u"Nazwa:", None))
        self.res10_l2.setText(QCoreApplication.translate("MainWindow", u"Zakres: od", None))
        self.res10_l3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.res10_l4.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 pocz\u0105tkowa", None))
        self.BtnCreate_CreateTemplate.setText(QCoreApplication.translate("MainWindow", u"STW\u00d3RZ", None))
        self.BtnReturn_CreateTemplate.setText(QCoreApplication.translate("MainWindow", u"WR\u00d3\u0106", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wybierz zapis gry", None))
        self.BtnDelete_Chosen_Save.setText(QCoreApplication.translate("MainWindow", u"USU\u0143", None))
        self.BtnStart_Chosen_Game.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.BtnReturn_LoadGame.setText(QCoreApplication.translate("MainWindow", u"WR\u00d3\u0106", None))
    # retranslateUi

