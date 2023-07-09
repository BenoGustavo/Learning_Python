from PySide6.QtWidgets import QPushButton,QGridLayout
from PySide6.QtCore import Slot
from paths import MEDIUM_FONT_SIZE
from utils import IsNumOrDot, isEmpty, isValidNumber
from display import Display

class Button(QPushButton):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75,75)

class ButtonGrid(QGridLayout):
    def __init__(self,display: Display,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self._gridMask = [
            ['C','⌫','^','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['', '0','.','='],
        ]

        self.display = display

        self._makeGrid
    
    def _makeGrid(self):
        for line,row in enumerate(self._gridMask):
            for column,button_text in enumerate(row):
                
                button = Button(button_text)

                if not button_text in '1234567890.':
                    button.setProperty('cssClass','specialButton')

                self.addWidget(button,line,column)

                buttonSlot = self._makeButtonDisplaySlot(self._insertContentIntoDisplay,button,)
                button.clicked.connect(buttonSlot)
    

    def _makeButtonDisplaySlot(self,method,*args,**kwargs):
        @Slot(bool)
        def realSlot():
            method(*args,**kwargs)
        return realSlot

    def _insertContentIntoDisplay(self,button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

