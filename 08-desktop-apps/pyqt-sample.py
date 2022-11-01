import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize    
     
class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world") 
        
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
 
        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  
 
        title = QLabel("Hello World from PyQt", self) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)
 
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
