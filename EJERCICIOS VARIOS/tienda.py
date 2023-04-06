import os;
os.system ("cls");
precioPrenda = float (input ("Ingrese precio de la Prenda: "));
print ("Seleccionar el Plan: ");
print ("1- Pago en Efectivo - descuento del 15% ");
print ("2- Solo 1 pago por plataforma digital - descuento del 5%")
print ("3- 3 cuotas sin  interes");
print ("4- 12 cuotas, abona un 20% mas");
opcion = int (input("Ingrese numero de Plan elegido:  "));
if opcion == 1:
    plan = precioPrenda - precioPrenda * 0.15;
    print (f"Se abonara el valor de {plan}  $ por via digital");
elif opcion == 2:
    plan = precioPrenda - precioPrenda * 0.05;
    print (f"Se abonara el valor de $ {plan} por via digital");
elif opcion == 3:
    plan = precioPrenda/3;
    print (f"Se abonara el valor de ¨Se abonara el valor de $ {plan} en 3 pagos");         
elif opcion == 4:
    plan = precioPrenda - precioPrenda * 0.20;
    plan = precioPrenda / 12;
    print (f"Se abonara el valor de ¨Se abonara el valor de ${plan} en 12 pagos iguales");
else:
    print ("Ingreso un valor Erroneo")