from os import system
system ("cls")

def Menu():
    print ("Menún Principal Veterinaria Pichichus")
    print ("-------------------------------------")
    print("0- Crear Base de Datos")
    print("1- Ingresar nueva mascota")
    print("2- Cambiar datos de una mascota")
    print("3- Eliminar nueva mascota")
    print("4- Buscar nueva mascota")
    print("5- Listar todas las mascotas")
    print("6- Salir")
    
    try:
        opcion= int(input("Ingrese una opción:"))
    except ValueError:
        print("Opción Incorrecta")
        os.system("pause")   #Se hace una pausa luego del mensaje de Opcion Incorrecta
        os.system("cls")    #Se limpia la pantalla luego de la pausa
        Menu()
    
    if opcion == 0:
        crearBD()        
    elif opcion == 1:
        ingresarMascota()
    elif opcion == 2:
        cambiarDatos()
    elif opcion == 3:
        eliminarMascota()
    elif opcion == 4:
        buscarMascota()
    elif opcion == 5:
        listarMascotas()
    elif opcion == 6:
        salir()
    else:
        print("Ingrese una opción válida")
        print("-------------------------") 
        Menu()
    
def crearBD():
    import os, sqlite3
    conexion = sqlite3.connect("veterinaria.db")
    conexion.execute("CREATE TABLE if not exists mascotas (id integer primary key AUTOINCREMENT, Nombre TEXT, Edad TEXT, Raza TEXT, Peso TEXT, Dueño TEXT)")
    conexion.commit()
    conexion.close()
    print("Base de Datos creada con Éxito")
    print("------------------------------")
    print("Presione tecla para continuar")
    os.system("pause")
    Menu()
    
def ingresarMascota():
    import os, sqlite3   # os es una librería que nos permite acceder a funcionalidades dependientes del S.O.
    conexion = sqlite3.connect("veterinaria.db")
    print("Ingresar una nueva mascota")
    print("--------------------------")
    nombre = input("Ingrese el nombre de la mascota:")
    edad = input("Ingrese la edad de la mascota:")
    raza = input("Ingrese la raza de la mascota:")
    peso = input("Ingrese el peso de la mascota:")
    dueño = input("Ingrese el nombre del dueño:")
    os.system("cls")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO mascotas(Nombre, Edad, Raza, Peso, Dueño) VALUES (?,?,?,?,?)", (nombre, edad, raza, peso, dueño))
    conexion.commit()
    conexion.close()
    print("Mascota ingresada con éxito")
    print("---------------------------")
    os.system("pause")
    Menu()

def salir():
    import os
    print ("Gracias por utilizar el programa")
    os.system ("pause")    
    os.system("cls")
    exit()
    
Menu()    




     