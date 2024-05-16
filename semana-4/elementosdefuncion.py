# CONCEPTO Y USO DE FUNCIONES
# ELEMENTO DE UNA FUNCIÓN

# Funciones

# Parámetros 
# ¿Qué son? 

# • Elementos que recibe una función para trabajar con ellos. 
# • Variables que usa la función. 
# • Se entregan al llamar a la función, según la necesidad.

 
#-----------------------------------------------------------------------------------------------------

# Parámetros 
# ¿Dónde se escriben? 

# Al definir una función 
# def func(parametro1, parametro2, ...): 
#     ... 
#     ... 

# La cantidad de pará metros y sus 
# nombres quedan determinados al 
# escribir el código de la función.

# Al llamar a una función, se entregan 
# los datos o variables que se utilizarán 
# como valores de los parámetros 
# variable1 = 1 
# variable2 = 2 
# func(variable1, variable2) 

#-----------------------------------------------------------------------------------------------------

# Valor de retorno 
# “Resultado” de una función 

# • Valor que entrega la función al terminar de ejecutarse. 
# • Se pueden igualar a una variable. 
# • Se utiliza la palabra clave return. 

 
#-----------------------------------------------------------------------------------------------------

# Valor de retorno 
# Término de una función 

# • Una vez que el programa llega al retorno, se termina la ejecución de la función. 
# • La línea después del retorno nunca se ejecutará: 

def funcion(): 
    return "Aquí se termina" 
print(5) 

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Valor de retorno 
# En el código 

# La siguiente función recibe un número, le resta 3 y 
# luego lo eleva al cubo, para después retornarlo: 

def calculo(numero): 
    resultado = (numero - 3) ** 3 
    return resultado 

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Valor de retorno 
# Utilización 

# Si se llama la función sin hacer más, en pantalla no se verán cambios: 

def calculo(numero): 
    resultado = (numero - 3) ** 3 
    return resultado 
calculo(8) 

print()
print("----------------------------------------------------------------------------------------------")
print()

def calculo(numero): 
    resultado = (numero - 3) ** 3 
    return resultado 
print(calculo(8)) 
salida = calculo(5) 
print(salida + 100) 

# Imprime
# > 125 
# > 108 

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Parámetros y retorno 
# Funciones booleanas 

# • Reciben uno o más parámetros de algún tipo, y retornan True o False. 
# • Un ejemplo, es el de una función para saber si un número es par. 

def es_par(numero): 
    if numero % 2 == 0: 
        return True 
    else: 
        return False 
print(es_par(8)) 
print(es_par(7)) 

# Imprime
# > True 
# > False 

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Resumiendo 

# • Parámetros son aquello que la función recibe para poder trabajar dentro de la función. 
# • Retorno es aquello que la función entrega para terminar la ejecución de la función.