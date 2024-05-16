# IMPORTACIÓN DE MÓDULOS Y LLAMADO DE FUNCIONES


# Módulos existentes 
# Mucho trabajo ya está hecho 

# • Existen muchas librerías o módulos ya programados. 
# • Realizan de todo tipo de tareas, simples o complejas. 

# Ejemplos 

# • randomy math son ejemplos. 
# • Permiten realizar acciones u operaciones cotidianas con un simple llamado a una función. 

#-----------------------------------------------------------------------------------------------------

# Módulos existentes 
# Como importarlos 

# • Primer método: 
# import <nombre modulo> 

# Ejemplo: 
# import math 

import math
print(math.sqrt(25))  

# Imprime 
# >  5.0
print()
print("----------------------------------------------------------------------------------------------")
print()

# • Segundo método: 
# from <nombre módulo> import <elemento1>, <elemento2> 

# Ejemplo: 
# from math 
# import pow, sqrt 

from math import pow, sqrt
print(pow(2, 3))  
print(sqrt(16))
# Imprime 
# >  8.0
# >  4.0
print()
print("----------------------------------------------------------------------------------------------")
print()

# • Tercer método: 
# from <nombre módulo> import <elemento1> as <alias> 

# Ejemplo: 
# from math import e as euler 

from math import e as euler
print(euler)
# Imprime 
# Valor de e (aprox. 2.71828)
print()
print("----------------------------------------------------------------------------------------------")
print()

# • Cuarto método (no recomendado): 
# from <nombre módulo> import * 

# Ejemplo: 
# from math import * 

from math import *
print(sin(pi/2))  
# Imprime 
# >1.0
print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Funciones importadas 
# Como llamarlas 

# • Con el primero: 
# import modulo modulo.funcion(argumentos) 

# Ejemplo: 
# import math math.sin(0) 

# • Con el segundo y cuarto método: 
# from modulo import funcion funcion(argumentos) 

# Ejemplo: 
# from random import uniform uniform(0, 1) 

# • Con el tercer método: 
# from modulo import funcion as mifun mifun(argumentos) 

# Ejemplo: 
# from random import randint as rnd rnd(5, 10) 

# Módulos, funciones y constantes 
# Utilidad de las librerías 

# • randompermite generar números pseudoaleatorios. 
# • mathpermite realizar cálculos complejos y acceder a constantes conocidas. 

# Ejemplo completo 
from random import randint as rnd 
from math import pi, e 
lanzamiento = rnd(1, 6) 
if lanzamiento < 4: 
    print(pi * lanzamiento) 
else: 
    print(e * lanzamiento) 

# Imprime
# > 6.283185307179586
    
# Resumiendo 
# • Existen módulos muy útiles incorporados en Python. 
# • Se pueden importar de diversas formas según la comodidad. 
# • Evitan programación extra.