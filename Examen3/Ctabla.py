import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

    
class control:
    

    def __init__(self):
        self.conexion = sqlite3.connect("BDBanco.db")
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.execute('''
                CREATE TABLE banco(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                NoCuenta VARCHAR(100),
                Saldo VARCHAR(100)
                )
            ''')
            messagebox.showinfo("BBDD", "Base de datos creada con éxito")
        except:
            messagebox.showwarning("¡Atención!", "La base de datos ya existe")
            
    #insertar usuarios
    
    def insertarbase(self, NoCuenta, Saldo):
        self.cursor.execute("INSERT INTO banco VALUES(NULL, '" + NoCuenta + "', '" + Saldo + "')")
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con éxito")
        
    def buscar(self, id):
        self.cursor.execute("SELECT * FROM banco WHERE id=?", (id,))
        usuario = self.cursor.fetchall()
        return usuario
    
        
    #quiero poder leer todos los parametros de la tabla
    def leerbase(self):
        self.cursor.execute("SELECT * FROM banco")
        usuarios = self.cursor.fetchall()
        return usuarios
        
    #volver a preguntar si quiere eliminar el usuario
    def eliminarbase(self, id):
        self.cursor.execute("DELETE FROM banco WHERE id=" + str(id))
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro eliminado con éxito")
    
    
    #preguntar si esta seguro de querer eliminar el usuario
    
    def actualizarbase(self, id, NoCuenta, Saldo):
        self.cursor.execute("UPDATE banco SET NoCuenta='" + NoCuenta + "', Saldo='" + Saldo + "' WHERE id=" + str(id))
        self.conexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
        
        

    


                    


    
