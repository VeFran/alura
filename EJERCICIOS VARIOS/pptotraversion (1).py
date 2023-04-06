'''
Algoritmo piedra_papel_tijera
	Escribir  "1.- Piedra"
	Escribir  "2.- papel"
	Escribir  "3.- tijera"
	
	Repetir
		Leer manoJugador
		si manoJugador<1 o manoJugador>3 Entonces
			escribir "numero incorrecto"
		finsi	
		
	hasta que manoJugador>=1 y manoJugador<=3
	
	jugadaOrdenador<-1+azar(3)
	si manoJugador=1 Entonces
		escribir"la jugada es PIEDRA"
	FinSi
	
	si manoJugador=2 Entonces
		Escribir "la jugada  es PAPEL"
	FinSi
	si manoJugador=3 Entonces
		Escribir "la jugada  es TIJERA"
	FinSi
	si manoJugadorr = jugadaOrdenador Entonces
		Escribir "empate"
	FinSi
	Si (manoJugador=2 Y jugadaOrdenador=1) o (manoJugador=3 Y jugadaOrdenador=2) o (manoJugador=1 Y jugadaOrdenador=3)Entonces
		Escribir "gana Jugador"
		jugadasGanadas= jugadasGanadas+1
		
		Escribir "la jugada del ordenador es   ", jugadaOrdenador
		Escribir "gana el ordenador con ", jugadaOrdenador  
	FinSi
	
	
Fin Algoritmo


'''