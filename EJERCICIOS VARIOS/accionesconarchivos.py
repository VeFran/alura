from os import system
system ("cls")

# # Generamos una lista con datos
# lista_nombres=['Luisana', 'Celeste','Natalia','Lautaro']

# # Vamos a crear un archivo
# contenido= open("C:\PYTHON 2022\EJERCIVIOS CON ARCHIVOS\misDatos.txt", "w")

# #ahora lo escribimos
# for nombre in lista_nombres:
#     contenido.write(nombre+ "\n")
    
# #ahora lo guardamos/cerramos
# contenido.close()

# Generamos una lista con datos
lista_nombres=['Luciana', 'Alejandra','Ailen','Yael','Nahiara']

# Vamos a crear un archivo
# contenido= open("C:\PYTHON 2022\EJERCIVIOS CON ARCHIVOS\misDatos.txt", "a")
contenido= open("C:\PYTHON 2022\EJERCIVIOS CON ARCHIVOS\misDatos2.txt", "w")

#ahora lo escribimos
for nombre in lista_nombres:
   print(nombre, file = contenido)
    
#ahora lo guardamos/cerramos
contenido.close()



