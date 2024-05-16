# MÓDULOS DE FUNCIONES

# Concepto de módulo 
# ¿Qué es? 
# • Un archivo Python con la extensión .py es un módulo. 
# • Los módulos tienen conjuntos de funciones y constantes importables desde cualquier otro programa. 

#-------------------------------------------------------------------------------------------------------------------------

# Concepto de módulo Uso 
# Como ya hemos visto, un módulo se importa, entre otras formas, así: 
from modulo import elementos 
#o 
import modulo 

#-------------------------------------------------------------------------------------------------------------------------

# Módulos propios Creando 
# • Similarmente, si creamos un archivo con extensión .py, podrá ser importado de la misma forma 
# • Basta con tener en ese archivo las funciones y constantes deseadas. 

#-------------------------------------------------------------------------------------------------------------------------

# Módulos propios 
# Ejemplo Si se tienen dos archivos creados por nosotros de la siguiente manera:

# modulo_funciones.py
# programa.py
 
# • Funciones y constantes irán en el archivo modulo_funciones.py 
# • Se importarán desde programa.py 

# Ejemplo 1
# modulo_funciones.py 
#         ↓
def es_par(numero): 
    if numero % 2 == 0: 
        return True 
    else: 
        return False

# Ejemplo 2 
# programa.py 
#     ↓
from modulo_funciones import es_par 

numero = int(input("Ingrese n°: "))
if es_par(numero): 
    print("Su número es par!") 
else: 
    print("Su número es impar!")
    
#-------------------------------------------------------------------------------------------------------------------------
     
# Consideraciones 
# • Cuando hay muchas funciones, es muy útil. 
# • La separación definición / utilización clarifica y ordena, sobretodo en proyectos grandes. 
# • Existen muchos módulos preexistentes como los ya vistos, random y math. 
# • Al crear módulos: fijarse en la ubicación de los archivos.