from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget,QFrame,QPushButton
import sys
from mywindow import UiMyWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Button(UiMyWindow):
    def __init__(self):
        super().__init__()

        self.cal=[
            '7','8','9',
            '4','5','6',
            '1','2','3'
        ]
    
    
        for i in self.cal:
            i = QPushButton(self.gridLayoutWidget)
            
            i.setEnabled(True)
            i.setMaximumSize(QtCore.QSize(60, 40))
            i.setLayoutDirection(QtCore.Qt.LeftToRight)
            i.setText("")
            i.setObjectName("pushButton_4")
          

