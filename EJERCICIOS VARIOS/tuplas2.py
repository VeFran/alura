import os
os.system ("cls")
miLista=["Pablo", 55, 1, 30.40, True] #Creamos una lista de elementos diferentes
print(miLista[:])
miTupla=tuple(miLista) #Convertimos la Lista en una tupla
print(miTupla[:])
UnaTupla=("España", "Francia", "Alemania", "Italia", "Portugal") #Creamos una tupla
print(UnaTupla)
# UnaLista=list(UnaTupla) #Convertimos la tupla en una lista
# print(UnaLista[:])
# print("Pablo" in UnaLista) #Imprimimos si el elemento "Pablo" esta en La Lista 
# print("Pablo" in UnaTupla) #Imprimimos si el elemento "Pablo" esta en La Tupla
# print("Pablo" in miTupla) #Imprimimos si el elemento "Pablo" esta en La Tupla
# print("Pablo" in miLista) #Imprimimos si el elemento "Pablo" esta en La Lista
# print(UnaTupla.count("Portugal")) #Imprimimos cuantas veces aparece el elemento "Portugal"
# print(len(UnaTupla)) #Imprimimos la Longitud de La Tupla
# Tupla_unidato=("Pablo",) #Creamos una tupla con un solo elemento
# print(len(Tupla_unidato))
# Tupla_conmas=UnaTupla+miTupla  #Concatenanos Tuplas
# print(Tupla_conmas[:])
# Tupla_dividida=Tupla_conmas[2:5]  #Dividimos la tupla
# print(Tupla_dividida[:])
# print(Tupla_conmas[2:5])

# otraforma="Julio", 25,3, 1965 #Creamos una tupla sin usar la funcion tuple()
# NOMBRE, DIA, MES, AÑO = otraforma  #Desempaquetado de Tupla
# print(otraforma)
# print(NOMBRE)
# print(DIA)
# print(MES)
# print(AÑO)

print(UnaTupla.count("Portugal")) #Imprimimos cuantas veces aparece Portugal en la Tupla


