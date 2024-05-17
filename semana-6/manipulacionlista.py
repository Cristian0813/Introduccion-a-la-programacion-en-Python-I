# ACCEDIENDO ELEMENTOS TIPO LIST


# Modificando la lista Lis
# ta son mutables lista 

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 

# Objetivo: Manipular elementos de listas 

# • Listas son mutables (no como str) 
# • Modificar elementos 
# • Acceder a elementos 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Posiciones dentro de la lista 

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000]

# no_olvidar                                                                    
#    ┌──────────┬─────────┬───────────┬────────────┬──────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │
#    └──────────┴─────────┴───────────┴────────────┴──────┘
#        [0]        [1]        [2]          [3]      [4] 


# • Los elementos de una lista están ordenados 
# • Cada elemento tiene una posición ó índice 
# • Posiciones empieza en 0 
# • Posiciones dentro de la lista son int 

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 
print(no_olvidar[2])
""" 
    >> lechuga 
"""

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Posiciones dentro de la lista no_olvidar "huevos" "palta" "lechuga" "naranjas" 7000 [0] [1] [2] [3] 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Secciones (slices) de la lista no_olvidar "huevos" "palta" "lechuga" "naranjas" 7000 [0] [1] [2] [3] [4] 

# no_olvidar                                                                    
#    ┌──────────┬─────────┬───────────┬────────────┬──────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │
#    └──────────┴─────────┴───────────┴────────────┴──────┘
#        [0]        [1]        [2]          [3]      [4] 

# • Podemos acceder a secciones (slice) de la lista 
no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 
print(no_olvidar[1:4]) 
"""
    >> ['palta', 'lechuga', 'naranjas'] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Obteniendo secciones de listas Slicing 
#Notación de slicing
 
# ┌────────────────────────┐
# │ lista[inicio:fin:step] │
# └────────────────────────┘ 

# • Desde lista[inicio] hasta lista[fin-1], en pasos de step 
letras = ["a","b","c","d","e","f","g","h","i","j"] 
#          0   1   2   3   4   5   6   7   8   9
 
print(letras[2:7]) 
print(letras[2:7:2]) 
print(letras[7:]) 
print(letras[:5:3]) 
print(letras[2:2]) 
print(letras[::-1]) 
""" 
    >> ['c','d','e','f','g'] 
    >> ['c','e','g'] 
    >> ['h','i','j'] 
    >> ['a','d'] 
    >> [] 
    >> ['j','i','h','g','f','e', 'd','c','b','a'] 
""" 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Recorriendo listas 
# Listas con for 

# • Podemos recorrer una lista con la construcción 
# for-in

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
for elem in no_olvidar: 
    print("No olvides", elem) 

"""
    >> No olvides huevos 
    >> No olvides palta 
    >> No olvides lechuga 
    >> No olvides naranjas 
    >> No olvides 7000
""" 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Mutabilidad 
# Modificando elementos de lista 

# • Podemos modificar los valores de cada posición 

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar[1] ="queso" 
no_olvidar[3] = 10000 
print(no_olvidar) 
"""
    >> ['huevos', 'queso', 'lechuga', 10000, 7000] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Resumiendo 
# Manipulación de elementos de lista 

# • Acceder a un elemento: posición 
# • Seleccionar una sección de la lista: slicing 
# • Recorrer los elementos: for-in 
# • Modificar los valores de cada posición