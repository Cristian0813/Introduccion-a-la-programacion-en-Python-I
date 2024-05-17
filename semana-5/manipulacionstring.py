# MANIPULACIÓN STRINGS 

# Acceso a elementos mediante índices string [índice] 
# ● Es posible seleccionar ciertos elementos de un string según su posición en él 
# ● Los índices comienzan en 0 (i.e.: el primer elemento está en la posición 0) 
# ● Los índices comienzan en 0 (i.e.: el primer elemento está en la posición 0) 

print("Martes"[0]) 
""" >> M """
print()

# ● Los índices comienzan en 0 (i.e.: el primer elemento está en la posición 0) 

a = "La casa es verde" 
print(a[5]) 
""" >> s""" 
print()

# ● Se pueden seleccionar los símbolos del final con números negativos (posición -1 es última letra, decrecen hacia la izquierda)
print("Martes"[5]) 
print("Martes"[-1]) 
""" 
    >> s
    >> s
"""

print()
print("------------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------------- 

# Acceso a "subpalabras" string[inicio:final]
 
# ● Podemos también seleccionar un cierto intervalo de símbolos del string 
#   indicándolo como string[inicio:final+1] 
# ● Esto es conocido como slicing online.ing.puc.cl Acceso a "subpalabras" string[inicio:final] 
# ● Podemos también seleccionar un cierto intervalo de símbolos del string 
print("Martes"[1:4]) 
""">> art""" 

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# Símbolos Especiales Uso de símbolo "\" para escapar elementos 

# ● Existen ciertos símbolos que no pueden escribirse directamente con el teclado (como una línea nueva) 
# ● Para esto se ocupa el símbolo "\" en conjunto con alguna letra para indicarlos 

# Ejemplos 
# "\n": indica una nueva línea 
print("Un párrafo.\nOtro párrafo.") 
""" 
    >> Un párrafo. 
    >> Otro párrafo
""" 
print()

# Ejemplos "\\": para escribir una sola vez "\" 
print("Para escribir un backslash, poner dos \\") 
"""
    >> Para escribir un backslash, poner dos \
""" 