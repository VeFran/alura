package default_package;

public class TestConversion {

	public static void main(String[] args){
		
		float puntoFlotante = 3.14f;   // aqui!
		
		double salario = 1270.50;
        int valor = (int) salario;  // hacemos casting del tipo de dato
        System.out.println (valor);
        
        double valor1 = 0.2;
        double valor2 = 0.1;
        double total = valor1 + valor2;

        System.out.println(total);
    }
	
}
