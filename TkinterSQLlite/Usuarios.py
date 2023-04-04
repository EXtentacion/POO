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
pestana5 = ttk.Frame(panel)



panel.add(pestana1, text="Crear")
panel.add(pestana5, text="Buscar")
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




#Pestana 5

#Buscar un usuario en especifico y mostrar sus datos nombre,apellido,correo,contraseña



id_var =StringVar()
nombre_var =StringVar()
apellido_var =StringVar()
correo_var =StringVar()
contraseña_var =StringVar()

Entry(pestana5, textvariable=id_var).grid(row=1, column=1, padx=10, pady=10)
Entry(pestana5, textvariable=nombre_var).grid(row=2, column=1, padx=10, pady=10)
Entry(pestana5, textvariable=apellido_var).grid(row=3, column=1, padx=10, pady=10)
Entry(pestana5, textvariable=correo_var).grid(row=4, column=1, padx=10, pady=10)
Entry(pestana5, textvariable=contraseña_var).grid(row=5, column=1, padx=10, pady=10)


def buscar():
    # Retrieve the information from the database
    usuario = interfazC.buscar(id.get())

    # Check if the user was found
    if usuario:
        # Set the values of the StringVarsx
        id_var.set(usuario[0][0])
        nombre_var.set(usuario[0][1])
        apellido_var.set(usuario[0][2])
        correo_var.set(usuario[0][3])
        contraseña_var.set(usuario[0][4])
    else:
        # Clear the values of the Entry widgets
        id_var.set("")
        nombre_var.set("")
        apellido_var.set("")
        correo_var.set("")
        contraseña_var.set("")
        
Label(pestana5, text="Id: ").grid(row=1, column=0, padx=10, pady=10)
Label(pestana5, text="Nombre: ").grid(row=2, column=0, padx=10, pady=10)
Label(pestana5, text="Apellido: ").grid(row=3, column=0, padx=10, pady=10)
Label(pestana5, text="Correo: ").grid(row=4, column=0, padx=10, pady=10)
Label(pestana5, text="Contraseña: ").grid(row=5, column=0, padx=10, pady=10)

# Set the initial value of the ID Entry widget to 0
id_var.set(0)

Button(pestana5, text="Buscar", command=buscar).grid(row=0, column=2, padx=10, pady=10)


    




#Pestaña 2

def leer():
    usuarios = interfazC.leerUsuarios()
    for usuario in usuarios:
        id_, nombre, apellido, correo, password = usuario
        tree.insert("", 0, text=id_, values=(nombre, apellido, correo, password))

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





# Pestaña 3


def actualizar():
    interfazC.actualizarPorId()

Button(pestana3, text="Actualizar", command=actualizar).grid(row=5, column=1, padx=10, pady=10)




#Pestaña 4

Label(pestana4, text="ID: ").grid(row=0, column=0, padx=10, pady=10)

id = StringVar()

Entry(pestana4, textvariable=id).grid(row=0, column=1, padx=10, pady=10)

def eliminar():
    # preguntar si está seguro de eliminar
    respuesta = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este usuario?")
    if respuesta:
        interfazC.eliminarUsuarios(id.get())
        id.set("")
    
Button(pestana4, text="Eliminar", command=eliminar).grid(row=1, column=1, padx=10, pady=10)

Ventana.mainloop()


