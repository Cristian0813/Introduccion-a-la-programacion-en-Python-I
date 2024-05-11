# Pregunta 1 Escribe un programa para ayudar a una empresa que desea asignar sueldos para los 
# cargos de sus trabajadores. La lista es la siguiente:

# Ejecutivo: 90
# Jefe: 100
# Externo: 50

# La variable cargo contiene el nombre del cargo (por ejemplo, "Externo"). Recuerda entregar tu resultado 
# modificando únicamente la variable dinero

def sueldo(cargo):
  if cargo == "Ejecutivo":
    dinero = 90
  elif cargo == "Jefe":
    dinero = 100
  elif cargo == "Externo":
    dinero = 50
  else:
    dinero = 0

  return dinero

# Ejemplo de uso
cargo = "Externo"
sueldo_asignado = sueldo(cargo)
print(f"El sueldo para el cargo {cargo} es de {sueldo_asignado}")

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------


# Pregunta 2 Escribe un código que calcule el cuadrado de un número si este es impar, 
# o el cubo de un número si este es par. Por ejemplo, para 4 tu programa debe 
# entregar 64, y para 3 debe entregar 9.

def exponenciacion(numero):
  if numero % 2 == 0:  # Si el número es par
    resultado = numero ** 3  # Eleva el número al cubo
  else:  # Si el número es impar
    resultado = numero ** 2  # Eleva el número al cuadrado
  return resultado

# Ejemplos de uso
numero = 4
resultado = exponenciacion(numero)

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# Pregunta 3 Escriba un programa que verifique si un número es primo o no. Por ejemplo, 
# para los número 3, 5, y 13, la variable primo debe ser True, y para 1, 10, y 33, False.

def es_primo(numero):
  if numero <= 1:  # Casos base: 1 y menores no son primos
    return False

  primo = True
  for divisor in range(2, numero):  # Recorrer desde 2 hasta la raíz cuadrada del número
    if numero % divisor == 0:  # Si encuentra un divisor distinto de 1 y sí mismo, no es primo
      primo = False
      break

  return primo

# Ejemplos de uso
numero = 3
resultado = es_primo(numero)
print(f"{numero} es primo: {resultado}")  # Debe imprimir True

numero = 5
resultado = es_primo(numero)
print(f"{numero} es primo: {resultado}")

numero = 13
resultado = es_primo(numero)
print(f"{numero} es primo: {resultado}")

numero = 1
resultado = es_primo(numero)
print(f"{numero} es primo: {resultado}")

numero = 10
resultado = es_primo(numero)
print(f"{numero} es primo: {resultado}")

numero = 33
resultado = es_primo(numero)
print(f"{numero} es primo: {resultado}")

