# ESCRIBIENDO EN PANTALLA PRINT

# Escribiendo en pantalla 
# ¿Cómo comunico un resultado? 
#
#>>>pesos_por_hora= 200 
#>>>llegada = 20 
#>>> salida = 22 
#>>> precio = (salida-llegada)*pesos_por_hora 
#>>> precio Salida 400
pesos_por_hora = 200
llegada = 20
salida = 22
precio = (salida - llegada) * pesos_por_hora
print("El precio del estacionamiento  es:", precio, "pesos")

#                         | Memoria |
#       __________________|---------|
#       \  pesos_por_hora |   200   |
#       -\----------------|---------|
#       \      llegada    |    20   |
#       -\----------------|---------|
#       \      salida     |    22   |
#       -\----------------|---------|
#       \       precio    |   400   |
#        \----------------|---------|

# Escribiendo en pantalla
# imprimir en pantalla print(expresión) 
# 
# print("Hola mundo") Salida Hola mundo 
print("Hola mundo")
#
# mensaje = "Hola mundo" 
# print(mensaje) Salida Hola mundo
mensaje = "Hola mundo"
print(mensaje)
#
# imprimir expresiones 
# print((3+5//4-2)-2**4+3*(7-2)) Salida 1
print((3+5//4-2)-2**4+3*(7-2))
#
# imprimir variables calculadas previamente
# fahrenheit= 91 
# celsius= (fahrenheit-32) * 5/9 
# print(celsius) Salida 32.77777777777778
fahrenheit= 91 
celsius= (fahrenheit-32) * 5/9 
print(celsius)
# 
# imprimir expresiones con variables
# temperatura = 33 
# print(temperatura >= 30) Salida True
temperatura = 33 
print(temperatura >= 30)


# Escribiendo en la misma línea print(expr, expr, ...)
#
# episodio = 3 
# print("Episodio") Salida Episodio
# print(episodio) Salida 3 
# print("del libro") Salida del libro
episodio = 3 
print("Episodio") 
print(episodio) 
print("del libro")

# imprimir múltiples expresiones
# episodio = 3
# print("Episodio", episodio, "del libro") Salida Episodio 3del libro
episodio = 3
print("Episodio", episodio, "del libro")

# Cambiando el fin de línea print(expr, end=str)
#
# cambiar el término de línea
# nombre = "Cristian"
# edad = 38
# print("Soy", nombre, end=" ")
# print("y tengo", edad, "años")
# print("cumplidos") Salida Soy Cristian y tengo 38 años cumplidos
nombre = "Cristian"
edad = 38
print("Soy", nombre, end=" ")
print("y tengo", edad, "años")
print("cumplidos")
#
# print("Este print", end=" :D ") 
# print("no cambia", "de línea", end=";)") Salida Este print:D no cambia de línea;)
print("Este print", end=" :D ") 
print("no cambia", "de línea", end=";)")

# Cambiando el separador print(expr, sep=str)
#
# msj1 = "Hoy habrá"
# temp= 34
# msj2 = "grados"
# print(msj1, temp, msj2) Salida Hoy habrá 34 grados
msj1 = "Hoy habrá"
temp= 34
msj2 = "grados"
print(msj1, temp, msj2)
#
# cambiar el separador de expresiones
# print("-El tesoro", "está", "en", sep="...") Salida -El tesoro...está...en
print("-El tesoro", "está", "en", sep="...")


# SSALUDANDO AL USUARIO
#
#• Problema:Programa que salude al usuario
#saludadorNick.py
# nombre = "Dr. Nick"
# saludo = "Hola,"
# pregunta = "¿cómo estás hoy?"
# print(saludo, nombre, pregunta) Salida Hola, Dr. Nick ¿cómo estás hoy?
nombre = "Dr. Nick"
saludo = "Hola,"
pregunta = "¿cómo estás hoy?"
print(saludo, nombre, pregunta)
#
#saludadorValeria.py
# nombre = "Valeria"
# saludo = "Hola,"
# pregunta = "¿cómo estás hoy?"
# print(saludo, nombre, pregunta) Salida Hola, Valeria ¿cómo estás hoy?
nombre = "Valeria"
saludo = "Hola,"
pregunta = "¿cómo estás hoy?"
print(saludo, nombre, pregunta)

# Programa que saluda al usuario ¿Cómo obtengo el nombre del usuario?
# 
# Entrada (input) ➡️      💻💻💻      ➡️  Resultado (output)  
# Jorge            saludador.py Programa    Hola, Jorge ¿cómo estás hoy? 


#saludador.py
# nombre = input("¿Cuál es tu nombre?")
# saludo = "Hola," 
# pregunta = "¿cómo estás hoy?" 
# print(saludo, nombre, pregunta) Salida ¿Cuál es tu nombre? Jorge Hola, Jorge ¿cómo estás hoy?
nombre = input("¿Cuál es tu nombre? ")
saludo = "Hola," 
pregunta = "¿cómo estás hoy?" 
print(saludo, nombre, pregunta)
#
# obtener datos de entrada 
# variable= input(texto)
#
# nombre = input("¿Cuál es tu nombre?")
# saludo = "Hola," 
# pregunta = "¿cómo estás hoy?" 
# print(saludo, nombre, pregunta) Salida ¿Cuál es tu nombre? Mar Hola, Mar ¿cómo estás hoy?
nombre = input("¿Cuál es tu nombre? ")
saludo = "Hola," 
pregunta = "¿cómo estás hoy?" 
print(saludo, nombre, pregunta)
#

# Programa que dice cuánto te falta ¿Qué tipo de dato leo? 
# obtener datos de entrada variable= input(texto) 

#lec= input("¿Cuántas lecciones has visto? ") 
# total = 15 
# faltan = total - lec 
# print("Te faltan ", faltan, "lecciones. ¡Ánimo!") 
# Salida File "lecciones.py", line 3, in <module> 
#       faltan= total -lec TypeError: unsupported operand type(s) for -: 'int' and 'str' 
lec= input("¿Cuántas lecciones has visto? ") 
total = 15 
faltan = total - lec 
print("Te faltan ", faltan, "lecciones. ¡Ánimo!")

# Programa que dice cuánto te falta input() siempre entrega str 
#
# obtener datos de entrada 
# variable= input(texto) 
#
# lec= input("¿Cuántas lecciones has visto? ") 
# print(type(lec)) Salida ¿Cuántasleccioneshas visto? <class 'str'>
lec= input("¿Cuántas lecciones has visto? ") 
print(type(lec)) 
#
# • input siempre entrega un str

# Conversión de tipos al rescate Conversión a int 
# obtener datos de entrada 
# variable= input(texto)
#
# lec= int(input("¿Cuántas lecciones has visto? ")) 
# total = 15 
# faltan = total - lec 
# print("Te faltan ", faltan, "lecciones. ¡Ánimo!") Salida ¿Cuántas lecciones has visto? 10 Tefaltan 5 lecciones. ¡Ánimo!
lec= int(input("¿Cuántas lecciones has visto? ")) 
total = 15 
faltan = total - lec 
print("Te faltan ", faltan, "lecciones. ¡Ánimo!")

# Conversión de tipos de entrada Leyendo int, float, bool 
#
# monedas = int(input("¿Cuántas monedas tienes? ")) 
# siguiente = monedas + 1 
# print("Yo tengo más. Tengo", siguiente) 
monedas = int(input("¿Cuántas monedas tienes? "))
siguiente = monedas + 1 
print("Yo tengo más. Tengo", siguiente) 

# t= float(input("¿En cuantos segscorres 100m? ")) 
# dif= t - 9.58 
# print("Eres ", dif, "segundos más lento que Bolt") 
t= float(input("¿En cuantos segscorres 100m? ")) 
dif= t - 9.58 
print("Eres ", dif, "segundos más lento que Bolt") 

# ingreso = bool(input("Ingresa tu nombre: ")) 
# print("Nombre ingresado: ", ingreso)
ingreso = bool(input("Ingresa tu nombre: ")) 
print("Nombre ingresado: ", ingreso)