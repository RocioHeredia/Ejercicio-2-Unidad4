from tkinter import *
from tkinter import ttk, font, messagebox
import tkinter as tk


class AplicacionIva():
    __ventana = None
    __precio_base = None
    __iva = None
    __precio_con_iva = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('250x250')
        self.__ventana.title('Calculo de IVA')
        self.__ventana.configure(bg='white')
        mainframe = ttk.Frame(self.__ventana, padding='4 5 12 4')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        fuente = font.Font(font='Verdana 10', weight='normal')
        self.valorIVA = tk.IntVar()
        self.__precio_base = StringVar()
        self.__precio_con_iva = StringVar()
        self.__iva = StringVar()
        #Titulo de calculo y definicion de para ingresar el precio base
        label_titulo = ttk.Label(mainframe, text='Calculo de Iva', background='light blue')
        label_titulo.grid(column=1, row=0, columnspan=2, sticky=N)
        ttk.Label(mainframe, text='Precio sin IVA').grid(column=1, row=2)
        self.preciobaseEntry = ttk.Entry(mainframe, width=15, textvariable=self.__precio_base)
        self.preciobaseEntry.grid(column=2, row=2)
        #Cuadro para la eleccion de porcentaje de iva
        labelFrameSeleccione = tk.LabelFrame(mainframe, text='Seleccione:', font=fuente)
        labelFrameSeleccione.grid(column=1, row=3, sticky=W)
        ttk.Radiobutton(labelFrameSeleccione, text='Iva 21%', value=0, variable=self.valorIVA, command=self.cambiaiva).grid(row=2, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(labelFrameSeleccione, text='Iva 10.5%', value=1, variable=self.valorIVA, command=self.cambiaiva).grid(row=3, column=0, columnspan=1, sticky='w')
        #Mostrar los datos de los iva y precio con iva
        ttk.Label(mainframe, text='IVA').grid(column=1, row=4)
        ttk.Label(mainframe, textvariable=self.__iva).grid(column=2,row=4, sticky=W)
        ttk.Label(mainframe, text='Precio con Iva').grid(column=1, row=5)
        ttk.Label(mainframe, textvariable=self.__precio_con_iva).grid(column=2, row=5, sticky=W)
        #Botones de calcular y salir
        ttk.Button(mainframe, text='Calcular', command=self.calcular).grid(column=1, row=6, sticky=E)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=2, row=6, sticky=E)
        #Separa cada objeto de la ventana
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.__ventana.mainloop()

    def cambiaiva(self):
        if self.valorIVA.get() == 0:
            self.__iva.set(21)
        else:
            if self.valorIVA.get() == 1:
                self.__iva.set(10.5)

    def calcular(self):
        try:
            monto = float(self.preciobaseEntry.get())
            iva = float(self.__iva.get())
            precioconiva = monto * (iva/100)
            self.__precio_con_iva.set(str(precioconiva))
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')


def testapp():
    mi_app = AplicacionIva()


if __name__ == '__main__':
    testapp()
