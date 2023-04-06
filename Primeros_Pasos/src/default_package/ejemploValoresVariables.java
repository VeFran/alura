package default_package;

public class ejemploValoresVariables {
      public static void main(String[] args) {
    	  
    	  int numero1 = 5;
    	  int numero2 = 9;
    	  
    	  System.out.println(numero2);
    	  
    	  numero2= numero1;
		  System.out.println(numero2);
		  
		  numero1= 88;
		  System.out.println(numero2); // Java guarda valores, no direcciones ni punteros en memoria	  
		  
		  String saludo = "Hola, mi nombre es ";
		  String nombre = "Rómulo ";
		  String continuacion = "y mi edad es ";
		  int edad = 100;
		  System.out.println (saludo + nombre + continuacion + edad);
		  
		  String palabra= "Alura cursos online";
		  String palabra1= palabra + " " +  2023;
		  System.out.println(palabra1);
		  String palabra2= palabra + "comienzan el: " + "1" + " " + "Marzo del" + " " + 2023;
		  System.out.println(palabra2);
		  
	}
}
