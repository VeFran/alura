from os import system
system ("cls")

# class MiClase:
#     x = 5
    
# prueba1= MiClase()
# print(prueba1.x)    

class Automovil:
    pintura = "blanco"
    precio= 10000
    marca = "Ford"
    modelo = "Fiesta"
    motor= "V8"
    cubiertas = "Michelin"

    def acelerar(self):
      print ("Acelerando")

    def frenar(self):
      print ("Frenando")

    def girarDerecha(self):
      print ("Girando a la derecha")

    def girarIzquierda(self):
      print ("Girando a la izquierda")  

auto1 = Automovil()
camioneta1= Automovil()

auto1.precio= 15000
auto1.modelo="Focus"
camioneta1.precio= 30000
camioneta1.modelo="Ranger"
camioneta1.motor = "V6"
print("----------Auto Atributos--------------")
print (auto1.pintura)
print(auto1.precio)
print(auto1.modelo)
print(auto1.marca)
print(auto1.motor)
print("-----------Camioneta Atributos----------")
print(camioneta1.precio)
print(camioneta1.modelo)
print(camioneta1.marca)
print(camioneta1.motor)
print("----------Auto Metodos-----------------")
auto1.acelerar()
auto1.frenar()
auto1.girarDerecha()
auto1.girarIzquierda()
print("----------Camioneta Metodos-------------")
camioneta1.acelerar()
camioneta1.frenar()
camioneta1.girarDerecha()
camioneta1.girarIzquierda()
print("-------------Precio Auto-------------------")

argumento_1 = auto1.precio
precio_mas_iva = argumento_1 * 1.21
print(f"Valor del auto marca:{auto1.marca}, modelo {auto1.modelo}, es de $:{precio_mas_iva}")

print("-------------Precio Camioneta-------------------")

argumento_2 = camioneta1.precio
precio_mas_iva1 = argumento_2 * 1.21
print(precio_mas_iva1)


  