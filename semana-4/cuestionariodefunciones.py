# Pregunta 1 Para la tarea de determinar si un usuario es mayor de edad o no, se dispone de la función mayor(edad) 
# que recibe como argumento un número entero que representa la edad, y retorna True si la persona tiene 
# 18 años o más, y False en caso contrario.

# Determina cuál o cuáles de las siguientes alternativas presenta funciones que realicen lo anterior correctamente.

def mayor(edad):
    if edad >= 18:
        return True
    return False

edad = int(input("¿Qué edad tienes?: "))
print("Tú edad es ", edad, "y eres mayor de edad:", mayor(edad))
print()

def mayor(edad):
    return edad >= 18

edad = int(input("¿Qué edad tienes?: "))
print("Tú edad es ", edad, "y eres mayor de edad:", mayor(edad))
print()

def mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

edad = int(input("¿Qué edad tienes?: "))
print("Tú edad es ", edad, "y eres mayor de edad:", mayor(edad))

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 2 Dada la función factorial(n), que dado un número natural n, retorna el valor de n!, es decir, 1*2*3*4*...*n, se desea que en la variable resultado esté almacenado el valor de dicho cálculo. Determina cuál de las siguientes alternativas es correcta para calcular el factorial de 5 y que quede en dicha variable.

""" Respuesta
(x) n = 5
resultado = factorial(n) """

def factorial(n):
   if n==0:
      return 1
   else:
      return n * factorial(n - 1)
n = 5
resultado = factorial(n)
print("El factorial de", n, "es:", resultado)


print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 3 En cuanto al scope de funciones. Determina cuáles de los siguientes códigos termina en un error de Python.

def sumador(n):
   n += sumando
   return n

sumando = 10
sumador(5)
print(sumando)
print()

cantidad = 0
def sumador(n):
  cantidad += 1
  n += 1
  return n
sumador(5)
print()

def sumador(n, sumando):
  sumando += 1
  n += sumando
  return n
b = 9
sumador(5, b)

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 4 Determina lo que imprimirá el siguiente código:

numero = 10
def operacion(n):
  numero = 100
  return n * numero
operacion(5)
print(numero)

# Imprime
# >> 10

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 5 Si se tiene un módulo de funciones de nombre modulo.py, y este contiene las funciones multiplicar(a, b) y dividir(a, b). Determina cuáles de los siguientes códigos es correcto.

""" (x) from modulo import multiplicar, dividir
print(multiplicar(2, 3))
print(dividir(10, 5))

 (x) from modulo import *
print(multiplicar(2, 3))
print(dividir(10, 5))

 (x) import modulo
print(modulo.multiplicar(2, 3))
print(modulo.dividir(10, 5)) """

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 6 Determina el valor que queda almacenado en las variables resultado1 y resultado2 tras la ejecución del siguiente código:

def operacion(n):
  if n > 10:
    return 20
    return 15
  return 10
  return 25

resultado1 = operacion(8)
resultado2 = operacion(12)

# Imprime 
# resultado1 = 10
# resultado2 = 20

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 7 Considera el siguiente código:

def funcion(x):
  n = 3
  return ?
print(funcion(9))
print(funcion(10))

# ¿Qué debe retornar la función en lugar de ese "?" para que el código imprima True y False respectivamente?

# Imprime
""" (x) not bool(x % n) """

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 8 Considera el siguiente código:

numero = 5
resultado = exponenciacion_aleatoria(numero)

def exponenciacion_aleatoria(n):
  return n ** random.randint(1, 10)

#Selecciona todas las alternativas que muestren razones por las cuales el código anterior es incorrecto.
""" (x) Se llama a la función antes de que se hay definido
(x) No se importa el módulo random """


print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 9 Selecciona la afirmación incorrecta respecto a funciones.

""" (x) Una función no puede tener más de dos retornos. """

print()
print("----------------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------------------

# Pregunta 10 Considerando el siguiente programa:

def funcion(n):
  a = n ** 3
  b = a ** 2
  c = b + 100
  d = 5 * c
  return print(d)

d = funcion(2)

# Determina el valor que queda almacenado en d tras la ejecución del programa.

""" (x) None """
