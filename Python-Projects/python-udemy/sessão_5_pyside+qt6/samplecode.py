# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

#Hierarquia

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QMainWindow

app = QApplication(sys.argv) #Set the app instance
window = QMainWindow() #Create a main window
window.setWindowTitle("Janela =)")
central_widget = QWidget() #Create a central widget
window.setCentralWidget(central_widget) #Set the widget in to the window

botao = QPushButton('Botão') #Create a button with a text
botao.setStyleSheet('font-size: 40px;') #CSS of the button

botao1 = QPushButton('Botão 1') #Create a button with a text
botao2 = QPushButton('Botão 2') #Create a button with a text

# #Vertical layout using QVBoxLayout
# layout = QVBoxLayout() #Create a vertical layout
# window.setLayout(layout) #Setting the layout for the window
# layout.addWidget(botao) #Adding the button to the layout
# layout.addWidget(botao1)
# layout.addWidget(botao2)

# #Horizontal layout using QHBoxLayout
# layout = QHBoxLayout() #Create a Horizontal layout
# window.setLayout(layout) #Setting the layout for the window
# layout.addWidget(botao) #Adding the button to the layout
# layout.addWidget(botao1)
# layout.addWidget(botao2)

#Grid layout using QGridLayout
layout = QGridLayout() #Create a gridlayout layout
central_widget.setLayout(layout) #Setting the layout for the window
layout.addWidget(botao,1,1,1,1) #Adding the button to the layout with the position
layout.addWidget(botao1,1,2,1,1)
layout.addWidget(botao2,3,1,1,2) #ROW,COLUMN,ROWSPAN AND COLUMNSPAN

def print_123():
    print("123")

def changing_the_status_bar(status_bar):
    status_bar.showMessage('O meu slot foi executado')

def hello_world():
    print("Hello World")

#Using the main window we can add a menu
menu = window.menuBar()
menu_one = menu.addMenu("Sou um menu e sou clicavel")

funcao_menu = menu_one.addAction("Funcao do menu") #Create a function in the menu
funcao_menu.triggered.connect(lambda: changing_the_status_bar(status_bar)) #Create the function

funcao_menu = menu_one.addAction("Mais uma funcao para o menu")
funcao_menu.triggered.connect(hello_world)

funcao_menu = menu_one.addAction("Onde pode dois pode tres")
funcao_menu.triggered.connect(print_123)

#Using the main window we can add a StatusBar
status_bar = window.statusBar()
status_bar.showMessage("Sou uma barra de status =)")

window.show() #Showing the window

app.exec()  # O loop da aplicação