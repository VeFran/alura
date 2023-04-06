import os
os.system ("cls")
paises = ["Peru", "Chile", "Argentina", "Bolivia"] #Creamos una lista
print (paises[:])  #Imprimimos la lista completa

paises.extend(["Ecuador", "Colombia", "Venezuela"]) #Agregamos varios elementos a la lista
print (paises[:])

# print (paises[0])   #Imprimimos el primer elemento de la lista 
# print (paises[4])   #Imprimimos el cuarto elemento de la lista
# print (paises [-1]) #Imprimimos el ultimo elemento de la lista 
# print (paises [-4]) #Imprimimos el primer elemento de la lista
# print (paises[0:3]) #Imprimimos des la posicion 0, los 3 primeros elementos de la lista
# print (paises[3:4]) #Imprime desde la posicion 3 hasta la posicion 4 de la lista
# print (paises[2][5]) #Imprime del indice 2, a elemento 5 de la Lista "Argentina"
# print(paises[2], paises[5]) #Imprime los elementos 2 y 5 de la lista
paises.append("Brasil") #Agregamos un elemento a la lista
print(paises[:])
paises.insert(0, "Uruguay") #Agregamos un elemento a la lista en la posicion 0
print(paises[:])
print(paises.index("Argentina"))
print("Brasil" in paises) #Imprimimos si el elemento "Brasil" esta en la lista
paises.remove("Brasil") #Eliminamos el elemento "Brasil" de la lista
print("Brasil" in paises)
print(paises[:])
paises.pop() #Eliminamos el ultimo elemento de la lista
print(paises[:])
datos_varios=[1,2,3,4,5,"Hola", "Mundo", True, False]
Lista_Nueva=paises+datos_varios #Concatenamos dos listas
print(Lista_Nueva[:])

