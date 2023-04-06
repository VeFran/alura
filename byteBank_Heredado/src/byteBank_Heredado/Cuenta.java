package byteBank_Heredado;

public abstract class Cuenta {

    protected double saldo;
    private int agencia = 1;
    private int numero;
    private Cliente titular = new Cliente();
    
    private static int total;

    
    public Cuenta(int agencia, int numero){
        Cuenta.total++;
        System.out.println("Total de cuentas es " + Cuenta.total);
        this.agencia = agencia;
        this.numero = numero;
        this.saldo = 100;
        System.out.println("Estoy creando una cuenta" + this.numero);
    }

    public abstract void deposita(double valor);
        

    public boolean saca(double valor) {
        if(this.saldo >= valor) {
            this.saldo -= valor;
            return true;
        } else {
            return false;
        }
    }

    public boolean transfiere(double valor, Cuenta destino) {
        if(this.saldo >= valor) {
            this.saldo -= valor;
            destino.deposita(valor);
            return true;
        }
        return false;
    }

    public double getSaldo(){
        return this.saldo;
    }

    public int getNumero(){
        return this.numero;
    }

    public void setNumero(int numero){
        if(numero <= 0) {
            System.out.println("No pueder ser el valor menor o igual a 0");
            return;
        }
        this.numero = numero;
    }

    public int getAgencia(){
        return this.agencia;
    }

    public void setAgencia(int agencia){
        if(agencia <= 0) {
            System.out.println("No pueder ser el valor menor o igual a ");
            return;
        }
        this.agencia = agencia;
    }

    public void setTitular(Cliente titular){
        this.titular = titular;
    }

    public Cliente getTitular(){
        return this.titular;
    }

    public static int getTotal(){
        return Cuenta.total;
    }
    
    

}
