package byteBank_Heredado;

public class TestGerente {
	public static void main(String[] args) {
		Gerente g1 = new Gerente();
		//g1.setNombre("Marco");
		//g1.setDocumento("235568413");
		//g1.setSalario(6000);
				
		//System.out.println(g1.getNombre());
		//System.out.println(g1.getDocumento());
		System.out.println(g1.getBonificacion());
		
		g1.setContraseña("Noviembre");
		boolean autentico = g1.iniciarSesion("Noviembre");
		
		System.out.println(autentico);
	}

}
