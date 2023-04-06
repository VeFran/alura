package byteBank_Heredado;

public class ControlBonificacion {
	
	private double suma;
	
	public double registrarSalario(Funcionario funcionario) {
		this.suma+= funcionario.getBonificacion();
		System.out.println("Cálculo actual: " + this.suma);
		return this.suma;
	}
	
	public double getSuma() {
		return suma;
	}
}
