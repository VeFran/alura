package default_package;

public class EjemploCondiciones {
	public static void main(String[] args) {

		System.out.println("Hello World");

		int edad = 15;
		int cantidadPersonas= 2;

		if (edad >= 18) {
			System.out.println("Usted puede pasar");
			System.out.println("Bienvenido ");
		} else {
			if (cantidadPersonas >= 2) {
                System.out.println("No tienes 18 años, pero puedes ingresar, porque estás acompañado");
            } else {
                System.out.println("Lamentablemente no puedes ingresar");
            }
		}
	}	
}
