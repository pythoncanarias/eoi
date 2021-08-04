import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.config(width=350, height=250)
root.title("TK/inter Aplicación de escritorio")
frame = tk.Frame(root)
frame.place(x=0, y=0, width=350, height=250)
button = tk.Button(frame, text="Hola mundo!")
button.place(x=50, y=50)
root.mainloop()
