# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\module\data\gui\layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(700, 400)
        self.frame = QtWidgets.QFrame(Window)
        self.frame.setGeometry(QtCore.QRect(20, 20, 651, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(460, 310, 151, 31))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(600, 10, 37, 31))
        self.toolButton.setObjectName("toolButton")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 551, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.mc = QtWidgets.QWidget()
        self.mc.setObjectName("mc")
        self.pushButton_MCServerV = QtWidgets.QPushButton(self.mc)
        self.pushButton_MCServerV.setGeometry(QtCore.QRect(20, 30, 281, 91))
        self.pushButton_MCServerV.setAutoDefault(False)
        self.pushButton_MCServerV.setDefault(False)
        self.pushButton_MCServerV.setObjectName("pushButton_MCServerV")
        self.pushButton_MCServerM = QtWidgets.QPushButton(self.mc)
        self.pushButton_MCServerM.setGeometry(QtCore.QRect(20, 130, 281, 91))
        self.pushButton_MCServerM.setAutoDefault(False)
        self.pushButton_MCServerM.setDefault(False)
        self.pushButton_MCServerM.setObjectName("pushButton_MCServerM")
        self.tabWidget.addTab(self.mc, "")
        self.auto_2 = QtWidgets.QWidget()
        self.auto_2.setObjectName("auto_2")
        self.pushButton_AutoInput = QtWidgets.QPushButton(self.auto_2)
        self.pushButton_AutoInput.setGeometry(QtCore.QRect(110, 50, 171, 71))
        self.pushButton_AutoInput.setObjectName("pushButton_AutoInput")
        self.tabWidget.addTab(self.auto_2, "")

        self.retranslateUi(Window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MoYu ToolBox 摸鱼工具箱"))
        self.label.setText(_translate("Window", "Copyright By WilsonVinson"))
        self.toolButton.setText(_translate("Window", "..."))
        self.pushButton_MCServerV.setText(_translate("Window", "Minecraft服务器 [原版服] 客户端下载"))
        self.pushButton_MCServerM.setText(_translate("Window", "Minecraft服务器 [模组服] 客户端下载"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mc), _translate("Window", "MC"))
        self.pushButton_AutoInput.setText(_translate("Window", "AutoInput 自动点击脚本"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.auto_2), _translate("Window", "Auto"))