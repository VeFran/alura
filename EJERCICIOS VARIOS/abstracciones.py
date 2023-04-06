from os import system
system ("cls")

#DEclaramos nuestra clase
#class Animal (object):
    #Primer método
    # def setName(self, name): #Método que asigna un nombre al animal
    #     self.name= name      #Self es un utilitario el objeto, hace referencia al objeto 
    
    # #Segundo método
    # def getName(self):       #Método que nos permite retornará el nombre del animal
    #     return self.name     #Es un utilitario del objeto, hace referencia al objeto
    
# animal= Animal()             #Instancia de nuetra clase    
# animal.setName ("Perro")     #Asignacion de nombre
# print(animal.getName())

# import abc                   #La librería abc nos permite crear clses abstractas
# from abc import ABC, ABCMeta, abstractmethod

# #Declaramos nuestra clse
# class Animal(ABC):
#     def _init_ (self):
#         _metaclass_= ABCMeta #Metaclase
#     #Primer método
#     #Decorar para métodos abstractos
#     @abc.abstractclassmethod
    
#     def setName (self, name):
#         self.name = name
#         return self.name

# import abc
# from abc import ABC, ABCMeta, abstractmethod
#Declaramos nuestra clase
# class Animal(ABC):
#     def _init_ (self):
#         _metaclass_= ABCMeta #Metaclase
#     #Primer método
#     #Decorar para métodos abstractos
#     @abc.abstractclassmethod
    
#     def setName (self, name):
#         self.name = name
        
#     #Segundo Método
#     #Decorar para métodos abstractos
#     @abc.abstractclassmethod
#     def getName (self):
#         return self.name 

# animal = Animal()    #Cuando hacemos corret, PYTHON arroja un error, ya que una clse abstracta no se puede asignar a una variable

# class Perro (Animal):
#    def _init_ (self):
#        pass
   
#    def setName(self, name):
#        self.name = name
       
#    def getName(self):
#        return self.name
   
# perro = Perro()
# perro.setName("Marly")
# perro.getName()
# print(perro.getName())

#Ahora, que tal si cambiamos la clase Animal para el manejo de propiedades:

import abc 
from abc import ABC

#declaramos nuestra clase
class Animal (ABC):
    #Asingar nombre
    def set_name(self, name):
        pass
    
    #Obtener nombre
    def get_name(self):
        pass
    
    #Definimos las propiedades
    name= abc.abstractproperty(get_name, set_name)
    
class Perro(Animal):
    def _init_ (self):
        pass
    
    #Propiedad para obtener el nombre
    @property
    def name(self):
        return self._name
    
    #Propiedad para asignar el nombre
    @name.setter
    def name (self, name):
        self._name = name

perro= Perro()           #Instancia Perro
perro.name = "Marley"    #Asignación del Nombre
print(perro.name)        #Obtenemos el valor del nombre
    
   
    
        

