from PyQt5 import uic
from PyQt5.QtWidgets import *

Form, Win = uic.loadUiType("./dialog.ui")

app = QApplication([])
win = Win()
form = Form()

form.setupUi(win)
win.show()
app.exec()
