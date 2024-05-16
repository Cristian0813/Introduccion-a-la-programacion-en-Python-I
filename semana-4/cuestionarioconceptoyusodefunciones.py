# Pregunta 1 ¿Con qué palabra se especifica el valor que queremos que la función nos devuelva?
""" (x) return """

#-----------------------------------------------------------------------------------------------------

# Pregunta 2 Dada la siguiente función,

def divis(a,b):
  c = a//b
  d = b//a
  resultado = c+d
  return resultado

# ¿Cuál es/son sus parámetros?

print("a, b")

# Respuesta
# (x) a, b

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 3 ¿Qué retorna la siguiente función, para x = 102, y para x=103?

def funcion_misteriosa(x):
  for i in range(2,x):
    if x % i == 0:
      return False
  return True

x=102
x=103

# Respuesta
# (x) x = 102, retorna False
#     x = 103, retorna True

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 4 Si queremos importar la función randint del módulo random, ¿cuál es/son formas correctas de hacerlo, y de luego utilizar la función?

import random
a = random.randint(1,10)
print("Valor de a utilizando 'import random': ", a)

from random import randint
a = randint(1,10)
print("Valor de a utilizando 'from random import radint': ", a)

from random import *
a = randint(1,10)
print("Valor de a utilizando 'from random import *': ", a)

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 5 ¿Qué hace la siguiente función? 

def funcion_misteriosa(x):
  c=0
  while x!=0:
    c+=1
    x = x//10
  return c

x = 12345

print(" Retorna el número de dígitos del número ", x)

# Respuesta
# Retorna el número de dígitos del número x

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

#Pregunta 6 ¿Cuál/es de las siguientes es una definición de función que SÍ es válida?

def hola(chao):
    print(chao)

def blabla():
    pass

def m_90(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------



# Pregunta 7 ¿Cuál código es correcto para una función que reciba un número N y entregue 1+2+3+4+...+N?

def suma(N):
  s=0
  for i in range(N):
    s+=i
  return s+N
N = 10  
resultado = suma(N)
print("El resultado de la suma de 1+2+3+...+N para N =", N, "es:", resultado)

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 8 Indica cuál es la línea de código incorrecta en la siguiente función.

def f(x,y):
  print("Funcion f")
  return x**2+y**2
  print("Final de la función")
  
# Resultado
""" print("Final de la función") """

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 9 Dada la siguiente función,

def funcion(x,y):
  return (x-8)*(y**2)

funcion(16,1)

#¿Qué imprime el programa?
 
""" No imprime nada """

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 10 ¿Cómo hacemos para importar la variable pi del módulo math, pero con el nombre valor_pi?

""" (x) from math import pi as valor_pi """
