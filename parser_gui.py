import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from graphviz import Digraph

import scanner
import my_parser
dot = Digraph()   # Directed graph
dot.format = 'png'  # Output format
MainUI, _ = loadUiType('parser.ui')

class Main(QMainWindow, MainUI):
    def __init__(self):
        super().__init__()
        self.title = "Parser"
        self.setupUi(self)
        self.Hanlde_Buttons()
        self.tabWidget.tabBar().setVisible(False)

    def Hanlde_Buttons(self):
        self.pushButton_3.clicked.connect(self.scan)
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.parser)

    def scan(self):
        input_text = self.textEdit_2.toPlainText()
        if(input_text==''):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setInformativeText('Please Enter Text!')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            scanner.scanner_file()
            file1 = open("sample_code.txt", "w")
            file1.write(input_text)

    def parser(self):
        #import my_parser
        my_parser.parser_file()

    def clear(self):
        self.textEdit_2.setPlainText('')
        #os.remove('image.png')
        #os.remove('image')
        #os.remove('TokensTable.txt')


    def msg(self,index):
        print("ok")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText("can't match mul-operator, line no. #", index)
        msg.setWindowTitle("Error")
        msg.exec_()
        if (QMessageBox.Yes):
            self.clear()
            # self.tabWidget.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()




if __name__ == '__main__':
    main()
