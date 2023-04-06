# Determinar el Mayor
import os
os.system ("cls")

#print ("programa para encontrar el Numero Mayor")
#a = int (input ("Ingrese el primer numero: "))
#b = int (input ("Ingrese el segundo numero: "))
#c = int (input ("Ingrese el tercer numero: ")) 
#if a > b & a > c:
#   print ("El numero mayor es: ", a) 
#elif b > a  & b > c:
#   print ("El numero mayor es: ", b)
#else:
#   print ("El numero mayor es: ", c)  
print ("Programa para evaluar Notas")  
Nota_Alumno = int (input ("Ingrese la nota del del alumno: "))
if Nota_Alumno ==10:
      print ("LA nota del alumno es:  Sobresaliente")
elif Nota_Alumno>=8 and Nota_Alumno<10:
      print ("La nota del alumno es: Muy Buena")
elif Nota_Alumno>=6 and Nota_Alumno<8:
      print ("La Nota del alumno es:  Buena")
elif Nota_Alumno>=4 and Nota_Alumno<6:
      print ("La nota del alumno es: Regular")
elif Nota_Alumno<4 and Nota_Alumno>=0:
      print ("La nota del alumno es: Insuficiente")
# else:
      print ("La nota del alumno es: No Existe")
      
      
      
       
