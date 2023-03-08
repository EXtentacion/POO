import tkinter as tk
import tkinter.messagebox as messagebox

class LoginUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Login")
        self.parent.geometry("400x200")
        self.parent.resizable(False, False)
        self.parent.config(bg="#fff")
        
        self.label1 = tk.Label(self.parent, text="Correo", bg="#fff")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        # escribir la contraseña con asteriscos
        self.label2 = tk.Label(self.parent, text="contraseña", bg="#fff")
        self.label2.grid(row=1, column=0, padx=10, pady=10)
          
        self.entry1 = tk.Entry(self.parent)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.entry2 = tk.Entry(self.parent, show="*")
        self.entry2.grid(row=1, column=1, padx=10, pady=10)
         
         
         #boton este centrado
        self.boton1 = tk.Button(self.parent, text="Ingresar", command=self.ingresar)
        self.boton1.grid(row=3, column=1, columnspan=2, padx=50, pady=50, sticky=tk.W+tk.E)

    def ingresar(self):
        correo = self.entry1.get()
        contraseña = self.entry2.get()
        if  correo ==  'fercho@gmail.com'  and contraseña ==  "12345" :
            messagebox.showinfo("Login", "Bienvenido")
        else :
            messagebox.showerror("Login", "Usuario o contraseña son incorrectos")
 



            