package default_package;

public class ejercicioFactorial {
	public static void main(String[] args) {
		
		int factorial= 1;
		
		for (int n = 1; n <= 10 ; n ++ ) {
			
			factorial= n * factorial;
			System.out.println("El factorial de : " + n + ", es: " + factorial);
			
			}
	 }
}
