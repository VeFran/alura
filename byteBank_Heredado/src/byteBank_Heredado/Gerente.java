package byteBank_Heredado;

public class Gerente implements Autenticable {
    
	private AutenticacionUtil autenticador;
		
	// Sobre-escritura de método
	public double getBonificacion() {
	    System.out.println("EJECUNTADO DESDE GERENTE");
	    return autenticador.getSalario()+ autenticador.getSalario()* 0.05;
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
		// TODO Auto-generated method stub
		return false;
	}
}
