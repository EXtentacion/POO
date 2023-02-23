#1. Importar la clase
from Personaje import *

#2. Instanciar un objeto
Heroe = Personaje()

#3. Acceder a sus atributos

Heroe.nombre 
Heroe.especie 
Heroe.altura 

#4. Acceder a sus metodos

        
print('Atributos del personaje: ')
print("El personaje pertenece a la raza: " + Heroe.especie + " Se llama: " + Heroe.nombre + " Mide: " + str(Heroe.altura) + " metros")
print('')

print('Metodos del personaje: ')



Heroe.correr(True)


    
