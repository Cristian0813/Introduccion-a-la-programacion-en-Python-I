# Reutilizando código 

# Objetivo: Reutilizar código mediante funciones 

# • ¡Podemos copiar y pegar! 
# • Es posible, pero es fácil cometer errores 
# • Debemos repetir cualquier cambio

# Concepto de función 

# Usando for para imprimir texto consecutivo 

total = 3 
unidad ="días" 
for i in range(total): 
    print("Han pasado "+ str(i), unidad)

print()
print("----------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Imprime
# Han pasado 0 días 
# Han pasado 1 días 
# Han pasado 2 días

# Si queremos escribir meses…

total = 3 
unidad = "días" 
for i in range(total): 
    print("Han pasado " + str(i), unidad) 
total = 4 
unidad = "meses" 
for i in range(total): 
    print("Han pasado " + str(i), unidad) 
total = 10 
unidad = "meses" 
for i in range(total): 
    print("Han pasado " + str(i), unidad)

print()
print("----------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Reutilizar código

# Si tenemos una función que pueda hacer este trabajo por nosotros 

# recordatorio(3, "días") 
# recordatorio(5, "meses") 
# recordatorio(10, "segundos") 

# Útil para no repetir código.

#-----------------------------------------------------------------------------------------------------

# Funciones existentes

# Ya hemos usado funciones anteriormente 
print("Esto es una función") 
input("Ingrese su nombre: ")

print()
print("----------------------------------------------------------------------------------")
print()

# La función print recibe como 
# parámetro uno o más string y 
# los muestra en pantalla 

string1 = "Pearl" 
string2 = "Jam" 
print(string1, string2) 

# Imprime
# Pearl Jam

print()
print("----------------------------------------------------------------------------------")
print()

# La función input recibe como parámetro un stringy le pide al usuario que ingrese contenido 

string= "Dime tu edad: " 
edad = input(string) 
print("Tienes",edad,"años:D")

# Imprime
# Dime tu edad: 38 Tienes 38 años :D

#-----------------------------------------------------------------------------------------------------

# ¿Qué es?

# Función 

# Fragmento de código que recibe parámetros, 
# ejecuta acciones, y retornan un resultado.

#-----------------------------------------------------------------------------------------------------

# Equivalente matemático

# Las funciones pueden ser entendidas 
# igual que en el ámbito matemático: 
#     f(x,y) = x² + y²
# Recibe elementos de entrada x e y, 
# entrega un valor de salida, y una 
# fórmula permite obtener este valor.


# En Python, es equivalente: 

#      ______________________ _____________________
#     |  Función matemática  |  Función de Python  |
#     |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯| 
#     | Elementos de entrada | Parámetros          |
#     | Fórmula              | Código              |
#     | Valor de salida      | Retorno             |
#      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 
#-----------------------------------------------------------------------------------------------------

# Resumiendo 
# • Concepto de función 
# • Reutilización de código 
# • Recibe parámetros, ejecuta acciones y retorna un resultado