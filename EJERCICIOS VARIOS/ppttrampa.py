'''
Algoritmo piedra_papel_tijeras
	i = 0	
	Mientras i<= 2 Hacer
		i = i + 1
	Escribir "Elegir piedra(1), papel(2), o tijeras(3): "
	Leer opcion  // Opcion de la persona
	computadoraOpcion = Aleatorio(1,3) // Opcion de la Computadora
		//Elegimos Piedra
		Si opcion == 1 Entonces
			Escribir "Gana Computadora, Papel mata a Piedra"
		SiNo
			Si opcion == 2 Entonces // Elegimos Papel
				
						Escribir "Gana Computadora, Tijeras mata a Papel"
			SiNo
				Si opcion == 3 Entonces // Elegimos Tijeras
				
						Escribir "Gana Computadora, Piedra mata a Tijeras"
				FinSi
			FinSi
		FinSi
	
Fin Mientras
	Escribir "Game Over"
	
FinAlgoritmo
'''