
import sys
from mywindow import UiMyWindow
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QApplication
import sys
from button import Button

class MyWindow(QMainWindow):
    def __init__(self, parent:QWidget | None=None, *args, **kwargs) -> None:
        super().__init__(parent, *args,**kwargs)
        self.setWindowTitle('Calculadora')
        self.setStyleSheet('border: blue')
        self.ui= UiMyWindow()
        self.ui.setup_ui(self)
        self.adjustfixedSize()


    def adjustfixedSize(self):
        self.adjustSize()
        self.setFixedSize(300, 370)
        
      
            


if __name__=='__main__':


    app= QApplication(sys.argv)

    window= MyWindow()

    window.show()
    app.exec()
   



