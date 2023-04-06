from os import system
system ("cls")

'''
Diccionario={"Argentina":"Buenos Aires", "Brazil":"Brazilia","Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
#Creamos un diccionario
print(Diccionario)
#Imprimo diccionario
Diccionario["Italia"]="Lisboa" #Agregamos un elemento al diccionario
print(Diccionario) #Imprimimos con el elemento agregado

Diccionario["Italia"]="Roma" #Modificamos el elemento para su correccion lo sobreescribimos

#del Diccionario["Reina Unido"] #Borramos un elemento escribiendolo con una falta de ortografia 
#Vimos que al no respetar minusculas y mayusculas nos da error y no continua
del Diccionario["Reino Unido"]

print(Diccionario)
#Imprimimos el Diccionario
print(" ")
Diccionario_Combinado={"Argentina":"Buenos Aires", 33:"Cristo", "Juan":23}
#Creo un Diccionario con elementos combinados
print(Diccionario_Combinado)
print(" ")
#Imprimo nuevo diccionario

Capitales=["España", "Italia", "Argentina"]
#Creo una tupla Capitales para comvertirlo en diccionario


capitales={Capitales[0]:"Madrid", Capitales[1]:"Roma",Capitales[2]:"Buenos Aires"}
print(capitales)

#Imprimo el diccionario capitales
print(Capitales)

#Imprimo la tupla Capitales
print(capitales["Argentina"])
#Imprimime el valor de la clave Argentina
'''

#VAMOS A CREAR UN DICCIONARIO QUE CONTENGA UNA lista INTERNA COMO VALOR
# Acuerdence que el diccionario tiene Clave:Valor

Equipo={23:"Juan", "Nombre":["Miguel", "Juan"], "Copas":[1982,1984,1985,1986]}
#Creamos una lista dentro de un diccionario
print(Equipo)
#Imprimo el diccionario
print(Equipo["Nombre"])
#Imprimo una clave que contiene una lista en el diccionario
print(Equipo["Copas"])
#Imprimo una clave que contiene una lista en el diccionario
Equipo["Años"]=55
#Agrego una clave y valor
print(Equipo)
#Imprimo el diccionario

#VAMOS A CREAR UN DICCIONARIO QUE CONTENGA UN DICCIONARIO INTERNO COMO VALOR
Equipo={23:"Juan", "Nombre":{"Mapuche":["Anamilla", "Camil", "Lihue"]}, "Copas":[1982,1984,1985,1986]}
#Creo un dicionario con lista o tupla y Diccionario interno
print(Equipo)
#Imprimimos todo completo
print(Equipo["Nombre"])
#Imprimo el diccionario interno con su lista
print(Equipo.keys())
# Imprimo solamente las llaves o claves de un diccionario
print(Equipo.values())
# Imprimo solo los valores del diccionario
print(len(Equipo))
#Imprimo el diccionario completo

print(Equipo)
