class Personaje:
   
   def __init__(self,esp,nom,alt):
      self.especie = esp
      self.nombre = nom
      self.altura = alt
         
      
    
   def correr(self,estado):
     if estado == True:
        print('El personaje'+self.nombre+'esta corriendo')
     else:
        print('El personaje'+self.nombre+'esta quieto')
        
            
        
   def lanzarGranada(self):
      print('El personaje'+self.nombre+'lanzo una granada')

   def recargarArma(self,municiones):
     cargador=5
     cargador = cargador + municiones
     print('El personaje'+self.nombre+'recargo su arma y ahora tiene'+str(cargador)+'municiones')

    
    




    
    