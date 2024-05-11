# Pregunta 1: ¿De las siguientes opciones, cuál es una manera inválida de implementar una condición en un programa Python?
""" (x) else sin if """

# Pregunta 2: En una competencia de cantantes, si las tres personas del jurado le dan una "X" al participante, 
# éste queda eliminado. De las siguientes, ¿cuál sería una manera de escribir esa condición?

# """ Asignar valores a los votos de los miembros del jurado """
jurado1 = "X"
jurado2 = "X"
jurado3 = "X"

# """ Verificar si el participante queda eliminado """
if jurado1 == "X" and jurado2 == "X" and jurado3 == "X":
    print("El participante queda eliminado")
else:
    print("El participante sigue en la competencia")

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 3: En algunos países, la mayoría de edad se cumple a los 18 años. 
# ¿Cúal es el código correcto para escribir un programa que determine si un usuario es mayor de edad o no?
 
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad") 
# Print Eres mayor de edad

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 4: ¿Qué imprime el siguiente código?
 
a = 15
b = 10
if a == b:
  print("Son iguales")
  print("Adiós")
else:
  print("Son distintos")
  print("Adiós")
print("a y b son dos números")
# Son distintos
# Adios
# a y b son dos números

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 5: ¿Cuál es el error que presenta el siguiente código?

""" 
c = float(input("Ingrese temperatura del agua"))
if c <= 0:
  print("Su agua está congelada")
elif c >= 0 and c < 100:
  print("Su agua está líquida") 
elif:
  print("Su agua está hirviendo") """
print("elif:")
print("    ^")
print("SyntaxError: invalid syntax")
# Print Existe un elif sin condición.

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 6: ¿Qué imprime el siguiente código?

n = 20
if (n <= 100 and n % 2 == 0) or (n < 5):
  if n != 21:
    print("1")
  else:
    print("2")
else:
  if n == 20:
    print("3")
  else:
    print("4")
# Print 1 

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 7: Para definir la calidad del aire se hace una medición de partículas presentes en este. 
# Dependiendo de su valor se definen 5 posibles estados de calidad de aire:
#
# Bueno: 0-99
# Regular: 100-199
# Alerta: 200-299
# Premergencia: 300-499
# Emergencia: 500-Superior
#
# Esto quiere decir si la medición es de menos de 99, la calidad es buena, si la medición es de menos de 199, 
# pero más de 100 es regular, etc.
#
# (Fuente: http://portal.mma.gob.cl pronostico-rm/)
#
# Hemos escrito el siguiente código que recibe esta medición e imprime la calidad del aire:

numero = int(input("Ingrese calidad del aire "))
if numero >= 0 and numero <= 99:
  print("Bueno")
elif numero >= 100 and numero <= 199:
  print("Regular")
elif numero >= 200 and numero <= 299:
  print("Alerta")
elif numero >= 300 and numero <= 499:
  print("Preemergencia")
else:
  print("Emergencia")
# Print Emergencia 

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 8: Para definir la calidad del aire se hace una medición de partículas presentes en este. 
# Dependiendo de su valor se definen 5 posibles estados de calidad de aire:
#
# Bueno: 0-99
# Regular: 100-199
# Alerta: 200-299
# Premergencia: 300-499
# Emergencia: 500-Superior
#
# Esto quiere decir si la medición es de menos de 99, la calidad es buena, si la medición es de menos de 199, 
# pero más de 100 es regular, etc.
# (Fuente: http://portal.mma.gob.cl pronostico-rm/)
# Hemos escrito el siguiente código que recibe esta medición e imprime la calidad del aire:

numero = int(input("Ingrese calidad del aire "))
if numero>=0 and numero<=99:
  print("Bueno")
if numero>=100 and numero<=199:
  print("Regular")
if numero>=200 and numero<=299:
  print("Alerta")
if numero>=300 and numero<=499:
  print("Preemergencia")
else:
  print("Emergencia")
# (x) Regular, Emergencia33

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 9: Queremos escribir un programa que imprima "par" si un número es par, y nada en otro caso. 
# ¿Cuál es el código correcto para esto?

numero = int(input("Ingrese numero "))
if numero%2==0:
  print("Es par")
# Print Es par

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Pregunta 10: Se conoce como año bisiesto a un año que tiene un día extra. Todo año bisiesto debe cumplir 
# alguna de las siguientes condiciones:
#
# 1. Debe ser divisible por 4, pero no por 100.
# 2. Debe ser divisible por 100, pero no por 400.
#
# Por ejemplo, 1996 es año bisiesto porque cumple la condición uno. Por otro lado 1900 no lo es, 
# ya que no cumple ninguna de las condiciones. 
# ¿Cuál de las siguientes condiciones es la que permite determinar si un año A es bisiesto?

A = 1996
if (A % 4 == 0 and A % 100 != 0) or (A % 100 == 0 and A % 400 == 0):
  print("Es bisiesto")
# Print Es bisiesto