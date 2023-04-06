from os import system
system ("cls")

txt = "Hola como están?"
x= txt.split()
print(x)

for elemento in x:
    print (elemento)

# parseo con coma
txt = "nombre, apellido, edad"
x= txt.split (",")
print(x)