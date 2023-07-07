import sys

from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from display import Display

from paths import WINDOW_ICON_PATH

from main_window import MainWindow

if __name__ == "__main__":
    
    #Creating the app
    app = QApplication(sys.argv)
    window = MainWindow()
    
    #Adding an icon to the app
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    display = Display()
    display.setPlaceholderText("I'm ready to calculate") #Setting a place holder text into the textbox
    window.addToVLayout(display) #Adding the text box to the layout

    #Remove the permission to resize the window
    window.AdjustFixedSize()
    window.show()
    app.exec()