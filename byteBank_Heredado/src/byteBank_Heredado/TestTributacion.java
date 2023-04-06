package byteBank_Heredado;

public class TestTributacion {

    public static void main(String[] args) {
        CuentaCorriente cc = new CuentaCorriente(222, 333);
        cc.deposita(100.0);

        SeguraDeVida seguro = new SeguraDeVida();

        CalculadoraImpuesto calc = new CalculadoraImpuesto();

        calc.registra(cc);;
        calc.registra(seguro);

        System.out.println(calc.getTotalImpuesto());
    }

}