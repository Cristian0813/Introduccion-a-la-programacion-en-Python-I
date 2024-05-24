
# 1. Calculadora Simple: Crea un programa que solicite dos números al usuario y realice 
#    operaciones básicas como suma, resta, multiplicación y división.

def solicitar_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("Entrada invalida. Por favor ingrese un número válido.")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def mostrar_resultados(a, b):
    print(f"Suma: {a} + {b} = {suma(a, b)}")
    print(f"Resta: {a} - {b} = {resta(a, b)}")
    print(f"Multiplicación: {a} * {b} = {multiplicacion(a, b)}")
    print(f"División: {a} / {b} = {division(a, b)}")

def calculadora():
    print("Calculadora Simple \n")
    while True:
        numero1 = solicitar_numero("Por favor, ingresa el primer número: ")
        numero2 = solicitar_numero("Por favor, ingresa el segundo número: ")
        mostrar_resultados(numero1, numero2)

        continuar = input("\n¿Deseas realizar otra operación? s/n: ")
        if continuar.lower() != 's':
            print("¡Gracias por usar la calculadora!")
            break

if __name__ == "__main__":
    calculadora()

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 2. Contador de Palabras: Escribe un programa que cuente la cantidad de palabras en una cadena 
#    de texto ingresada por el usuario.?

texto= input("Por favor ingresa el texto: ")
palabras = texto.split()
numero_palabras = len (palabras)
caracteres = len (texto)
print("El número de palabras en el texto es: ", numero_palabras)
print("Las palabras encontradas son:", palabras," y contiene ",caracteres, " caracteres")

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 3. Conversor de Temperatura Crea un programa que convierta grados Celsius a Fahrenheit o viceversa, dependiendo de la opción elegida por el usuario

def celsius_a_fahrenheit(celsius):
   """ Convertir de Celsius a Fahrenheit """
   fahrenheit = (celsius * 9/5) + 32
   return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
   """ Convertir de Fahrenheit a Celsius """
   celsius = (fahrenheit - 32) * 5/9
   return celsius

def princilpal():
   while True:
      opcion = input("¿Qué temperatura deseas convertir? \n1. Celsius a Fahrenheit \n2. Fahrenheit a Celsius \n3. Salir \n")
      if opcion == "1":
         celsius = float(input("Ingresa la temperatura en grados Celsius: "))
         fahrenheit = celsius_a_fahrenheit(celsius)
         print(f"{celsius}°C es igual a {fahrenheit}°F")
      elif opcion == "2":
         fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
         celsius = fahrenheit_a_celsius(fahrenheit)
         print(f"{fahrenheit}°F es igual a {celsius}°C")
      elif opcion == "3":
        print("Gracias por usar el programa")



def principal():
  while True:
    # Opción del usuario
    opcion = input("¿Desea convertir Celsius a Fahrenheit (C a F) o Fahrenheit a Celsius (F a C)? (C/F): ").upper()

    if opcion not in ("C", "F"):
      print("Opción inválida. Intente nuevamente.")
      continue

    # Valor de temperatura
    temperatura = float(input("Ingrese la temperatura: "))

    # Conversión de temperatura según la opción
    if opcion == "C":
      temperatura_convertida = fahrenheit_a_celsius(temperatura)
      tipo_conversion = "Fahrenheit"
    else:
      temperatura_convertida = celsius_a_fahrenheit(temperatura)
      tipo_conversion = "Celsius"

    # Mostrar temperatura convertida
    print(f"{temperatura} grados {opcion} equivalen a {temperatura_convertida:.2f} grados {tipo_conversion}.")

    # Continuar o salir
    otra_conversion = input("¿Desea realizar otra conversión? (S/N): ").upper()
    if otra_conversion != "S":
      break

if __name__ == "__main__":
  principal()


print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 4. Adivina el Número: Haz un juego en el que el programa elija un número aleatorio y el usuario tenga que adivinarlo. El programa debería dar pistas (mayor o menor) hasta que el usuario adivine el número.
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 5. Calculadora de Factorial: Escribe un programa que calcule el factorial de un número ingresado por el usuario.
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 6. Inversor de Cadena: Crea un programa que tome una cadena de texto ingresada por el usuario y devuelva la misma cadena pero invertida.
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 7. Generador de Contraseñas: Haz un generador de contraseñas que combine letras mayúsculas, minúsculas, números y caracteres especiales. El usuario debe poder especificar la longitud de la contraseña.
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 8. Suma de Dígitos: Escribe un programa que sume los dígitos de un número ingresado por el usuario.
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 9. Chequeo de Palíndromo: Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# 10 .Generador de Tablas de Multiplicar: Haz un programa que genere la tabla de multiplicar de un número ingresado por el usuario.
