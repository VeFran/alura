'''
Desafío 11:
Retomar el ejercicio del desafío anterior pero solo cargar en la lista aquellas notas que estén entre  6 y 10 (inclusive)
Mostrar las notas cargadas en la lista.
Si se ingresa la nota cero sale.'''
miLista=[]
numero=int(input("Ingrese una nota. Si ingresa cero(0) sale del programa "))
while numero !=0:
    if 10>=numero>=6:
        miLista.append(numero)
    numero=int(input("Ingrese una nota. Si ingresa cero(0) sale del programa "))
print("Las notas ingresadas son: ")
#for nota in miLista:
print(miLista)