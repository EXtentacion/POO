#Examen 2do Parcial

#Necesitamos crear una interfaz capas de generar un matricula 

from tkinter import *
from tkinter import messagebox
import random


class Matricula:
    

    def __init__(yo, hermano):
        #Creacion de la Ventana
        yo.hermano = hermano
        yo.hermano.title("Matricula")
        yo.hermano.geometry("350x250")
        yo.hermano.config(bg="#f4f4f4")
        
        #Predefinos variables
        yo.nombre = StringVar()
        yo.a_paterno = StringVar()
        yo.a_materno = StringVar()
        yo.a_nacimiento = IntVar()
        yo.carrera = StringVar()
        
        yo.crear_widgets()
        
    def crear_widgets(yo):
        #Componentes de mi interfaz
        yo.label_n = Label(yo.hermano, text="Nombre:", bg="#F0F0F0")
        yo.label_n.grid(row=0, column=0, padx=5, pady=5)
        
        yo.entry_n = Entry(yo.hermano, textvariable=yo.nombre)
        yo.entry_n.grid(row=0, column=1, padx=5, pady=5)
        
        yo.l_a_paterno = Label(yo.hermano, text="A Paterno:", bg="#F0F0F0")
        yo.l_a_paterno.grid(row=1, column=0, padx=5, pady=5)
        
        yo.e_a_paterno = Entry(yo.hermano, textvariable=yo.a_paterno)
        yo.e_a_paterno.grid(row=1, column=1, padx=5, pady=5)
        
        yo.l_a_materno = Label(yo.hermano, text="A Materno:", bg="#F0F0F0")
        yo.l_a_materno.grid(row=2, column=0, padx=5, pady=5)
        
        yo.e_a_materno = Entry(yo.hermano, textvariable=yo.a_materno)
        yo.e_a_materno.grid(row=2, column=1, padx=5, pady=5)
        
        yo.l_a_nacimiento = Label(yo.hermano, text="Año de nacimiento:", bg="#F0F0F0")
        yo.l_a_nacimiento.grid(row=3, column=0, padx=5, pady=5)
        
        yo.e_a_nacimiento = Entry(yo.hermano, textvariable=yo.a_nacimiento)
        yo.e_a_nacimiento.grid(row=3, column=1, padx=5, pady=5)
        
        yo.l_carrera = Label(yo.hermano, text="Carrera:", bg="#F0F0F0")  
        yo.l_carrera.grid(row=4, column=0, padx=5, pady=5)
        
        yo.e_carrera = Entry(yo.hermano, textvariable=yo.carrera)
        yo.e_carrera.grid(row=4, column=1, padx=5, pady=5)
        
        yo.b = Button(yo.hermano, text="Generar", command=yo.generar_matricula)
        yo.b.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def generar_matricula(yo):
        #Obtenermos los datos de los textvariables y asignamos a variables
        nombre = yo.nombre.get()
        a_paterno = yo.a_paterno.get()
        a_materno = yo.a_materno.get()
        a_nacimiento = yo.a_nacimiento.get()
        carrera = yo.carrera.get()
        
        #Evitar mistakes
        if nombre == "" or a_paterno == "" or a_materno == "" or a_nacimiento == "" or carrera == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
        else:
            #Logica detras del poema
            matricula = nombre[0] + a_paterno[0:2] + a_materno[0:2] + str(a_nacimiento)[-2:] + str(2023)[-2:] + carrera[0:3] + str(random.randint(0, 1000))
            messagebox.showinfo("Matricula", "Tu Matricula random es: {}".format(matricula.upper()))
            
if __name__ == "__main__":
    root = Tk()
    app = Matricula(root)
    root.mainloop()
    



    


