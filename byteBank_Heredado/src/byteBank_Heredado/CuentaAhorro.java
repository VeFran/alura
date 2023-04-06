package byteBank_Heredado;

public class CuentaAhorro extends Cuenta {
    
		
	public CuentaAhorro(int agencia, int numero) {
		super(agencia, numero);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void deposita(double valor) {
		this.saldo = this.saldo + valor;
		
	}

}
