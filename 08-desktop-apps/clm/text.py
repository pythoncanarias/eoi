import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

file_path = None

app = QApplication([])
app.setApplicationName("CLM Pad")

def dialogo_confirmacion():
    return QMessageBox.question(
        window, "Confirmación",
        "Tienes cambios sin guardar. Estás segur@?",
        QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
        QMessageBox.Save)

def save_if_modified():
    if text.document().isModified():
        answer = dialogo_confirmacion()
        if answer == QMessageBox.Save:
            guardar()
            return False
        elif answer == QMessageBox.Cancel:
            return False
    return True


class MyMainWindow(QMainWindow):
    def closeEvent(self, evt):
        if text.document().isModified():
            answer = dialogo_confirmacion()
            if answer == QMessageBox.Save:
                guardar()
            elif answer == QMessageBox.Cancel:
                evt.ignore()

text = QPlainTextEdit()
window = MyMainWindow()
window.setCentralWidget(text)
barra_de_menus = window.menuBar()

menu_archivo = barra_de_menus.addMenu("&Archivo")

def nuevo():
    global file_path
    if save_if_modified():
        text.clear()
        file_path = None

accion_nuevo = QAction("&Nuevo")
accion_nuevo.setShortcut(QKeySequence.New)
accion_nuevo.triggered.connect(nuevo)
menu_archivo.addAction(accion_nuevo)

def mostrar_dialogo_abrir():
    global file_path
    if not save_if_modified():
        return
    filename, _ = QFileDialog.getOpenFileName(window,
                    "Abrir fichero...",
                    os.getcwd(),
                    "Ficheros de texto (*.txt *.py)"
                  )
    if filename:
        with open(filename, 'r') as f:
            text.setPlainText(f.read())
        file_path = filename

accion_abrir = QAction("&Abrir")
accion_abrir.setShortcut(QKeySequence.Open)
accion_abrir.triggered.connect(mostrar_dialogo_abrir)
menu_archivo.addAction(accion_abrir)

def guardar():
    if file_path:
        with open(file_path, 'w') as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
        print(text.document().isModified())
    else:
        mostrar_dialogo_guardar()

def mostrar_dialogo_guardar():
    global file_path
    filename, _ = QFileDialog.getSaveFileName(window,
                    "Guardar fichero...",
                    os.getcwd(),
                    "Ficheros de texto (*.txt *.py)"
                  )
    if filename: 
        with open(filename, 'w') as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
        print(text.document().isModified())
        file_path = filename

accion_guardar = QAction("&Guardar")
accion_guardar.setShortcut(QKeySequence.Save)
accion_guardar.triggered.connect(guardar)
menu_archivo.addAction(accion_guardar)

accion_guardar_como = QAction("G&uardar como...")
accion_guardar_como.setShortcut(QKeySequence.SaveAs)
accion_guardar_como.triggered.connect(mostrar_dialogo_guardar)
menu_archivo.addAction(accion_guardar_como)

accion_cerrar = QAction("&Cerrar")
accion_cerrar.triggered.connect(window.close)
menu_archivo.addAction(accion_cerrar)

def mostrar_dialogo_acercade():
    text = """
       <center>
         <h2>CLM Pad</h2><br/>
         <img src="data:image/png;base64,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">
       </center>
       <h4>Version 0.0.2</h4>
       <p>Copyright Pepe</p>
    """
    QMessageBox.about(window, "Acerca de CLM Pad...", text)

menu_ayuda = barra_de_menus.addMenu('&Ayuda')
acerca_de = QAction('Acerca de...')
acerca_de.triggered.connect(mostrar_dialogo_acercade)
menu_ayuda.addAction(acerca_de)

window.show()
app.exec()