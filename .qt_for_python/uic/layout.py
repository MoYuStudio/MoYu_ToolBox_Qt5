# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(718, 318)
        Window.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(Window)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(Window)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(700, 300))
        self.tabWidget.setStyleSheet(u"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidget_hub = QWidget()
        self.tabWidget_hub.setObjectName(u"tabWidget_hub")
        self.tabWidget.addTab(self.tabWidget_hub, "")
        self.tabWidget_up = QWidget()
        self.tabWidget_up.setObjectName(u"tabWidget_up")
        self.gridLayout_4 = QGridLayout(self.tabWidget_up)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_obs = QPushButton(self.tabWidget_up)
        self.pushButton_obs.setObjectName(u"pushButton_obs")
        self.pushButton_obs.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.pushButton_obs, 0, 0, 1, 1)

        self.pushButton_androidtopc = QPushButton(self.tabWidget_up)
        self.pushButton_androidtopc.setObjectName(u"pushButton_androidtopc")
        self.pushButton_androidtopc.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.pushButton_androidtopc, 2, 0, 1, 1)

        self.pushButton_liveass = QPushButton(self.tabWidget_up)
        self.pushButton_liveass.setObjectName(u"pushButton_liveass")
        self.pushButton_liveass.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.pushButton_liveass, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tabWidget_up, "")
        self.tabWidget_mc = QWidget()
        self.tabWidget_mc.setObjectName(u"tabWidget_mc")
        self.gridLayout_5 = QGridLayout(self.tabWidget_mc)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_mcserver_v = QPushButton(self.tabWidget_mc)
        self.pushButton_mcserver_v.setObjectName(u"pushButton_mcserver_v")
        self.pushButton_mcserver_v.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_v.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.pushButton_mcserver_v, 0, 0, 1, 1)

        self.pushButton_mcserver_mod = QPushButton(self.tabWidget_mc)
        self.pushButton_mcserver_mod.setObjectName(u"pushButton_mcserver_mod")
        self.pushButton_mcserver_mod.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_mod.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.pushButton_mcserver_mod, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tabWidget_mc, "")
        self.tabWidget_auto = QWidget()
        self.tabWidget_auto.setObjectName(u"tabWidget_auto")
        self.gridLayout_3 = QGridLayout(self.tabWidget_auto)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_autoInput = QPushButton(self.tabWidget_auto)
        self.pushButton_autoInput.setObjectName(u"pushButton_autoInput")
        self.pushButton_autoInput.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_autoInput, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWidget_auto, "")
        self.tabWidget_download = QWidget()
        self.tabWidget_download.setObjectName(u"tabWidget_download")
        self.gridLayout = QGridLayout(self.tabWidget_download)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_mcserver_v_download = QPushButton(self.tabWidget_download)
        self.pushButton_mcserver_v_download.setObjectName(u"pushButton_mcserver_v_download")
        self.pushButton_mcserver_v_download.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_v_download.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton_mcserver_v_download, 0, 1, 1, 1)

        self.pushButton_mcserver_mod_download = QPushButton(self.tabWidget_download)
        self.pushButton_mcserver_mod_download.setObjectName(u"pushButton_mcserver_mod_download")
        self.pushButton_mcserver_mod_download.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")
        self.pushButton_mcserver_mod_download.setAutoDefault(False)

        self.gridLayout.addWidget(self.pushButton_mcserver_mod_download, 0, 2, 1, 1)

        self.textBrowser_download = QTextBrowser(self.tabWidget_download)
        self.textBrowser_download.setObjectName(u"textBrowser_download")
        self.textBrowser_download.setStyleSheet(u"background-color: rgb(76, 76, 76);\n"
"color: rgb(0, 255, 0);\n"
"font: 9pt \"Impact\";")

        self.gridLayout.addWidget(self.textBrowser_download, 1, 1, 1, 2)

        self.tabWidget.addTab(self.tabWidget_download, "")
        self.tabWidget_setting = QWidget()
        self.tabWidget_setting.setObjectName(u"tabWidget_setting")
        self.gridLayout_2 = QGridLayout(self.tabWidget_setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_autostart = QCheckBox(self.tabWidget_setting)
        self.checkBox_autostart.setObjectName(u"checkBox_autostart")
        self.checkBox_autostart.setStyleSheet(u"font: 25 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"border:2px;\n"
"border-radius:10px;\n"
"\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.checkBox_autostart, 2, 1, 1, 1)

        self.pushButton_about = QPushButton(self.tabWidget_setting)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	color:white;\n"
"	background-color:rgb(14 , 150 , 254);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:white;\n"
"	background-color:rgb(44 , 137 , 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:white;\n"
"	background-color:rgb(14 , 135 , 228);\n"
"	padding-left:3px;\n"
"	padding-top:3px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.pushButton_about, 4, 2, 1, 1)

        self.label = QLabel(self.tabWidget_setting)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 25 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";")

        self.gridLayout_2.addWidget(self.label, 4, 4, 1, 1)

        self.checkBox_autoupdata = QCheckBox(self.tabWidget_setting)
        self.checkBox_autoupdata.setObjectName(u"checkBox_autoupdata")
        self.checkBox_autoupdata.setStyleSheet(u"font: 25 12pt \"\u5fae\u8f6f\u96c5\u9ed1 Light\";\n"
"border:2px;\n"
"border-radius:10px;\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.checkBox_autoupdata, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tabWidget_setting, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Window)

        self.tabWidget.setCurrentIndex(4)
        self.pushButton_mcserver_v.setDefault(False)
        self.pushButton_mcserver_mod.setDefault(False)
        self.pushButton_mcserver_v_download.setDefault(False)
        self.pushButton_mcserver_mod_download.setDefault(False)


        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"MoYu ToolBox \u6478\u9c7c\u5de5\u5177\u7bb1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_hub), QCoreApplication.translate("Window", u"HUB", None))
        self.pushButton_obs.setText(QCoreApplication.translate("Window", u"OBS", None))
        self.pushButton_androidtopc.setText(QCoreApplication.translate("Window", u"\u5b89\u5353\u6295\u5c4f", None))
        self.pushButton_liveass.setText(QCoreApplication.translate("Window", u"\u76f4\u64ad\u59ec", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_up), QCoreApplication.translate("Window", u"UP", None))
        self.pushButton_mcserver_v.setText(QCoreApplication.translate("Window", u"Minecraft\u670d\u52a1\u5668 [\u539f\u7248\u670d]", None))
        self.pushButton_mcserver_mod.setText(QCoreApplication.translate("Window", u"Minecraft\u670d\u52a1\u5668 [\u6a21\u7ec4\u670d]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_mc), QCoreApplication.translate("Window", u"MC", None))
        self.pushButton_autoInput.setText(QCoreApplication.translate("Window", u"AutoInput \u81ea\u52a8\u70b9\u51fb\u811a\u672c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_auto), QCoreApplication.translate("Window", u"Auto", None))
        self.pushButton_mcserver_v_download.setText(QCoreApplication.translate("Window", u"Minecraft\u670d\u52a1\u5668 [\u539f\u7248\u670d] \u5ba2\u6237\u7aef\u4e0b\u8f7d", None))
        self.pushButton_mcserver_mod_download.setText(QCoreApplication.translate("Window", u"Minecraft\u670d\u52a1\u5668 [\u6a21\u7ec4\u670d] \u5ba2\u6237\u7aef\u4e0b\u8f7d", None))
        self.textBrowser_download.setHtml(QCoreApplication.translate("Window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Impact'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:600; color:#00ff00;\">[MoYuStudio\u4e0b\u8f7d\u7cfb\u7edf]</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_download), QCoreApplication.translate("Window", u"Download", None))
        self.checkBox_autostart.setText(QCoreApplication.translate("Window", u"\u5f00\u673a\u81ea\u52a8\u542f\u52a8", None))
        self.pushButton_about.setText(QCoreApplication.translate("Window", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("Window", u"Copyright By WilsonVinson", None))
        self.checkBox_autoupdata.setText(QCoreApplication.translate("Window", u"\u81ea\u52a8\u66f4\u65b0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_setting), QCoreApplication.translate("Window", u"Setting", None))
    # retranslateUi

