from tkinter import *
from tkinter import messagebox
from clase import GeneradorPassword, CopiarPassword


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de contraseñas")
        self.master.resizable(0,0)
        self.master.iconbitmap("icon.ico")

        # Interfaz gráfica
        self.generador = GeneradorPassword(self.master)
        Button(self.generador.frame, text="Copiar", command=self.copiar).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        Button(self.generador.frame, text="Salir", command=self.salir).grid(row=3, column=1, sticky="w", padx=5, pady=5)

    def copiar(self):
        password = self.generador.contrasena.get()
        CopiarPassword(Toplevel(self.master), password)

    def salir(self):
        valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
        if valor == "yes":
            self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()







    
