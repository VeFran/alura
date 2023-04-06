'''
	Escribir  "elegir piedra(1), papel(2) o tijeras(3): "
	Leer miOpcion
	computadoraOpcion = Aleatorio(1,3)
	Si miOpcion == computadoraOpcion Entonces
		Escribir "Empate"
	SiNo
		Si miOpcion == 1  Entonces // Piedra
			Si computadoraOpcion == 2 Entonces // Papel
				Escribir "Gana Computadora, Papel mata a piedra"
			SiNo
				Escribir "Ganaste, Piedra mata a Tijeras"
			FinSi
		SiNo
			Si miOpcion == 2 Entonces // Papel
				Si computadoraOpcion == 3 Entonces // Tijeras
					Escribir "Gana Computadora, Tijeras mata a Papel"
				SiNo
					Escribir "Ganaste, Papel mata a Piedra"
				FinSi
			SiNo
				Si miOpcion == 3 Entonces // Tijeras
					Si computadoraOpcion == 1 Entonces // Piedra
						Escribir "Gana Computadora, Piedra mata a Tijeras"
					SiNo
						Escribir "Ganaste, Tijeras mata a Papel"
					FinSi 
				FinSi
			FinSi
			
		FinSi
	FinSi
	Escribir "Game Over"
'''
from ast import match_case
from random import randint

miOpcion = int(input("elegir piedra(1), papel(2) o tijeras(3): "))
computadoraOpcion = randint(1,3) # Un numero del 1 al 3

if miOpcion == computadoraOpcion:
  print("Empate")
elif miOpcion == 1: # Piedra
  if computadoraOpcion == 2: # Papel
    print("Gana Computadora, Papel mata a piedra")
  else:
    print("Ganaste, Piedra mata a Tijeras")
elif miOpcion == 2: # Papel
		if computadoraOpcion == 1: # Piedra
			print("Ganaste, Papel mata a Piedra")
		else:
			print("Gana Computadora, Tijeras mata a Papel")
elif miOpcion == 3: # Tijeras
		if computadoraOpcion == 1: # Piedra
			print("Gana Computadora, Piedra mata a Tijeras")
		else:
			print("Ganaste, Tijeras mata a Papel")
print("Game Over")

