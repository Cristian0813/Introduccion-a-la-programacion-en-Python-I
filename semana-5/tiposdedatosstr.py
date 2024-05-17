#TIPO DE DATOS STRING

# str: Cadenas de texto Cómo representarlas

# ● Se pueden escribir con comillas simples o dobles
print('Con comillas dobles " "')
print("Comillas simples ' '")

""" 
    >> Con comillas dobles ""
    >> Comillas simples '' 
"""
print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# ¿Qué pueden representar? Posibilidades de strings

# ● Nombres
# ● Párrafos de libros
# ● Números de teléfono
# ● Contraseñas
# ● Contenido página web 

#----------------------------------------------------------------------------------------------------

# Concatenación de strings Usando operador "+"

# ● Es posible unir dos strings (concatenar) mediante el símbolo "+" 
# ● Es posible unir dos strings (concatenar) mediante el símbolo "+" 

print("Hola" + " Gente") 
""" >> 'Hola Gente' """ 
print()

string1 = "La casa" 
string2 = " es verde" 
string3 = string1 + string2 
print(string3) 
""" >> La casa es verde """ 
print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

#Repetición de un string Mediante el operador "*"
# ● Se puede concatenar un string consigo mismo una cierta can dad de veces
# ● Esto se hace mediante el operador "*"
# ● Esto se hace mediante el operador "*" 
print("Hola " * 3) 
""" >> HolaHolaHola  """
print()
print("------------------------------------------------------------------------------------------")
print()

#----------------------------------------------------------------------------------------------------

# Inmutabilidad de un string No cambia ante las operaciones

# ● Los Strings son inmutables, es decir, una vez definido un objeto, 
#   este no cambiará a menos que se defina nuevamente 

a = "Martes " 
print(a + "Miércoles") 
print(a)
""" 
>> MartesMiércoles 
>> Martes 
"""
print()

a = "Martes " 
a = a + "Miércoles" 
print(a) 
""" >> MartesMiércoles """