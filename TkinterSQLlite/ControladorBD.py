from tkinter import messagebox
import sqlite3
import bcrypt
from tkinter import simpledialog



class controlador:
    
    def __init__(self):
        self.conexion = sqlite3.connect("Alumnos.db")
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.execute('''
                CREATE TABLE loll(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100),
                apellido VARCHAR(100),
                correo VARCHAR(100),
                contraseña VARCHAR(100)
                )
            ''')
            messagebox.showinfo("BBDD", "Base de datos creada con éxito")
        except:
            messagebox.showwarning("¡Atención!", "La base de datos ya existe")
            
   #insertar usuarios
   

   
    def insertarUsuarios(self, nombre, apellido, correo, contraseña):
        self.cursor.execute("INSERT INTO loll VALUES(NULL, '" + nombre + "', '" + apellido + "', '" + correo + "', '" + contraseña + "')")
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con éxito")
        
    def buscar(self, id):
        self.cursor.execute("SELECT * FROM loll WHERE id=?", (id,))
        usuario = self.cursor.fetchall()
        return usuario
    
        
    #quiero poder leer todos los parametros de la tabla
    def leerUsuarios(self):
        self.cursor.execute("SELECT * FROM loll")
        usuarios = self.cursor.fetchall()
        return usuarios
        
    #volver a preguntar si quiere eliminar el usuario
    def eliminarUsuarios(self, id):
        self.cursor.execute("DELETE FROM loll WHERE id=" + str(id))
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro eliminado con éxito")
    
    
    #preguntar si esta seguro de querer eliminar el usuario
    
    def actualizarUsuarios(self, id, nombre, apellido, correo, contraseña):
        self.cursor.execute("UPDATE loll SET nombre='" + nombre + "', apellido='" + apellido + "', correo='" + correo + "', contraseña='" + contraseña + "' WHERE id=" + str(id))
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
        
    
        
        
    def actualizarPorId(self):
        # Ventana de diálogo para ingresar el ID
        id_usuario = simpledialog.askinteger("Actualizar usuario", "Ingrese el ID del usuario que desea actualizar:")
        
        # Verificar si se ingresó un ID válido
        if id_usuario:
            # Obtener los datos actuales del usuario a partir de su ID
            usuario_actual = self.buscar(id_usuario)
            
            # Verificar si se encontró un usuario con ese ID
            if usuario_actual:
                # Mostrar una ventana de diálogo para ingresar los nuevos datos del usuario
                datos_nuevos = simpledialog.askstring("Actualizar usuario", "Ingrese los nuevos datos del usuario (nombre, apellido, correo, contraseña), separados por comas:")
                
                # Verificar si se ingresaron datos válidos
                if datos_nuevos:
                    # Convertir los datos ingresados en una lista y actualizar el usuario
                    datos_nuevos = datos_nuevos.split(",")
                    self.actualizarUsuarios(id_usuario, datos_nuevos[0], datos_nuevos[1], datos_nuevos[2], datos_nuevos[3])
            else:
                messagebox.showwarning("¡Atención!", "No se encontró ningún usuario con ese ID")

        

        
    def __del__(self):
        self.conexion.close()
        
      
