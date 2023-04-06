from os import system
system ("cls")

# Argumentos pasados por valor

def doblarNumero(nro):
   nro= nro * 2
   return nro

miNumero = 3
print(doblarNumero(miNumero)) 
print (miNumero)

# Argumentos pasados por referencia

def doblarNumero2(nros):
  for indice in range(len(nros)): 
    nros[indice]= nros[indice] * 2
  return nros

miNumeros=[10,20,5]
print(miNumeros)

print (doblarNumero2(miNumeros))

print(miNumeros)