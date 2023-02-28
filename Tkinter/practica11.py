from tkinter import *



ventana = Tk()
ventana.title("Practica 11")
ventana.geometry("600x400")




#creacion de un menu
barraMenu = Menu(ventana)
ventana.config(menu=barraMenu)


#2. Definimos Secciones de la ventana
seccion1 = Frame(ventana,bg="red",width=200,height=200)
seccion1.pack(expand=True,fill=BOTH)


#izquierda
seccion2 = Frame(ventana,bg="blue",width=200,height=200)
seccion2.pack(side=LEFT,anchor=NW,fill=Y)

#derecha
seccion3 = Frame(ventana,bg="yellow",width=200,height=200)
seccion3.pack(side=RIGHT,anchor=NE,fill=Y)

#abajo
seccion4 = Frame(ventana,bg="green",width=200,height=200)
seccion4.pack(side=BOTTOM,anchor=SW,fill=X)

#3. Botones

boton1 = Button(seccion1,text="Presioname", bg="#000",fg="#000",width=10,height=1,)
boton1.grid(row=0,column=0)

boton2 = Button(seccion1,text="a la una", bg="blue",fg="#000",width=10,height=1)
boton2.grid(row=1,column=0)

boton3 = Button(seccion1,text="y a las tres", bg="yellow",fg="#000",width=10,height=1 )
boton3.grid(row=2,column=0)

boton4 = Button(seccion1,text="a las dos", bg="green",fg="#000",width=10,height=1)
boton4.grid(row=3,column=0)





#creacion de un submenu
archivoMenu = Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")

#creacion de un submenu
archivoEdicion = Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")

#creacion de un submenu
archivoHerramientas = Menu(barraMenu,tearoff=0)
archivoHerramientas.add_command(label="Herramienta 1")
archivoHerramientas.add_command(label="Herramienta 2")
archivoHerramientas.add_command(label="Herramienta 3")

    
#creacion de un submenu
archivoAyuda = Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Ayuda 1")
archivoAyuda.add_command(label="Ayuda 2")
archivoAyuda.add_command(label="Ayuda 3")

#agregar los submenus al menu principal
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)






ventana.mainloop()









