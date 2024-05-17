
# Pregunta 1 ¿Qué carácter especial señala un salto de línea?

""" (x) \n """

#------------------------------------------------------------------------------------------

# Pregunta 2 ¿Cuál es el orden correcto para realizar estas acciones?

""" (x) Abrir archivo - Leer archivo - Cerrar archivo """

#------------------------------------------------------------------------------------------

# Pregunta 3 ¿Cuál de estas expresiones indica, como segundo parámetro de la función open, el modo solo lectura?

"""(x) r"""

#------------------------------------------------------------------------------------------

# Pregunta 4 Si un archivo llamado "ejemplo.txt" contiene lo siguiente:
# La lengua de la
# ballena azul pesa lo mismo
# que un elefante
# ¿Qué imprimen las siguientes líneas?

ejemplo = open("ejemplo.txt", "r")
a = ejemplo.readline()
b = ejemplo.readline()
c = ejemplo.readline()
d = a + c
print(d)

""" 
(x) La lengua de la
    que un elefante
 """
print()
print("---------------------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------------------

# Pregunta 5 ¿Por qué NO es válido el siguiente código?
# archivo = open(archivo.txt, "r")
# archivo.close()

""" 
    (x) Porque el nombre del archivo no está en formato string.
"""

#------------------------------------------------------------------------------------------

# Pregunta 6 Si tenemos un archivo "mooc.txt" que tiene el siguiente contenido:

# MOOC 
# significa
# Massive
# Open
# Online
# Course

# y ejecutamos el siguiente código:

a = open("mooc.txt")
linea = a.readline()
linea = a.readline()
linea = a.readline()
linea = a.readline()

# ¿Qué contendrá la variable linea al final del código?

print(linea)

"""
    (x) "Open"
"""


print()
print("---------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------

# Pregunta 7 Si tenemos el siguiente código, ¿cuál será el resultado, que quedará guardado en el archivo mooc.txt?

a = open("mooc2.txt", "w")
a.write("1 2 3 4")
a.write("5 6 7 8")
a.close()

mooc = open("mooc2.txt", "r")
lectura = mooc.read()
mooc.close()
print(lectura)

""" 
    (x) 1 2 3 45 6 7 8
"""

print()
print("---------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------

# Pregunta 8 ¿Cuál es la instrucción correcta si queremos convertir todo el contenido de un archivo 
# "direcciones.txt" a un string s?

""" 
    (x) s = open("direcciones.txt").read()
"""

#------------------------------------------------------------------------------------------

# Pregunta 9 ¿Por qué no es correcto el siguiente código?

# a = open("mi_nombre.txt")
# a.write("Me llamo Luis")
# a.close()
# print(a)

""" 
    (x) Porque estamos escribiendo en un archivo solo de lectura.
"""

#------------------------------------------------------------------------------------------

# Pregunta 10 ¿Cuál es el código correcto para leer (e imprimir en pantalla) 
# un archivo que sea elegido por el usuario?

""" 
    (x) s = input("Ingresa nombre archivo: ")
        t = open(s)
        l = t.readline()
        while l!="":
        print(l)
        l=t.readline()
"""


