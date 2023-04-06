package byteBank_Heredado;

public class TestCuenta {
      public static void main(String[] args) {
		CuentaCorriente cc = new CuentaCorriente(1,1);
		cc.deposita(100.0);
		
		CuentaAhorro cp = new CuentaAhorro(2,3);
		cp.deposita(100.0);
		
		cc.transfiere(10.0, cp);
		
		System.out.println("El saldo de la cuenta de corriente es: " + cc.getSaldo());
		System.out.println("El saldo de la cuenta de ahorro es: " + cp.getSaldo());
	}
}
