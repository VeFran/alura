def Menu():
    import os
    print("Menú Principal Veterinaria Pichichus")
    print("-----------------------------------")
    print("0. Crear Base de Datos(Solo 1vez)")
    print("1. Ingresar nueva mascota")
    print("2. Cambiar datos de una mascota")
    print("3. Eliminar una mascota")
    print("4. Buscar una mascota")
    print("5. Listar todas las mascotas")
    print("6. Salir")
    try:
        opcion=int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción incorrecta")
        os.system("pause") # Pausa el programa hasta que se presione una tecla
        os.system("cls")
        Menu()
    if opcion==0:
        crearBD()
    elif opcion==1:       
        ingresarMascota()
    elif opcion==2:
        cambiarDatos()
    elif opcion==3:
        eliminarMascota()
    elif opcion==4:
        buscarMascota()
    elif opcion==5:
        listarMascotas()
    elif opcion==6:
        salir()
    else:
        print("Ingrese una opción válida")
        print("-------------------------")
        Menu()

def crearBD():
    import os, sqlite3
    con=sqlite3.connect("veterinaria.db")
    con.execute("CREATE TABLE if not exists mascotas (id integer primary key AUTOINCREMENT, Nombre TEXT, Edad TEXT, Raza TEXT, Peso TEXT, Dueño TEXT)")
    con.commit()
    con.close()
    print("Base de datos creada con éxito")
    print("------------------------------")
    os.system("pause")
    Menu()

def ingresarMascota():
    import os, sqlite3
    con=sqlite3.connect("veterinaria.db")
    print("Ingresar nueva mascota")
    print("----------------------")
    nombre=input("Ingrese el nombre de la mascota: ")
    edad=input("Ingrese la edad de la mascota: ")
    raza=input("Ingrese la raza de la mascota: ")
    peso=input("Ingrese el peso de la mascota: ")
    dueño=input("Ingrese el nombre del dueño: ")
    os.system("cls")
    cursor=con.cursor()
    cursor.execute("INSERT INTO mascotas (Nombre, Edad, Raza, Peso, Dueño) VALUES (?,?,?,?,?)", (nombre, edad, raza, peso, dueño))
    con.commit()
    con.close()
    print("Mascota ingresada con éxito")
    print("---------------------------")
    os.system("pause")
    Menu()

def cambiarDatos():
    import os, sqlite3
    con=sqlite3.connect("veterinaria.db")
    print("Ingresar nueva mascota")
    print("----------------------")
    Menu()
    
def eliminarMascota():
    Menu()

def buscarMascota():
    import os, sqlite3, re
    con=sqlite3.connect("veterinaria.db")
    print("Menu Buscar Mascota")
    print("-------------------")
    nombre=input("Ingresar nombre de la mascota: ")
    dueno=input("Ingresar nombre del dueño: ")
    cursor=con.cursor()
    cursor.execute("SELECT * FROM mascotas WHERE Nombre=? AND Dueño=?", (nombre, dueno))
    print("\tId\tNombre\tEdad\tRaza   \tPeso \tDueño")
    print("--\t------\t----\t----\t----\t-----")
    variable=cursor.fetchone()
    if variable != None:
        for i in variable:
            print(i,"\t", end="")
    else:
        print("No se ha encontrado el animal")
    print("\n")
    os.system("pause")
    # i=0
    # for i in varble:
    #     print(i,"\t", end="")
        
    # for fila in cursor:
    #     filaF='\t'+str(fila[0])+'\t'+fila[1]+'\t'+fila[2]+'\t'+fila[3]+'\t'+fila[4]+'\t'+fila[5]
    #     print(str(filaF))
    # for Productos in cusor:
    #     product='\t'+str(Productos[0])+'\t'+Productos[1]+'\t'+str(Productos[2])
    #     print(str(product))
    con.close()
    
    os.system("cls")
    

    # varble=cursor.fetchone()
    # varble=re.sub(r'[\[\]\(\)\(\,\)\']', ' ', str(varble))
    # print(varble)
    # print("------------------------------")
    
    Menu()
    

def listarMascotas():
    Menu()

def salir():
    import os
    print("Gracias por utilizar el programa")
    os.system("pause")
    os.system("cls")
    exit()
    
Menu()
