package default_package;

public class ejemploCondicionales2 {

	public static void main(String[] args) {

		System.out.println("Hello World");

		int edad = 21;
		int cantidadPersonas= 2;
		
		boolean esPareja = cantidadPersonas > 1;

		if (edad >= 18 && esPareja) {
			System.out.println("Usted puede pasar");
       } else {
                System.out.println("Usted no esta permitido a " + "entrar");
            }
		
		int edad2 = 68;
		boolean esAnciano = edad2 >= 65;
		System.out.println(esAnciano);
	}	
}
