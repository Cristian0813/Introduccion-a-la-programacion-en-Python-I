# Pregunta 1 De estas expresiones, ¿cuál NO es un string válido?
#  Hint: Recuerda como el computador interpreta que algo es un string o no. 

""" (x) Martes """

#----------------------------------------------------------------------------------------------------


# Pregunta 2 ¿Qué imprimiría las siguientes líneas de código?

a = "49" + "10"
print(a)

# Imprime
""" >> 4910 """

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# Pregunta 3 Al ejecutar el siguiente código:

print("MmM" * 4)

# Se imprime "MmmmmM"

""" (x) Falso """

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 4 Si al ejecutar el siguiente código

a = "notar"
b = a.replace("v","n")
print(b)

# se imprime "notar", determina cuál o cuáles de las siguientes opciones corresponden a 
# posibles valores de la variable a. 

""" 
  (x) notar
  (x) votar 
"""


print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 5 ¿Qué imprimiría las siguientes líneas de código?

a = "oso pardo"
b = a.strip("o")
print(b)

""" (x) so pard """

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 6 ¿Cuál de estos métodos retornaría exactamente el string "ANIMALES"?

print("ANIMALES".upper())
print("AniMALeS".upper())

""" (x) "ANIMALES".upper() """

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 7 ¿Qué imprimirían las siguientes líneas de código?

a = "Barcelona 92"
print(a[1])

""" (x) a """ 

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 8 Dado el siguiente código,

s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
print(t)

# ¿Qué se imprime? (Escríbelo sin comillas; recuerda usar las mayúsculas y minúsculas que correspondan)

""" (x) aso hubA """

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 9 ¿Qué imprime el siguiente código?

s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i<len(s):
  resultado= resultado + s[len(s)-i-1]
  i=i+1
print(resultado)
  
""" (x) Imprime la palabra que ingresó el usuario, pero en orden inverso. """

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------


# Pregunta 10 Si s =  "hola que tal", ¿cuál es el valor de len(s)?

s = "hola que tal"
print(len(s))

""" (x) 12 """