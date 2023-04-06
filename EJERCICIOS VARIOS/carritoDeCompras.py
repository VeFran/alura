import os
os.system ("cls")

# Programa Inicio Carrito de Compras
idProducto=[];
precioProducto=[];
Producto=[];
acumulador=0
bandera ="s"
i=0
while bandera =="s":
    idProducto.append(int(input("Ingrese Artículo del Producto:  ")))
    Producto.append(str(input("Ingrese el producto que desea comprar: ")))
    precioProducto.append(float(input("Ingrese precio de Producto: ")))
    i+= 1;
    acumulador = acumulador + precioProducto[i-1]
    bandera = str(input("Desea seguir comprnado?  S/N:  "))
    bandera = bandera.lower()
print(f"Los productos que Ud compro son:{Producto}")
print(f"Los precios de los productos que Ud compro son: {precioProducto}")
print("El total de su compra es: " +str(acumulador)) 
