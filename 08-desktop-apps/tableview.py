import csv
import sys
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

selected_origin = [0,0]

def on_cell_pressed(index):
    global selected_origin
    selected_origin[0] = index.row()
    selected_origin[1] = index.column()

def on_cell_entered(index):
    global selected_origin
    x = sorted((selected_origin[0], index.row()))
    y = sorted((selected_origin[1], index.column()))
    data_array = [x[0],y[0]],[x[1],y[1]]
    print(data_array)
    return data_array

def extract_data():
    indexes = view.selectedIndexes()
    for index in indexes:
        print(index.data())

app = QApplication([])
model = MyTableModel()
view = QTableView()
view.setModel(model)
view.pressed.connect(on_cell_pressed)
view.entered.connect(on_cell_entered)
button = QPushButton("Extract data")
button.clicked.connect(extract_data)

window = QWidget()
layout = QVBoxLayout()
layout.addWidget(view)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec()
