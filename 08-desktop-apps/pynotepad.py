from PyQt5.QtWidgets import *

app = QApplication([])
app.setApplicationName("PyNotepad")
editor = QPlainTextEdit()
window = QMainWindow()
window.setWindowTitle("PyNotepad")
window.setCentralWidget(editor)

file_menu = window.menuBar().addMenu("&File")
close_action = QAction("&Close")
close_action.triggered.connect(window.close)
file_menu.addAction(close_action)

window.show()
app.exec()
