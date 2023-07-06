import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    test_label = QLabel('Testing label')
    test_label.setStyleSheet('font-size: 150px')
    window.Vlayout.addWidget(test_label)
    
    window.AdjustFixedSize()
    window.show()
    app.exec()