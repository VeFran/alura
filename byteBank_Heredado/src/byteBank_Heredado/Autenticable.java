package byteBank_Heredado;

public  interface Autenticable {
	
  
	public  void setContraseña(String contraseña);
	
	public boolean iniciarSesion (String contraseña);

	boolean autenticar(String contraseña);

	double getBonificacion();
	
	

}
