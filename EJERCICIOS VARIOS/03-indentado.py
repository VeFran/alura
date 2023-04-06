
'''
Python se basa en la sangría (espacio en blanco al comienzo de una línea) para definir el alcance en el código. Otros lenguajes de programación a menudo usan corchetes para este propósito.

El scope o cuerpo de una funcion o un bucle se define por un indentado o sangria.
'''

def saludar():
  print("Hola")

if 1 == 1:
  print("uno es uno")
  if 2 == 1:
    print("dos es uno")
  print("dos es uno")
print("Chau")

