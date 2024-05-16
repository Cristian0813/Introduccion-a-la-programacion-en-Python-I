# INVOCACIÓN Y SCOPE DE FUNCIONES

#Invocación ¿Qué es? 
# • La invocación o llamado se realiza cuando se quiere ejecutar la función definida. 
# • Sin invocación, el código nunca se ejecuta.

#-------------------------------------------------------------------------------------------------------------------------

# Error común 
cuenta(3) 
def cuenta(tope): 
    i = 0 
    while i < tope: 
        print(i) 
        i += 1

# Imprime >>> NameError: name ‘cuenta' is not defined

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Invocación Caso correcto 
def cuenta(tope): 
    i = 0 
    while i < tope: 
        print(i) 
        i += 1 
cuenta(3)

# Imprime 
# > 0 
# > 1 
# > 2

print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Invocación Utilizar el llamado 
# Se puede, opcionalmente, igualar un llamado de función a una variable: 

def calculo(numero): 
    resultado = (numero - 3) ** 3 
    return resultado 
salida = calculo(5) 

# Ahora se tiene en salida el valor de resultado


print()
print("--------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------------------------------------

# Scope ¿Qué es? 
# • El scope de una función corresponde al manejo de las variables dentro de la misma. 
# • Variables definidas dentro de una función no existen fuera de ella. 

#-------------------------------------------------------------------------------------------------------------------------

# Ejemplo 
def es_par(numero): 
    divisor = 2 
    if numero % divisor == 0: 
        return True 
    else: 
        return False 
print(divisor) 

# Imprime
# >>> NameError: name ‘divisor' is not defined 

#-------------------------------------------------------------------------------------------------------------------------

#Consideraciones 
# • Que las variables “mueran” al terminar la función evita errores. 
# • Se les llama variables locales, y solo existen dentro de la función que las define. Consideraciones 
# • Las variables fuera del scope de la función, se pueden utilizar pero no modificar. 
# • Fuera del scope: variables que no fueron definidas en la función.

#-------------------------------------------------------------------------------------------------------------------------

# Ejemplo 1
def fx(numero): 
    print(numero * factor) 
factor = 0.5 
fx(3) 
print(factor) 

# Imprime 
# > 1.5 
# > 0.5 

# Ejemplo 2
def fx2(numero): 
    factor += 0.1 
    print(numero * factor) 
factor = 0.5 
fx2(3) 

# Imprime 
# >>> UnboundLocalError: local variable 'factor' referenced before assignment 

# Ejemplo 3
def fx3(numero): 
    factor = 0.9 
    print(numero * factor) 
    factor = 0.5 
fx3(3) 
print(factor) 

# Imprime 
# > 2.7 
# > 0.5

# Ejemplo 4 
def fx4(numero): 
    print(numero * factor) 
    factor = 0.5 
fx3(3) 
fx4(3) 
# Imprime 
# > 2.7 
# > 1.5 

#-------------------------------------------------------------------------------------------------------------------------

# Resumiendo 
# • Variables definidas en una función son locales. 
# • Dentro de una función se pueden leer variables de un scope mayor o externo, pero no modificarlas.