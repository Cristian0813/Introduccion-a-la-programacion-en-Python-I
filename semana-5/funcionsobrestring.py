# MÉTODOS SOBRE STRINGS

# Métodos propios de strings 
# Introducción 

# • Todo po de dato en Python posee ciertos métodos predefinidos 
# • Son funciones muy ú les y comunes 

# Métodos propios de strings len(str) 

# • Uno de los métodos más útiles y comunes es len (abreviado de length, longitud) 
# • Retorna el largo del string que se pase como parámetro 

print(len("Martes")) 
print(len("Yo soy.")) 

"""
    >> 6
    >> 7 
"""
print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# Métodos propios de strings str.upper() y str.lower()

# • Para pasar todo un string a mayúsculas o minúsculas, 
#   se puede invocar a los métodos 
#   string.upper() y 
#   string.lower(), respectivamente 
# • Para pasar todo un string a mayúsculas o minúsculas... 
print("Martes".upper()) 
print("MArtes".lower()) 
"""
    >> MARTES
    >> martes
""" 
print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# Métodos propios de strings str.strip(char)
 
# • Para remover algún símbolo de los extremos del string, existe el método strip, 
#   con el símbolo como parámetro 
# • El método strip, con el elemento a remover como parámetro 
a = "Bien. Martes a las 5." 
print(a.strip(".")) 
"""
    >> Bien. Martes a las 5
"""

print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# Métodos propios de strings str.replace(viejo, nuevo) 
# • Para reemplazar algún símbolo del string, existe el método replace, con el símbolo antiguo y el nuevo como parámetros 
# Replace 
a = "Hola!!1!" 
print(a.replace("1", "!")) 
"""
    >> Hola!!!!
""" 
