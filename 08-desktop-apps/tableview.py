import csv
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import (
        Qt, QAbstractTableModel, QVariant)

file_name = "datos.csv"
headers = None
rows = None
with open(file_name, 'r') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
    headers = data[0]
    rows = data[1:]

class MyTableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)

    def columnCount(self, parent):
        return len(headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return headers[section]

def on_cell_clicked(index):
    print("clicked", index.row(), index.column())

def on_cell_entered(index):
    print("entered", index.row(), index.column())

def on_cell_pressed(index):
    print("pressed", index.row(), index.column())

app = QApplication([])
model = MyTableModel()
view = QTableView()
view.setModel(model)
view.clicked.connect(on_cell_clicked)
view.pressed.connect(on_cell_pressed)
view.entered.connect(on_cell_entered)
view.show()
app.exec()
