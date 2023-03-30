from tkinter import messagebox
import sqlite3
import bcrypt



class controlador:
    
    def __init__(self):
        self.conexion = sqlite3.connect("Alumnos.db")
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.execute('''
                CREATE TABLE hey(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT(100),
                apellido TEXT(100),
                correo TEXT(100),
                contraseña VARCHAR(100)
                )
            ''')
            messagebox.showinfo("BBDD", "Base de datos creada con éxito")
        except:
            messagebox.showwarning("¡Atención!", "La base de datos ya existe")
            
    def crearUsuarios(self, nombre, apellido, correo, contraseña):
        self.cursor.execute("INSERT INTO fernando VALUES(NULL, '" + nombre + "', '" + apellido + "', '" + correo + "', '" + contraseña + "')")
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con éxito")
    
    #quiero poder leer todos los parametros de la tabla
    def leerUsuarios(self):
        self.cursor.execute("SELECT * FROM fernando")
        usuarios = self.cursor.fetchall()
        return usuarios
        
    
    def eliminarUsuarios(self, id):
        self.cursor.execute("DELETE FROM fernando WHERE id=" + id)
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro eliminado con éxito")
        
    def actualizarUsuarios(self, id, nombre, apellido, correo, contraseña):
        self.cursor.execute("UPDATE fernando SET nombre='" + nombre + "', apellido='" + apellido + "', correo='" + correo + "', contraseña='" + contraseña + "' WHERE id=" + id)
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
        
    def __del__(self):
        self.conexion.close()
        
      
