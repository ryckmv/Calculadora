from PyQt5.QtWidgets import QGridLayout, QWidget,QPushButton,QLineEdit,QGraphicsDropShadowEffect
import sys
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QKeyEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from utils  import isValidNumber, isnumordot,isempty

class UiMyWindow(object):
    

    def setup_ui(self, parent):
        self.operato=None
        self.left=None
        self.right=None
        self.result=None
        self.sol=True
        # Central Widget
        self.centralwidget = QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.layout =  QGridLayout(self.centralwidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.display_= Display()
        
        self.layout.addWidget(self.display_, 0, 0, 1, 3)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        

        

        self.layout_buttons = QGridLayout(self.gridLayoutWidget)
        self.layout_buttons.setSpacing(0)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.gridLayoutWidget, 1, 0, 1, 3)

        self.configButton()
        self.configSignal()
        

        
        parent.setCentralWidget(self.centralwidget)
   
    def stylebutton(self,button):
        qss=f"""
            QPushButton{{
               
              font-size: 25px; background-color:#E0E0E0;
                
                border: 2px solid #404040 ; 
                padding: 10px
            }}
            QPushButton:hover{{
             font-size: 30px; background-color:#323232; 
                
                 border-width: 2px; border-color:#a0a0a0
            }}
             QPushButton:pressed {{
           font-size: 25px; background-color:#038C3E; 
                 
                 border-width: 6px; border-color:#02735E
         }}
           """
        qss2=f"""
            QPushButton{{
                font-size: 25px; background-color:#262626;
                
                border: 2px solid #C0C0C0 ; 
                padding: 10px
                 
                 }}
            QPushButton:hover{{
             font-size: 30px; background-color:#E0E0E0; 
                border-style: outset; 
                 border-width: 2px; border-color:#a0a0a0
            }}
             QPushButton:pressed {{
           font-size: 25px; background-color:#038C3E; 
                border-style: outset; 
                 border-width: 6px; border-color:#02735E
         }}
           """
        sombra= QGraphicsDropShadowEffect()
        sombra.setBlurRadius(7)
        sombra.setXOffset(7)
        sombra.setYOffset(7)
        sombra.setColor(QtGui.QColor(0,0,0,160))
        button.setGraphicsEffect(sombra)
        n=button.text()
        if isnumordot(n):
             button.setStyleSheet(qss)
        else:
             button.setStyleSheet(qss2)

 
        
    def configSignal(self):
        self.display_.enterPressed.connect(self.equacao)
        self.display_.backpressed.connect(self._backSpace)
        self.display_.clearpressed.connect(self.clear)
        self.display_.oppressed.connect(self.op_)
        self.display_.inputpressed.connect(self.presedInsertDisplay)
        
        
    def configButton(self):
       
        
        self.cal=[
            
            ['C','%', '^', '/'],
            ['7','8', '9', '*'],
            ['4','5', '6', '-'],
            ['1','2', '3', '+'],
            ['N', '0', '.', '='],
        ]
        
        
        for i,row in enumerate (self.cal):
            for j,text in enumerate(row):

                
                button = QPushButton(text)
                button.setMinimumSize(60,50)
                button.setMaximumSize(60,50)
        
                self.stylebutton(button)
                
                self.layout_buttons.addWidget(button,i,j)
                slot=self.Clicked(self.presedInsertDisplay,text)
                self.connectButtonClicked(button,slot)
                
                
         
    def Clicked(self,fun,*args,**kwargs):
        def realslot():
            fun(*args,**kwargs)
        return realslot
    
    def connectButtonClicked(self,button,slot):
           button.clicked.connect(slot)

    
    def op_(self,text):

        if not isValidNumber(self.display_.text()) and self.left is None:
                print('Não há calculos para fazer')
                return
            
        self.operato=text
        self.left = self.display_.text()
        self.display_.clear()
              
       
    def presedInsertDisplay(self,text):
       
        if isnumordot(text):
            self.display_.insert(text)
       
        self.op= ['+', '-', '*', '/', '^','%']
        if text  in self.op:
            self.op_(text)
          
        
        if text =='=':
            self.equacao()
            
        if 'N' in text:
            self.isNegative()
        if 'C' in text:
            self.clear()

    def _backSpace(self):
        self.display_.backspace()
        self.display_.setFocus()


    def isNegative(self):
          displaytext= self.display_.text() 
          if not isValidNumber(displaytext):
            return
          number= float(displaytext)
          number1=-number
          self.display_.setText(str(number1))
          self.display_.setFocus()
         
            
    def clear(self):
         self.display_.clear()
         self.left=None
         self.right=None
         self.display_.setFocus()
             

    def equacao(self):
        if not isValidNumber(self.display_.text()) and self.left is None:
                print('Não há calculos para fazer')
                return
        
           
        self.right=  self.display_.text()
        
        if self.operato=='+':
            self.result= float(self.left)+float(self.right)
            
            self.display_.setText(str(self.result))
        if self.operato=='-':
            self.result= float(self.left)-float(self.right)
            self.display_.setText(str(self.result))
            print(self.result)
        if self.operato=='*':
            self.result= float(self.left)*float(self.right)
            self.display_.setText(str(self.result))
            print(self.result)
        if self.operato=='/':
            self.result= float(self.left)/float(self.right)
            self.display_.setText(str(self.result))
            print(self.result)
        if self.operato=='%':
            self.result= (float(self.left)/float(100))*float(self.right)
            self.display_.setText(str(self.result))
            print(self.result)
        
        self.left=self.result
        print(self.left)
        
        self.display_.setFocus()
        
        
        

        
class Display(QLineEdit):
    enterPressed=pyqtSignal()
    backpressed=pyqtSignal()
    clearpressed=pyqtSignal()
    inputpressed= pyqtSignal(str)
    oppressed= pyqtSignal(str)



    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.confistyle()
        


    def confistyle(self):
        
        MARGIN=5
        MEDIUM_SIZER=40
        MINIMUN_WIDTH=10
        margin=[MARGIN for m in  range(4)]
        self.setStyleSheet('font-size: 40px; background-color: #0e0e0e; color: white;border: 2px solid gray;')
        self.setMinimumHeight(MEDIUM_SIZER*2)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margin)
        self.setMinimumWidth(MINIMUN_WIDTH)
    
    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        key=event.key()
        text=event.text().strip()

        KEYS=Qt.Key
        isenter= key in [KEYS.Key_Enter, KEYS.Key_Return]
        isbackSpace=key in[KEYS.Key_Delete, KEYS.Key_Backspace]
        isesc=key in[KEYS.Key_Escape]
        isoperator= key in[KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,KEYS.Key_P]
       
        
        if isenter:
            self.enterPressed.emit()
            return event.ignore()
        
        if isbackSpace:
            self.backpressed.emit()
            return event.ignore()
        
        if isesc:
            self.clearpressed.emit()
            return event.ignore()
        
        if isoperator:
            self.oppressed.emit(text)
            return event.ignore()
        
        if isempty(text):

            return event.ignore()
        
        if isnumordot(text):
        
            self.inputpressed.emit(text)
            return event.ignore()
     


        