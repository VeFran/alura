package byteBank_Heredado;

public class Administrador  implements Autenticable {
    
	
	private AutenticacionUtil autenticador;
	
	private String contraseña;
	
	public Administrador() {
		this.autenticador = new AutenticacionUtil();
		
	}
	
		
    @Override	
	public double getBonificacion() {
		// TODO Auto-generated method stub
		return this.getSalario();
	}

	private double getSalario() {
		// TODO Auto-generated method stub
		return 0;
	}


	
	@Override
    public boolean autenticar(String contraseña) {
		
		return this.autenticador.autenticar(contraseña);
	
	 	
	}

	@Override
	public boolean iniciarSesion(String contraseña) {
		// TODO Auto-generated method stub
		return this.contraseña == contraseña;
	}
	
	@Override
	public void setContraseña(String contraseña) {
		// TODO Auto-generated method stub
		this.autenticador.setContraseña(contraseña); 
	}
	
}
