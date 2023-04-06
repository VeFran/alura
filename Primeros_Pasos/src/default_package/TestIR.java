package default_package;

public class TestIR {
	public static void main(String[] args) {
		
		double salario = 3300.0;
		
		if ((salario >= 1900) && (salario<= 2800)){
		
		   double IR= (salario * 7.5)/100;
		   System.out.println("El IR es del 7.5% y se deducen: " +IR);
	    
	     }else
	        {
	    	  if ((salario >= 2800.01) && (salario<= 3751.0)){
	    	     double IR= (salario* 15)/100;
			     System.out.println("El IR es del 15% y se deducen: " +IR);
	    	  }else {
	    		     if ((salario >= 3751.01)&& (salario<= 4664.0)){
	    		    	 double IR= (salario * 22.5)/100;
	    			 System.out.println("El IR es del 22.5% y se deducen: " +IR);
	    		     }
	    	}	     
	    		
	     }   		   
	}

}
