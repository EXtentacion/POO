#1. Importar la clase
from Personaje import *

#2. Solicitar atributos para el objeto

print('Ingrese los datos del HEROE')
especie = input('Ingrese la especie del personaje: ')
nombre = input('Ingrese el nombre del personaje: ')
altura = float(input('Ingrese la altura del personaje: '))
cargador = int(input('Ingrese la cantidad de municiones del personaje: '))
print('')
print('Ingrese los datos del ENEMIGO')
especie = input('Ingrese la especie del personaje: ')
nombre = input('Ingrese el nombre del personaje: ')
altura = float(input('Ingrese la altura del personaje: '))




#3. Crear el objeto

Heroe = Personaje(especie,nombre,altura)
vilano = Personaje(especie,nombre,altura)

#4. acceder a atributos y metodos de cada objeto

print('Los datos del heroe son: ')
print('El heroe es un '+Heroe.especie+' de nombre '+Heroe.nombre+' y mide '+str(Heroe.altura)+' metros')
print('')
print('')
print('Los datos del enemigo son: ')
print('El enemigo es un '+vilano.especie+' de nombre '+vilano.nombre+' y mide '+str(vilano.altura)+' metros')


#5. Llamar a los metodos de cada objeto

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(5)

vilano.correr(False)
vilano.lanzarGranada()
vilano.recargarArma(5)















    
