
# -*- coding: UTF-8 -*-
 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import data.gui

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
        self.gui.pushButton_MCServerV.clicked.connect(self.print_click)
        self.gui.pushButton_MCServerM.clicked.connect(self.print_click)

        self.gui.pushButton_AutoInput.clicked.connect(self.print_click)

    def print_click(self):
        print('click')

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
