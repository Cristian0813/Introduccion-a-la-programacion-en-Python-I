
# Imprime el resultado en la consola
# print ("Hello world")

# Este es un comentario de una sola línea

"""
Este es un comentario de varias líneas.
Puedes escribir múltiples líneas de texto aquí
sin necesidad de comenzar cada línea con #
"""

# Estas líneas de código son operaciones matematicas de dos números  y los imprime en pantalla
""" resultado = 2 + 2
print("El resultado de la operación es:", resultado)

resultado = 123 * 123
print("El resultado de la operación es:", resultado)

resultado = 20 - 2
print("El resultado de la operación es:", resultado)

resultado = 20 / 2
print("El resultado de la operación es:", resultado)

x = 2
y = 2
res =  x**y
print(f"La suma de x e y es {x+y}") """

""" x=2
y=2
res=x*y
print (f"La multiplicacion de x por y es {res} ")
res=6
res=x*y
print (f"La multiplicacion de x por y es {res} ")

x = 2
y = 2
res = x*y
print (f"La multiplicacion de x por y es {res} ")
x = 6
res = x*y
res = 4 """

# Se está aprendiendo a imprimir en pantalla
# print("Bienvenido a ... ")
# print("""              _                  __
#   ____ ___  (_)  ________  ____/ /
#  / __ `__ \/ /  / ___/ _ \/ __  /
# / / / / / / /  / /  /  __/ /_/ /
#/_/ /_/ /_/_/  /_/   \___/\__,_/
#
#      ______     
#     / ____/     _  _____  __  _  _____ _
#    / /   _____ (_)/____/ / / (_)/__  / /_____
#   / /   / ____/ / /_____/ /_/ /___/ / ____  /
#  / /   / /   / /___  /_   _/ / __  / /   / /
# / /___/ /   / /___/ / / / / / /_/ / /   / /
#/_____/_/   /_/_____/ /_/ /_/_____/_/   /_/  
#
#""")

# Se esta  trabajando con variables globales. 
# No se recomienda en programación funcional o puramente orientada a objetos.
""" nombre = "Cristian"
edad = 33
print("Soy", nombre, end=" ")
print("y tengo", edad, "años")
print("cumplidos")

print("Este print", end=" :D ")
print("no cambia", " de linea", end=";)" ) """

# Variables globales vs locales "Leyendo datos del usuario input()"
""" nombre = input("¿Cúal es tu nombre?")
saludo = "Hola,"
pregunta = "¿Cómo estás el día de hoy?"
print(nombre, saludo, pregunta) """

# Programa que dice cuáto te falta ¿Qué tipo de dato leo?
""" lec = int(input("¿Cuántas lecciones has visto?"))
total = 15
faltan  = total - lec
print("Te faltan", faltan, "lesiones. ¡Ánimo!" ) """

# Ejercicio
""" coste_variable = input("¿Coste variable?")
coste_fijo = "10"
coste_total = coste_fijo + coste_variable """ 

#Conversión de tipos de entradas. Leyendo int, float, bool
""" monedas = int(input("¿Cuántas monedas tienes?"))
siguiente = monedas + 1
print("Yo tengo más, Tengo", siguiente)

t = float(input("¿En cuántos segs corres 100m?"))
dif = t - 9.58
print("Eres ", dif, "segundos más lentos que Bolt.")

ingreso = bool(input("Ingresa tu nombre: "))
print("Nombre ingresado: ", ingreso) """

print("¿Cuantos billetes de $1000 tienes?")
a = input()
print("Tienes" + str(int(a) * 1000) + " pesos en billetes de $1000")