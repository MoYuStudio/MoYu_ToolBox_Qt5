
# -*- coding: UTF-8 -*-

import os
import sys
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from .data import gui
from . import lanzoucloud_downloader

class GUI:
    def __init__(self):
        pass

    def mainloop(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        self.gui = gui.layout.Ui_Window()
        self.gui.setupUi(window)
        self.slot()
        window.show()
        sys.exit(app.exec_())

    def slot(self):
        # tabWidget MC
        self.gui.pushButton_mcserver_v.clicked.connect(self.print_coming_soon)
        self.gui.pushButton_mcserver_mod.clicked.connect(self.pushButton_mcserver_mod_clicked)

        # tabWidget Auto
        self.gui.pushButton_autoInput.clicked.connect(self.print_coming_soon)

        # tabWidget Download
        self.gui.pushButton_mcserver_v_download.clicked.connect(self.print_coming_soon)
        self.gui.pushButton_mcserver_mod_download.clicked.connect(self.pushButton_mcserver_mod_download_clicked)

        # tabWidget Setting
        self.gui.checkBox_autostart.clicked.connect(self.print_coming_soon)
        self.gui.checkBox_autoupdata.clicked.connect(self.print_coming_soon)
        self.gui.pushButton_about.clicked.connect(self.print_coming_soon)

    def print_coming_soon(self):
        print('coming soon')

    def pushButton_mcserver_mod_clicked(self):
        os.startfile(os.getcwd()+'/src/module/data/cloud_files/mc_server_mod/start.exe')

    def pushButton_mcserver_mod_download_clicked(self):

        def run_threading():
            dr = lanzoucloud_downloader.LanZouCloudDownloader()
            dr.download('mc_server_mod',self.textBrowser_download_print)
        
        thread = threading.Thread(target = run_threading,args= ())
        thread.start()

    def textBrowser_download_print(self,state,filename):
        self.gui.textBrowser_download.verticalScrollBar().setValue(self.gui.textBrowser_download.verticalScrollBar().maximum())
        if state == 'download':
            self.gui.textBrowser_download.append('下载 '+filename+' 成功')
        elif state == 'remove':
            self.gui.textBrowser_download.append('清理 '+filename+' 成功')
        elif state == 'done':
            self.gui.textBrowser_download.append(' ')
            self.gui.textBrowser_download.append('=== '+filename+' 下载成功 ===')
            self.gui.textBrowser_download.append(' ')
            self.gui.textBrowser_download.append(' ')
        self.gui.textBrowser_download.verticalScrollBar().setValue(self.gui.textBrowser_download.verticalScrollBar().maximum())

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
    
