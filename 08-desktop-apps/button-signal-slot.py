from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('click aqui')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('has hecho click')
    alert.exec()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()
