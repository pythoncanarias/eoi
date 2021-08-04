import tkinter as tk
from tkinter import ttk

def di_hola():
    nombre = textbox.get()
    print("hola", nombre)
    print(textbox['text'])

root = tk.Tk()
root.config(width=350, height=250)
root.title("Aplicación de escritorio en Tcl/Tk")
frame = tk.Frame(root)
frame.place(x=0, y=0, width=350, height=250)
button = tk.Button(frame, text="Hola mundo!", command=di_hola)
button.place(x=50, y=50)
textbox = tk.Entry(frame)
textbox.insert(0, "Ingrese su nombre...")
textbox.place(x=50, y=100)
checkbox = ttk.Checkbutton(frame, text="Opción 1")
checkbox.place(x=50, y=150)
root.mainloop()


