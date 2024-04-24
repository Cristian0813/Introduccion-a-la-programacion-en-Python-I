# 1. Calculadora Simple: Crea un programa que solicite dos números al usuario y realice operaciones básicas como suma, resta, multiplicación y división.
""" while True:
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
        break """

# 2. Contador de Palabras: Escribe un programa que cuente la cantidad de palabras en una cadena de texto ingresada por el usuario.

# 3. Conversor de Temperatura: Crea un programa que convierta grados Celsius a Fahrenheit o viceversa, dependiendo de la opción elegida por el usuario.

# 4. Adivina el Número: Haz un juego en el que el programa elija un número aleatorio y el usuario tenga que adivinarlo. El programa debería dar pistas (mayor o menor) hasta que el usuario adivine el número.

# 5. Calculadora de Factorial: Escribe un programa que calcule el factorial de un número ingresado por el usuario.

# 6. Inversor de Cadena: Crea un programa que tome una cadena de texto ingresada por el usuario y devuelva la misma cadena pero invertida.

# 7. Generador de Contraseñas: Haz un generador de contraseñas que combine letras mayúsculas, minúsculas, números y caracteres especiales. El usuario debe poder especificar la longitud de la contraseña.

# 8. Suma de Dígitos: Escribe un programa que sume los dígitos de un número ingresado por el usuario.

# 9. Chequeo de Palíndromo: Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# 10 .Generador de Tablas de Multiplicar: Haz un programa que genere la tabla de multiplicar de un número ingresado por el usuario.


# h-o-l-a- -q-u-e- -t-a-l
# 0-1-2-3-4-5-6-7-8-9-10-11 =12

datos = [2, "Julio", 2017, "Final", 14.5, "Chile", 0, "Alemania", 1]
trozo = datos[2:6]
print(trozo)

lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"]
lista_compras.append("maní")  # Agrega "maní" al final de la lista
lista_compras.remove("arroz")  # Remueve "arroz" de la lista
lista_compras.insert(2, "leche")  # Inserta "leche" en la posición 2 de la lista

print(lista_compras)  # Imprime la lista actualizada

datos = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
print(trozo)

unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = unidades[2:3] + unidades[3:7:3] + unidades[7:8]
muestra2 = unidades[2:4] + unidades[6:8]
print(muestra)
print(muestra2)

contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")

print(splitted)

pintura = list(range(1, 101))  # Genera la lista de números del 1 al 100

# Selecciona los elementos 6, 14 y 20 de la lista
sol = pintura[5:21:5]

# Selecciona los elementos 6, 14, 20 y 26 de la lista
sol2 = pintura[5:26:5]

print(sol)
print(sol2)

# 6, 11, 16, 3, 8, 14


import math

def promedio_std(lista):
    # Calcula el promedio
    promedio = sum(lista) / len(lista)
    
    # Calcula la suma de los cuadrados de las diferencias respecto al promedio
    suma_cuadrados_diff = sum((x - promedio) ** 2 for x in lista)
    
    # Calcula la desviación estándar
    desviacion_estandar = math.sqrt(suma_cuadrados_diff / len(lista))
    
    # Retorna el promedio y la desviación estándar
    return promedio, desviacion_estandar

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
promedio, std_dev = promedio_std(numeros)
print("Promedio:", promedio)
print("Desviación estándar:", std_dev)
