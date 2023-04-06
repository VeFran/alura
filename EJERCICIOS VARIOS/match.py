from os import system
system ("cls")

print("MENU DE OPCIONES")
print("1. Ventas")
print("2. Pagos")
print("3. Servicio Técnico")
print("4. Gerencia")

num= int (input("Ingrese una opción: !\n "))

match num:
    case 1:
        print("Elegiste Ventas")
    case 2:
        print("Elegiste Pagos")
    case 3:
        print("Elegiste Servicio Técnico")
    case 4:
        print("Elegiste Gerencia")    
        