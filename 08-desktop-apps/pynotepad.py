from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])
app.setApplicationName("PyNotepad")
editor = QPlainTextEdit()
window = QMainWindow()
window.setWindowTitle("PyNotepad")
window.setCentralWidget(editor)

file_menu = window.menuBar().addMenu("&File")
file_path = None

def show_open_dialog():
    global file_path
    filename, _ = QFileDialog.getOpenFileName(window, 'Open...')
    if filename:
        file_contents = ""
        with open(filename, 'r') as f:
            file_contents = f.read()
        editor.setPlainText(file_contents)
        file_path = filename

open_action = QAction("&Open file...")
open_action.triggered.connect(show_open_dialog)
# open_action.hovered.connect(lambda : print("me han hovereado"))
open_action.setShortcut(QKeySequence.Open)
file_menu.addAction(open_action)

def save():
    if file_path is None:
        show_save_dialog()
    else:
        with open(file_path, 'w') as f:
            f.write(editor.toPlainText())

def show_save_dialog():
    global file_path
    filename, _ = QFileDialog.getSaveFileName(window, 'Save as...')
    if filename:
        file_path = filename
        save()

save_action = QAction("&Save")
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
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
