class Personaje:
   
   def __init__(self,esp,nom,alt):
      self.__especie = esp
      self.__nombre = nom
      self.__altura = alt
         
      
    
   def correr(self,estado):
     if estado == True:
        print('El personaje'+self.__nombre+'esta corriendo')
     else:
        print('El personaje'+self.__nombre+'esta quieto')
        
            
        
   def lanzarGranada(self):
      print('El personaje'+self.__nombre+'lanzo una granada')

   def recargarArma(self,municiones):
     cargador=5
     cargador = cargador + municiones
     print('El personaje'+self.__nombre+'recargo su arma y ahora tiene'+str(cargador)+'municiones')
     
     
   #ejemplo de metodo privado
   
   def __pensar(self):
      print('El personaje'+self.__nombre+'esta pensando')
      
   def getNombre(self):
      return self.__nombre
   
   def getEspecie(self):
      return self.__especie
   
   def getAltura(self):
      return self.__altura
   
   def setNombre(self,nombre):
      self.__nombre = nombre
      
   def setEspecie(self,especie):
      self.__especie = especie
   
   def setAltura(self,altura):
      self.__altura = altura

    
    




    
    