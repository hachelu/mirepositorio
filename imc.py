masa=float(input("inserta tu masa en kilogramos:"))
altura=float(input("inserta el tu altura en metros"))

imc=masa/altura**2

print("tu imc es:" +str(imc))

if imc >= 25:
  print("tiene sobrepeso")

if imc <= 19:
  print("tiene sobrepeso")