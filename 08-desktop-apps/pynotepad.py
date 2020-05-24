from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
app.setApplicationName("PyNotepad")
editor = QPlainTextEdit()
window = QMainWindow()
window.setWindowTitle("PyNotepad")
window.setCentralWidget(editor)

file_menu = window.menuBar().addMenu("&File")

def show_open_dialog():
    filename, _ = QFileDialog.getOpenFileName(window, 'Open...')
    if filename:
        file_contents = ""
        with open(filename, 'r') as f:
            file_contents = f.read()
        editor.setPlainText(file_contents)

open_action = QAction("&Open file...")
open_action.triggered.connect(show_open_dialog)
open_action.setShortcut(QKeySequence.Open)
file_menu.addAction(open_action)

def show_save_dialog():
    filename, _ = QFileDialog.getSaveFileName(window, 'Save as...')
    if filename:
        with open(filename, 'w') as f:
            f.write(editor.toPlainText())

save_action = QAction("&Save as...")
save_action.triggered.connect(show_save_dialog)
file_menu.addAction(save_action)

close_action = QAction("&Close")
close_action.triggered.connect(window.close)
file_menu.addAction(close_action)

def show_about_dialog():
    text = """
        <center>
            <h1>PyNotepad</h1><br/>
            <img src=logo.png width=200 height=200>
        </center>
        <p>Version 0.0.1</p>
    """
    QMessageBox.about(window, "About PyNotepad", text)


help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
about_action.triggered.connect(show_about_dialog)
help_menu.addAction(about_action)

window.show()
app.exec()
