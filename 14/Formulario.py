
#Se requiere una Interfaz con dos screens una para la administración de cuenta en caja popular y la otra para la creacion de cuentas, con elprograma podremos consultar saldo, ingresar efectivo, retirar efectivo y depositar a otracuenta,cada cuenta tiene registrados los siguientes datos: No. Cuenta, titular, edad y saldo

# Path: 14/Formulario.py




from tkinter import *
from tkinter import messagebox
import random
 



class Cuenta:
    def __init__(self, numero, titular, edad, saldo):
        self.numero = numero
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        
    def __str__(self):
        return "No. Cuenta: {}, Titular: {}, Edad: {}, Saldo: {}".format(
            self.numero, self.titular, self.edad, self.saldo)
    
    def __repr__(self):
        return "Cuenta({}, {}, {}, {})".format(
            self.numero, self.titular, self.edad, self.saldo)
    
    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.numero == other.numero
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)


class Caja:
    def __init__(self):
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
    def consultar_saldo(self, numero):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta.saldo
        return None
        
    def ingresar_efectivo(self, numero, monto):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                cuenta.saldo += monto
                return True
        return False
        
    def retirar_efectivo(self, numero, monto):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
                    return True
                else:
                    return False
        return False
        
    def depositar_a_otra_cuenta(self, numero, monto, numero2):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
                    for cuenta2 in self.cuentas:
                        if cuenta2.numero == numero2:
                            cuenta2.saldo += monto
                            return True
                else:
                    return False
        return False
    

class NuevaCuenta(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Nueva Cuenta")
        self.grab_set()
        
        self.numero = random.randint(1000, 9999)
        self.titular = StringVar()
        self.edad = StringVar()
        
        Label(self, text="No. Cuenta: {}".format(self.numero)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Label(self, text="Titular: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        Entry(self, textvariable=self.titular).grid(row=1, column=1, padx=5, pady=5)
        Label(self, text="Edad: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        Entry(self, textvariable=self.edad).grid(row=2, column=1, padx=5, pady=5)

        Button(self, text="Crear", command=self.crear).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def crear(self):
        if self.titular.get() == "" or self.edad.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            self.parent.caja.agregar_cuenta(Cuenta(self.numero, self.titular.get(), int(self.edad.get()), 0))
            messagebox.showinfo("Información", "Cuenta creada con éxito")
            self.destroy()
    
    
            
class Formulario(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Caja Popular")
        self.geometry("300x300")
        self.caja = Caja()
        
        self.numero = StringVar()
        self.monto = StringVar()
        self.numero2 = StringVar()
        
        Label(self, text="No. Cuenta: ").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.numero).grid(row=0, column=1, padx=5, pady=5)
        
        Label(self, text="Monto: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.monto).grid(row=1, column=1, padx=5, pady=5)
        
        Label(self, text="No. Cuenta 2: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.numero2).grid(row=2, column=1, padx=5, pady=5)
        
        Button(self, text="Consultar Saldo", command=self.consultar_saldo).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Ingresar Efectivo", command=self.ingresar_efectivo).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Retirar Efectivo", command=self.retirar_efectivo).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Depositar a otra cuenta", command=self.depositar_a_otra_cuenta).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Nueva Cuenta", command=self.nueva_cuenta).grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Ver Todas las Cuentas", command=self.ver_todas).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        
        
    def consultar_saldo(self):
        if self.numero.get() == "":
            messagebox.showerror("Error", "Debe llenar el campo No. Cuenta")
        else:
            saldo = self.caja.consultar_saldo(int(self.numero.get()))
            if saldo is None:
                messagebox.showerror("Error", "No existe la cuenta")
            else:
                messagebox.showinfo("Información", "El saldo de la cuenta es: {}".format(saldo))
            
    def ingresar_efectivo(self):
        if self.numero.get() == "" or self.monto.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.ingresar_efectivo(int(self.numero.get()), float(self.monto.get())):
                messagebox.showinfo("Información", "Efectivo ingresado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
                
    def retirar_efectivo(self):

        if self.numero.get() == "" or self.monto.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.retirar_efectivo(int(self.numero.get()), float(self.monto.get())):
                messagebox.showinfo("Información", "Efectivo retirado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
                
    def depositar_a_otra_cuenta(self):

        if self.numero.get() == "" or self.monto.get() == "" or self.numero2.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.depositar_a_otra_cuenta(int(self.numero.get()), float(self.monto.get()), int(self.numero2.get())):
                messagebox.showinfo("Información", "Efectivo depositado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
    
    def nueva_cuenta(self):
        NuevaCuenta(self)
    
    def ver_todas(self):
        cuentas = [str(cuenta) for cuenta in self.caja.cuentas]
        if len(cuentas) == 0:
            messagebox.showinfo("Información", "No hay cuentas registradas")
        else:
            messagebox.showinfo("Cuentas", "\n".join(cuentas))
 



if __name__ == "__main__":
    app = Formulario()
    app.mainloop()
    

    



     








    

