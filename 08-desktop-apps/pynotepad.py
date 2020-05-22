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
