from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

gui = Tk()
gui.geometry('700x800') # anchura x altura
gui.configure(bg = 'beige')
gui.title('Ejemplo grids')

Btn_salir = ttk.Button(gui, text='Salir', command=quit)
Btn_salir.grid(column=1, row=1)

etiqueta = ttk.Label(gui, text ="Hola Mundo")
etiqueta.grid(column=0,row=0)

etiqueta_2 = ttk.Label(gui, text="De Python")
etiqueta_2.grid(column=1, row=0)


gui.mainloop()