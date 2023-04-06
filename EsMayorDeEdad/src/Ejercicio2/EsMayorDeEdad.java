
package Ejercicio2;
import java.util.Scanner;

 class EsMayorDeEdad {
	public static void main(String[] args) {
		
	   byte edad;
	   
	   System.out.println("Cuantos años tenes?");
	   Scanner leer = new Scanner (System.in);//creando el escaneador del teclado
	                                          //se crea una sola vez
	   edad = leer.nextByte();
	   
	   if (edad >= 18) {
		   System.out.println ("Sos mayor de Edad");
	   }  
	   else {
		   System.out.println ("Sos menor de Edad");
	   }
	}
 }


