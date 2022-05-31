
# -*- coding: UTF-8 -*-
 
import sys
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import data.gui
import anonfiles_downloader

class GUI:
    def __init__(self):
        pass

    def mainloop(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        self.gui = data.gui.layout.Ui_Window()
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

        # tabWidget Setting
        self.gui.checkBox_autostart.clicked.connect(self.print_coming_soon)
        self.gui.checkBox_autoupdata.clicked.connect(self.print_coming_soon)
        self.gui.pushButton_about.clicked.connect(self.print_coming_soon)

    def print_coming_soon(self):
        print('coming soon')

    def pushButton_mcserver_mod_clicked(self):

        def run():
            ad = anonfiles_downloader.AnonfilesDownloader('mc_server_mod.zip','src/module/data/cloud_files','https://anonfiles.com/Xbj9F3lay4/mc_server_mod_zip')
            ad.download()
        thread = threading.Thread(target = run,
                        args= ()
                        )
        thread.start()

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
    
