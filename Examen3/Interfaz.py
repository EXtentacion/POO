from Ctabla import *
from tkinter import *


interfazC = control()

Ventana = Tk()
Ventana.title("Banco")
Ventana.geometry("420x300")
Ventana.config(bg="lightblue")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")


pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)


panel.add(pestana1, text="Crear")
panel.add(pestana2, text="Leer")
panel.add(pestana3, text="Actualizar")


#Pestaña 1

Label(pestana1, text="NoCuenta: ").grid(row=0, column=0, padx=10, pady=10)
Label(pestana1, text="Saldo: ").grid(row=1, column=0, padx=10, pady=10)

NoCuenta = StringVar()
Saldo = StringVar()


Entry(pestana1, textvariable=NoCuenta).grid(row=0, column=1, padx=10, pady=10)
Entry(pestana1, textvariable=Saldo).grid(row=1, column=1, padx=10, pady=10)

def crear():
    interfazC.insertarbase(NoCuenta.get(), Saldo.get())

    
Button(pestana1, text="Crear", command=crear).grid(row=2, column=1, padx=10, pady=10)

#Pestaña 2

Label(pestana2, text="NoCuenta: ").grid(row=0, column=0, padx=10, pady=10)
Label(pestana2, text="Saldo: ").grid(row=1, column=0, padx=10, pady=10)

NoCuenta = StringVar()

Saldo = StringVar()


Entry(pestana2, textvariable=NoCuenta).grid(row=0, column=1, padx=10, pady=10)

def leer():
    datos = interfazC.leerbase(NoCuenta.get())
    Saldo.set(datos[0][1])
    
Button(pestana2, text="Leer", command=leer).grid(row=2, column=1, padx=10, pady=10)

Entry(pestana2, textvariable=Saldo).grid(row=1, column=1, padx=10, pady=10)

#Pestaña 3

Label(pestana3, text="NoCuenta: ").grid(row=0, column=0, padx=10, pady=10)
Label(pestana3, text="Saldo: ").grid(row=1, column=0, padx=10, pady=10)

NoCuenta = StringVar()

Saldo = StringVar()


Entry(pestana3, textvariable=NoCuenta).grid(row=0, column=1, padx=10, pady=10)
Entry(pestana3, textvariable=Saldo).grid(row=1, column=1, padx=10, pady=10)

def actualizar():
    
    interfazC.actualizarbase(NoCuenta.get(), Saldo.get())
    
    NoCuenta.set("")
    
    Saldo.set("")
    
Button(pestana3, text="Actualizar", command=actualizar).grid(row=2, column=1, padx=10, pady=10)

Ventana.mainloop()

