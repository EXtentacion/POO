from tkinter import messagebox
import sqlite3
import bcrypt



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
        
    
    def eliminarUsuarios(self, id):
        self.cursor.execute("DELETE FROM loll WHERE id=" + id)
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro eliminado con éxito")
        
    def actualizarUsuarios(self, id, nombre, apellido, correo, contraseña):
        self.cursor.execute("UPDATE loll SET nombre='" + nombre + "', apellido='" + apellido + "', correo='" + correo + "', contraseña='" + contraseña + "' WHERE id=" + id)
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
        
    def __del__(self):
        self.conexion.close()
        
      
