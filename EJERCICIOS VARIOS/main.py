import os, sys, sqlite3

conexion = sqlite3.connect("cajeroNew.db")
cursor=conexion.cursor()
cursor.execute("create table if not exists autoServicio (id integer primary key autoincrement, nombre varchar(100), clave integer, movimiento varchar(100), serviciopagado varchar(100), saldo float, dolares float)")
conexion.commit()
conexion.close()

def Admin():
    print("Menu Administrador")
    print("------------------")
    opcion=int(input("Ingrese la clave de administrador: "))
    match opcion:
        case 987654:
            IngresodeDatos()            
        case _: # default
            Menu()
            
def IngresodeDatos():
    import os, sqlite3
    os.system("cls")
    print("Menu Ingresar Nuevo Cliente")
    print("--------------------")
    con=sqlite3.connect("cajeroNew.db")
    print("Ingresar nuevo Cliente: \n")
    nombre = input("Ingrese Nombre del Cliente: ")
    clave = input("Ingrese la Clave transitoria: ")
    cursor = con.cursor()
    cursor.execute("INSERT INTO autoServicio (nombre, clave) VALUES (?, ?)", (nombre, clave))
    con.commit()
    con.close()
    print("Cliente ingresado con exito")
    opcion= input("Desea ingresar otro cliente? (S/N): ").lower()
    if opcion == "s":
        IngresodeDatos()
    else: 
        Menu()
    os.system("pause")
    os.system("cls")
    # Agregar validacion de ingreso de datos
    
    
def Menu():
    import os
    os.system("cls")
    print("Menu Principal Cajero Automatico")
    print("--------------------------------")
    print("1. Ingresar Dinero")
    print("2. Retirar Dinero")
    print("3. Consultar Saldo")
    print("4. Pagar Servicios")
    print("5. Cambiar Clave")
    print("6. Consultar Movimientos")
    print("7. Comprar Dolares")
    print("0. Salir")
    print("--------------------------------")
    opcion= int(input("Seleccione una opcion: "))
    match opcion:
        case 1:
            IngresarDinero()
        case 2:
            RetirarDinero()
        case 3:
            ConsultarSaldo()
        case 4:
            PagarServicios()
        case 5:
            CambiarClave()
        case 6:
            ConsultarMovimientos()
        case 7:
            ComprarDolares()
        case 0:
            salir()
        case _: # default
            print("Opcion no valida")
            os.system("pause")
            os.system("cls")
            Menu()
            
def IngresarDinero():
    Menu()

def RetirarDinero():
    Menu()

def ConsultarSaldo():
    Menu()

def PagarServicios():
    Menu()

def CambiarClave():
    Menu()

def ConsultarMovimientos():
    Menu()

def ComprarDolares():
    Menu()  
    
def salir():
    import os
    print("Gracias por utilizar el programa")
    os.system("pause")
    os.system("cls")
    exit()
    
Admin()