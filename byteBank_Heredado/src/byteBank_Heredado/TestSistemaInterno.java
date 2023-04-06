package byteBank_Heredado;

public class TestSistemaInterno {
      public static void main(String[] args) {
    	  Gerente g = new Gerente ();
    	  g.setContraseña ("2222");

    	  SistemaInterno si = new SistemaInterno();
    	  si.autentica(g);
		     		     
	}
}
