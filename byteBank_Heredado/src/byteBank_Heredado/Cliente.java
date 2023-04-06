package byteBank_Heredado;

public class Cliente implements Autenticable {

   
	//private String nombre;
	//private String documento;
	
	private String contraseña;
	
	private AutenticacionUtil autenticador;

    public Cliente() {
        this.autenticador = new AutenticacionUtil();
    }

    @Override
    public void setContraseña(String contraseña) {
        this.autenticador.setContraseña(contraseña);
    }


    @Override
    public boolean autenticar(String contraseña) {
        return this.autenticador.autenticar(contraseña);
    }

	@Override
	public boolean iniciarSesion(String contraseña) {
		if (this.contraseña == contraseña) {
			return true;
		}
		return false;
	}

	@Override
	public double getBonificacion() {
		// TODO Auto-generated method stub
		return 0;
	}

}