def Menu():
    import os
    print("Estas en el menu principal")
    print("--------------------------")
    print("1. Agregar un articulo")
    print("2. Modificar un articulo")
    print("3. Eliminar un articulo")
    print("4. Listar articulos")
    print("5. Salir")
    print("--------------------------")
    try:
        opcion = int(input("Elija una opcion: "))
    except ValueError:
        print("Esta opcion no es valida")
        print("")
        Menu()
    os.system("cls")
    if opcion==1:
        AgregarArticulo()
    elif opcion==2:
        ModificarArticulo()
    elif opcion==3:
        EliminarArticulo()
    elif opcion==4:
        ListarArticulos()
    elif opcion==5:
        Salir()
    else:
        print("Esta opcion no es valida")
        print("")
        Menu()
def AgregarArticulo():
    import os, sqlite3
    con=sqlite3.connect("Articulo1.db")
    print("Menu Agregar Articulo")
    print("---------------------")
    nombre=input("Ingrese el nombre del articulo: ")
    precio=input("Ingrese el precio del articulo: ")
    os.system("cls")
    con.execute("""create table if not exists Productos 
                (codigo integer primary key AUTOINCREMENT, nombre text, precio real)""")
    con.execute("insert into Productos (Nombre, Precio) values ('"+nombre+"','"+precio+"')")
    con.commit()
    con.close()
    Menu()
def ModificarArticulo():
    import os, sqlite3
    producto=[]
    con=sqlite3.connect("Articulo1.db")
    print("Menu Modificar Articulos")
    print("---------------------")
    con.execute("select * from Productos")
    print("\tCodigo    \tNombre     \tPrecio")
    print("\t---------------------------------")
    for fila in con:
        producto.append(fila)
        product='\t'+str(fila[0])+'\t'+fila[1]+'\t'+str(fila[2])
        print(str(product))
        print("")
    cod=input("Ingrese el codigo del articulo a modificar: ")
    for fila in producto:
        if int(fila[0])==int(cod):
            nombre=fila[1]
            precio=fila[2]
            encontrado=True
            break
    nombre=input("Ingrese el nuevo nombre del articulo: "+nombre+": ")
    precio=input("Ingrese el nuevo precio del articulo: "+str(precio)+": ")
    sql="update Productos set Nombre='"+nombre+"', Precio='"+precio+"' where Codigo="+cod
    con.execute(sql)
    con.commit()
    con.close()
    os.system("cls")
    print("Articulo modificado")
    print("-------------------")
    Menu()
def ListarArticulos():
    import os, sqlite3
    con=sqlite3.connect("Articulo1.db")
    cusor=con.cursor()
    cusor.execute("select * from Productos")
    print("Menu Listar Articulos")
    print("---------------------")
    print("\tCodigo    \tNombre     \tPrecio")
    print("\t---------------------------------")
    for Productos in cusor:
        product='\t'+str(Productos[0])+'\t'+Productos[1]+'\t'+str(Productos[2])
        print(str(product))
    con.close()
    print("")
    print("")
    os.system("pause")
    os.system("cls")
    Menu()

def EliminarArticulo():
    import os, sqlite3
    con=sqlite3.connect("Articulo1.db")
    print("Menu Eliminar Articulos")
    print("---------------------")
    con.execute("select * from Productos")
    print("\tCodigo    \tNombre     \tPrecio")
    print("\t---------------------------------")
    for fila in con:
        product='\t'+str(fila[0])+'\t'+fila[1]+'\t'+str(fila[2])
        print(str(product))
        print("")
        
    cod=input("Ingrese el codigo del articulo que desea eliminar:")
    sql="delete from Productos where Codigo="+cod
    con.execute(sql)
    con.commit()
    con.close()
    os.system("cls")
    print("Articulo eliminado")
    print("-------------------")
    Menu()
def Salir():
    import sys
    print("Gracias por usar este programa")
    sys.exit()
Menu()