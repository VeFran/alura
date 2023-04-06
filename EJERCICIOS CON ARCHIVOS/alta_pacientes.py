import os

def clear():
    os.system("cls")
    print()

def crear_archivo(info): # Se escribe en el archivo de texto, si no existe se crea.
    try:
        with open("Pacientes.txt","a") as turnos:
            turnos.write(info)
    except:
        turnos = open("Pacientes.txt","a")
        turnos.write(info)

def main():
    clear()
    a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))
    while a == 0:

        dni = input("[?] Ingrese su DNI por favor: ")
        while dni.isdigit() == False:
            dni = input("[?] Ingrese su DNI correctamente por favor. Solo numeros: ")

        nombre = input("[?] Ingrese su nombre por favor: ")
        while nombre.isdigit():
            nombre = input("[?] Ingrese su nombre por favor, solo letras: ")

        edad = input("[?] Edad: ")
        while edad.isdigit() == False:
            edad = input("[?] Ingrese su edad nuevamente. Solo numeros: ")
        while int(edad) <= 17:
            print("[!] Error, no se le puede inscribir si es menor de 17.")
            edad = input("[?] Ingrese su edad nuevamente: ")


        nombre_guion = nombre.replace(" ", "_")
        l = f"{dni} {nombre_guion} {edad}"+" " + ";"

        crear_archivo(l)

        print()
        clear()
        a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))


