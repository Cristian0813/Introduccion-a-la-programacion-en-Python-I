# 1. Calculadora Simple: Crea un programa que solicite dos números al usuario y realice operaciones básicas como suma, resta, multiplicación y división.
while True:
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    print (
        f"{numero1} + {numero2} = {numero1 + numero2}",
        f"{numero1} - {numero2} = {numero1 - numero2}",
        f"{numero1} * {numero2} = {numero1 * numero2}",
        f"{numero1} / {numero2} = {numero1 / numero2}",
        sep= "\n"
    )
    continuar = input("\n¿Deseas realizar otra operación? s/n\n")

    if(continuar.lower() != 's'):
        print("¡Gracias por usar la calculadora!")
        break

# 2. Contador de Palabras: Escribe un programa que cuente la cantidad de palabras en una cadena de texto ingresada por el usuario.

# 3. Conversor de Temperatura: Crea un programa que convierta grados Celsius a Fahrenheit o viceversa, dependiendo de la opción elegida por el usuario.

# 4. Adivina el Número: Haz un juego en el que el programa elija un número aleatorio y el usuario tenga que adivinarlo. El programa debería dar pistas (mayor o menor) hasta que el usuario adivine el número.

# 5. Calculadora de Factorial: Escribe un programa que calcule el factorial de un número ingresado por el usuario.

# 6. Inversor de Cadena: Crea un programa que tome una cadena de texto ingresada por el usuario y devuelva la misma cadena pero invertida.

# 7. Generador de Contraseñas: Haz un generador de contraseñas que combine letras mayúsculas, minúsculas, números y caracteres especiales. El usuario debe poder especificar la longitud de la contraseña.

# 8. Suma de Dígitos: Escribe un programa que sume los dígitos de un número ingresado por el usuario.

# 9. Chequeo de Palíndromo: Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# 10 .Generador de Tablas de Multiplicar: Haz un programa que genere la tabla de multiplicar de un número ingresado por el usuario.