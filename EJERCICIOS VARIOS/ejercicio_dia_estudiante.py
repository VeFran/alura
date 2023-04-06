import os
os.system ("cls")
#  tabla de multiplicar
resultado = 0
for i in range (1,11):
  print ("Tabla del  ", i)
  for j in range (1,11):
      resultado = i*j
      print (i, "x", j, "=", resultado)
print ("")
    
 # otro ejemplo para talba del 3
a= 0 
for i in range (0,31,3): #el 3 respresenta el incremento de la i
   print(f"3 x {a} = {i}")
   a= a+1
   