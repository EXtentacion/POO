from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana = Tk()
Ventana.title("Usuarios")
Ventana.geometry("700x500")
Ventana.resizable(0,0)

# Crear Tabla

panel = ttk.Notebook(Ventana)
panel.pack(fill = "both", expand = "yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)



panel.add(pestana1, text = "Formulario usuarios")
panel.add(pestana2, text = "Buscar Usuarios")
panel.add(pestana3, text = "Consultar usuarios")
panel.add(pestana4, text = "Actualizar usuarios")

titulo = Label(pestana1, text = "Formulario de usuarios", font = ("Arial", 20)).place(x = 200, y = 20)
varNombre = StringVar()
nombre = Label(pestana1, text = "Nombre: ", font = ("Arial", 12)).place(x = 20, y = 100)
txtNombre = Entry(pestana1, textvariable = varNombre, font = ("Arial", 12)).place(x = 100, y = 100)
varContrasena = StringVar()
contrasena = Label(pestana1, text = "Contraseña: ", font = ("Arial", 12)).place(x = 20, y = 150)
txtContrasena = Entry(pestana1, textvariable = varContrasena, font = ("Arial", 12)).place(x = 100, y = 150)
varCorreo = StringVar()
correo = Label(pestana1, text = "Correo: ", font = ("Arial", 12)).place(x = 20, y = 200)
txtCorreo = Entry(pestana1, textvariable = varCorreo, font = ("Arial", 12)).place(x = 100, y = 200)
boton = Button(pestana1, text = "Guardar", font = ("Arial", 12)).place(x = 20, y = 250)

titulo2 = Label(pestana2, text = "Buscar usuarios", font = ("Arial", 20)).place(x = 200, y = 20)
varBuscar = StringVar()
buscar = Label(pestana2, text = "Buscar: ", font = ("Arial", 12)).place(x = 20, y = 100)
txtBuscar = Entry(pestana2, textvariable = varBuscar, font = ("Arial", 12)).place(x = 100, y = 100)
boton2 = Button(pestana2, text = "Buscar", font = ("Arial", 12)).place(x = 20, y = 150)


titulo3 = Label(pestana3, text = "Consultar usuarios", font = ("Arial", 20)).place(x = 200, y = 20)
cosultar = Label(pestana3, text = "Consultar: ", font = ("Arial", 12)).place(x = 20, y = 100)
txtconsultar = Entry(pestana3, textvariable = varBuscar, font = ("Arial", 12)).place(x = 100, y = 100)
boton3 = Button(pestana3, text = "Consultar", font = ("Arial", 12)).place(x = 20, y = 150)


titulo4 = Label(pestana4, text = "Actualizar usuarios", font = ("Arial", 20)).place(x = 200, y = 20)
varActualizar = StringVar()
actualizar = Label(pestana4, text = "Actualizar: ", font = ("Arial", 12)).place(x = 20, y = 100)
txtActualizar = Entry(pestana4, textvariable = varActualizar, font = ("Arial", 12)).place(x = 100, y = 100)
boton4 = Button(pestana4, text = "Actualizar", font = ("Arial", 12)).place(x = 20, y = 150)





Ventana.mainloop()







