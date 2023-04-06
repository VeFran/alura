from os import system
system("cls")

from random import randint

dadosUsuario=[]
totalUsuario = 0
partidaActual = 1
while partidaActual <= 5:
  print(f'..:: Ronda #{partidaActual} ::..')
  tirarDados = input("Tirar los dados (s/n): ")
  if tirarDados == "n":
    print("Dale tira esos dados!!!")
    continue
  # Tiramos los dados de usuario
  for i in range(5):
    dadosUsuario.append(randint(1,6))
  print("Sus dados: ", dadosUsuario)

  # Tenemos los dados, realizamos calculo de puntaje
  puntajeUsuario = 0
  dadoParEncontrado = 0
  trio = 0
  par1 = 0
  par2 = 0

  for dado in dadosUsuario:
    if dadosUsuario.count(dado) == 5:
      print(f"Sacaste 5 veces el dado: {dado}")
      puntajeUsuario = puntajeUsuario + 15
      break
    elif dadosUsuario.count(dado) == 4:
      print(f"Sacaste 4 veces el dado: {dado}")
      puntajeUsuario = puntajeUsuario + 10
      break
    elif dadosUsuario.count(dado) == 3:
      if trio == 0:
        print(f"Sacaste 3 veces el dado: {dado}")
        trio = dado
    elif dadosUsuario.count(dado) == 2:
      if par1 == 0:
        print(f"Sacaste un par de: {dado}")
        par1 = dado
      elif par1 != dado  and par2 == 0:
        print(f"Sacaste un par de: : {dado}")
        par2 = dado
  
  if par1 != 0 and par2 != 0:
    print(">>>> Doble Par +5")
    puntajeUsuario = puntajeUsuario + 5
  elif par1 != 0 or par2 != 0:
    if trio !=0:
      print(f">>>> Full!!! +9")
      puntajeUsuario = puntajeUsuario + 9
    else:
      print(">>>> Par Simple +2")
      puntajeUsuario = puntajeUsuario + 2
  else:
    if trio != 0:
      print(f">>>> Trio de {trio} +6")
      puntajeUsuario = puntajeUsuario + 6
  
  totalUsuario = totalUsuario + puntajeUsuario
  print(
f'''
Puntaje en esta tirada: {puntajeUsuario}
## Marcador general {totalUsuario} ##
'''
  )
    
  partidaActual += 1
  dadosUsuario.clear()
