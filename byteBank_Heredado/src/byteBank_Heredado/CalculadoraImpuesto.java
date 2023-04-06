package byteBank_Heredado;

public class CalculadoraImpuesto {
	
	private double totalImpuesto;
	
	public void registra (Tributacion t) {
		
		double valor = t.getValorImpuesto();
		this.totalImpuesto += valor;
	}
	
	public double getTotalImpuesto() {
		return totalImpuesto;
	}

	public void registra(CuentaCorriente cc) {
		// TODO Auto-generated method stub
		
	}

}
