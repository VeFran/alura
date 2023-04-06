package byteBank_Heredado;

public class AutenticacionUtil {
	
	private String contraseña;

    public void setContraseña(String contraseña) {
        this.contraseña = contraseña;
    }

    public boolean autenticar(String contraseña2) {
        if (this.contraseña == contraseña2) {
            return true;
        } else {
            return false;
        }
    }

	
	public double getSalario() {
		// TODO Auto-generated method stub
		return 0;
	}

	
}
