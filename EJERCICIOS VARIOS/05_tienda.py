'''
- Una tienda de ropa tiene 4 planes según como se decida efectuar el pago:
Plan 1: pago en efectivo, 15% de descuento del precio publicado.
Plan 2: Un solo pago por plataformas digitales, se realiza un 5% del precio publicado.
Plan 3: 3 cuotas sin interés, paga el precio publicado en 3 partes.
Plan 4: 12 cuotas, al precio publicado se le agregara el 20% y se pagaran 12 cuotas iguales de este nuevo valor.

El cliente (la tienda) nos pide que al ingresar por sistema el valor del precio publicado, nos regrese una pantalla con el detalle y los valores de los distintos planes.

Una posible resolucion en PSeInt

  Definir  precio, plan1, plan2, plan3, plan4 Como Real
	Escribir "precio de la prenda"
	Leer precio
	plan1 = precio * 0.85
	plan2 = precio * 0.95
	plan3 = precio / 3
	plan4 = (precio * 1.20)/12
	Escribir "los planes de pago son: "
	Escribir "Plan1 efectivo 15% de descuento $", plan1
	Escribir "plan2 plataforma digital 5% de descuento $", plan2
	Escribir "plan3 tres cuotas sin interes de: $", plan3
	Escribir "plan4 20% de interes en 12 cuotas de: $", plan4
'''


precio = 100

plan1 = precio * 0.85
plan2 = precio * 0.95
plan3 = precio / 3
plan4 = (precio * 1.20)/12
