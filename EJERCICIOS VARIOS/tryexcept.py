from os import system
system("cls")

num = int(input("Ingrese un numero: "))
div = int(input("Ingrese un divisor: "))

def dividir (num, div):
    return num/div
try:
    res = dividir(num,div)
    print(res)
except ZeroDivisionError:
    print ("Trataste de dividir entre cero :/ ")