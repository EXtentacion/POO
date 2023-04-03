from tkinter import *
from tkinter import ttk
from ControladorBD import *

interfazC = controlador()


Ventana = Tk()
Ventana.title("Usuarios")
Ventana.geometry("420x300")
Ventana.config(bg="lightblue")

panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")


pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)



panel.add(pestana1, text="Crear")
panel.add(pestana2, text="Leer")
panel.add(pestana3, text="Actualizar")
panel.add(pestana4, text="Eliminar")


#Pestaña 1

Label(pestana1, text="Nombre: ").grid(row=0, column=0, padx=10, pady=10)
Label(pestana1, text="Apellido: ").grid(row=1, column=0, padx=10, pady=10)
Label(pestana1, text="Correo: ").grid(row=2, column=0, padx=10, pady=10)
Label(pestana1, text="Contraseña: ").grid(row=3, column=0, padx=10, pady=10)

nombre = StringVar()
apellido = StringVar()
correo = StringVar()
contraseña = StringVar()


Entry(pestana1, textvariable=nombre).grid(row=0, column=1, padx=10, pady=10)
Entry(pestana1, textvariable=apellido).grid(row=1, column=1, padx=10, pady=10)
Entry(pestana1, textvariable=correo).grid(row=2, column=1, padx=10, pady=10)
Entry(pestana1, textvariable=contraseña, show="*").grid(row=3, column=1, padx=10, pady=10)

def crear():
    
    interfazC.insertarUsuarios(nombre.get(), apellido.get(), correo.get(), contraseña.get())
    
    nombre.set("")
    apellido.set("")
    correo.set("")
    contraseña.set("")
    
Button(pestana1, text="Crear", command=crear).grid(row=4, column=0, padx=10, pady=10)




#Pestaña 2

#pedir id y buscar por usuario 


#Leer todos los datos de la tabla

def leer():
    usuarios = interfazC.leerUsuarios()
    for usuario in usuarios:
        tree.insert("", 0, text=usuario[0], values=(usuario[1], usuario[2], usuario[3], usuario[4]))
    
tree = ttk.Treeview(pestana2, height=10, columns=("#0", "#1", "#2", "#3"))

tree.heading("#0", text="id")
tree.heading("#1", text="nombre")
tree.heading("#2", text="apellido")
tree.heading("#3", text="correo")
tree.heading("#4", text="contraseña")


tree.grid(row=0, column=0, padx=10, pady=10)

#FUNCION PARA QUE NO SE REPITAN LOS DATOS AL LEER AUTOMATICAMENTE


def limpiar():
    registros = tree.get_children()
    for registro in registros:
        tree.delete(registro)
        
Button(pestana2, text="Leer", command=leer).grid(row=1, column=0, padx=10, pady=10)
Button(pestana2, text="Limpiar", command=limpiar).grid(row=2, column=0, padx=10, pady=10)





#Pestaña 3

Label(pestana3, text="ID: ").grid(row=0, column=0, padx=10, pady=10)
Label(pestana3, text="Nombre: ").grid(row=1, column=0, padx=10, pady=10)
Label(pestana3, text="Apellido: ").grid(row=2, column=0, padx=10, pady=10)
Label(pestana3, text="Correo: ").grid(row=3, column=0, padx=10, pady=10)
Label(pestana3, text="Contraseña: ").grid(row=4, column=0, padx=10, pady=10)

id = StringVar()


Entry(pestana3, textvariable=id).grid(row=0, column=1, padx=10, pady=10)

Entry(pestana3, textvariable=nombre).grid(row=1, column=1, padx=10, pady=10)

Entry(pestana3, textvariable=apellido).grid(row=2, column=1, padx=10, pady=10)

Entry(pestana3, textvariable=correo).grid(row=3, column=1, padx=10, pady=10)

Entry(pestana3, textvariable=contraseña, show="*").grid(row=4, column=1, padx=10, pady=10)

def actualizar():
    interfazC.actualizarUsuarios(id.get(), nombre.get(), apellido.get(), correo.get(), contraseña.get())
    id.set("")
    nombre.set("")
    apellido.set("")
    correo.set("")
    contraseña.set("")
    
Button(pestana3, text="Actualizar", command=actualizar).grid(row=5, column=1, padx=10, pady=10)

#Pestaña 4

Label(pestana4, text="ID: ").grid(row=0, column=0, padx=10, pady=10)

id = StringVar()

Entry(pestana4, textvariable=id).grid(row=0, column=1, padx=10, pady=10)

def eliminar():
    interfazC.eliminarUsuarios(id.get())
    id.set("")
    
Button(pestana4, text="Eliminar", command=eliminar).grid(row=1, column=1, padx=10, pady=10)

Ventana.mainloop()


