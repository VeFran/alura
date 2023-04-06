package default_package;

public class ejercicioTablaMultiplicar {
	
	public static void main(String[] args) {
		
		for (int contador= 0; contador<= 10; contador++ ) {
			
			for (int multiplicacion= 0; multiplicacion <= 10; multiplicacion++ ) {
				
				System.out.print(contador * multiplicacion);  //de esta manera se imprimen la mult por cada linea
				System.out.print(" ");				
			}
			
			System.out.println();
		}
	}

}
