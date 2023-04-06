package java_Pila_Ejecucion;

public class Flujo {
	public static void main(String[] args) {
		System.out.println("Inicio main");
		metodo1();
		System.out.println("Fin main");
		
	}
    public static void metodo1() {
    	System.out.println("Inicio metodo1");
    	metodo2();
    	System.out.println("Fin de método1");
    }
    
    public static void metodo2() {
    	System.out.println("Inicio método2");
    	for(int i= 1; i <= 5; i++) {
    		System.out.println(i);
    		try { // Intenta esto
    		  //int num = 0;
    		  //int resultado = i/num;
    		  // System.out.println(resultado);
    			String test = null;
    			System.out.println(test.toString());
    		} catch(ArithmeticException | NullPointerException exception) { //Atrapa el error
    		  System.out.println(exception.getMessage());
    		  System.out.println("Atrapo Excepción");
    		  exception.printStackTrace();
    		} 
    	 
        }
    	System.out.println("Fin método2");
    }
}
