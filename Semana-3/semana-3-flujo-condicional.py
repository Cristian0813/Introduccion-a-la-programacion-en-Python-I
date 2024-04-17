# 3.1.1 IF - ELSE


# TOMA DECISIONES
# ¿Como hacer que el programa decida?
#
#
# Operadores de comparación
# < <= > >= != ==
""" Menor --> """ 
5 < 5.1  #True

""" Mayor o igual --> """
3 >=5  #False

""" Distinto --> """
3!=5  #True

""" Igual --> """
6==9  #False

# ¿Qué valor entregará a <= b, si a=10 y b=7?
a = 10
b  = 7
a<=b  #False

# Operadores para tipos lógicos
# not and or
""" Negación --> """ 
not 3>5  #True

""" Conjunción --> """ 
3>5 and 2<6  #False

""" Disyunción --> """ 
3>5 or 2<6  #True

# Pregunta
""" llueve=False 
if llueve==True: 
    print("Llevaré paraguas")
else: print("No llevaré paraguas")
print("Ahora saldré a la calle") """

# Ejercicio
""" meses = int(input("Ingresa nº de meses "))
if meses <= 12:
  print("No te daré miel")
else:
  print("Toma esta cucharada de miel") """

# Ejercicio
""" llueve=True
temperatura=12
if llueve==True and temperatura <20: 
    print("Llevaré paraguas y abrigo") 
else: print("No necesito paraguas o abrigo") """



# 3.1.2. IF

# Flujo	condicional if
# Ejemplo if sin else
""" charco = True 
print("Comienza la caminata!") 
if charco==True: 
    print("A saltar!") 
print("Fin de la caminata") """

""" charco = False 
print("Comienza lacaminata!") 
if charco==True: 
  print("Asaltar!")
print("Findelacaminata") """

# Pregunta
""" x = float(input("Ingresa un dividendo: "))
y = float(input("Ingresa un divisor: "))
if y!=0:
  print("La división es",x/y)
print("Fin del programa") """

# Malo
""" charco = False 
else: 
 print("No saltaré") 
print("Sigo caminando")
#  else: 
#  ^^^^
#  SyntaxError: invalid syntax """

# Malo
""" charco = False 
if charco == True: 
    print("A saltar!") 
print("Sigo caminando")
else: 
    print("No saltaré")
#  else: 
#  ^^^^
#  SyntaxError: invalid syntax """


# 3.1.3. ELIF

# Lluvia Abrigo if/else
""" llueve = True
temperatura = int(input("Ingresa temp° "))
if temperatura < 18:
    if llueve == True:
        print("Llevaré paragua y abrigo")
    else:
        print("Solo llevaré abrigo")
else:
    print("No necesito paraguas ni abrigo") """

# Pregunta
# ¿Qué imprime el siguiente código, si el usuario ingresa el valor x=1001?

""" x = int(input("Ingrese x: "))
if x<10:
  if x>1000:
    print("1")
  else:
    print("2")
else:
  if x>1000:
    print("3")
  else:
    print("4") """

# Ejemplo elif
""" llueve=True
temperatura=int(input("Ingresa tempº "))
if temperatura<18 and llueve==True:
    print("Llevaré paraguas y abrigo")
elif temperatura<18 and llueve==False:
    print("Solo llevaré abrigo")
else: 
    print("No llevaré paraguas ni abrigo") """

# Ejemplo simplificado elif
""" llueve=True 
temperatura=int(input("Ingresa tempº ")) 
if temperatura>=18: 
    print("No llevaré paraguas ni abrigo")
elif llueve==True: 
    print("Llevaré paraguas y abrigo")
else: 
    print("Solo llevaré abrigo") """


# Cuestionario

# Pregunta 1: ¿De las siguientes opciones, cuál es una manera inválida de implementar una condición en un programa Python?
""" (x) else sin if """


# Pregunta 2: En una competencia de cantantes, si las tres personas del jurado le dan una "X" al participante, éste queda eliminado. De las siguientes, ¿cuál sería una manera de escribir esa condición?
""" # (x) 
if jurado1 == "X" and jurado2 == "X" and jurado3 == "X": """

# Pregunta 3: En algunos países, la mayoría de edad se cumple a los 18 años. ¿Cúal es el código correcto para escribir un programa que determine si un usuario es mayor de edad o no?
""" # (x) 
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad") 
# Eres mayor de edad """

# Pregunta 4: ¿Qué imprime el siguiente código?
""" # (x) 
a = 15
b = 10
if a == b:
  print("Son iguales")
  print("Adiós")
else:
  print("Son distintos")
  print("Adiós")
print("a y b son dos números")
# Son distintos
# Adios
# a y b son dos números """

# Pregunta 5: ¿Cuál es el error que presenta el siguiente código?
""" 
c = float(input("Ingrese temperatura del agua"))
if c <= 0:
  print("Su agua está congelada")
elif c >= 0 and c < 100:
  print("Su agua está líquida") 
elif:
  print("Su agua está hirviendo") 
# (x) Existe un elif sin condición. """

# Pregunta 6: ¿Qué imprime el siguiente código?
""" n = 20
if (n <= 100 and n % 2 == 0) or (n < 5):
  if n != 21:
    print("1")
  else:
    print("2")
else:
  if n == 20:
    print("3")
  else:
    print("4")
# (x) 1 """

# Pregunta 7: Para definir la calidad del aire se hace una medición de partículas presentes en este. Dependiendo de su valor se definen 5 posibles estados de calidad de aire:
#
# Bueno: 0-99
# Regular: 100-199
# Alerta: 200-299
# Premergencia: 300-499
# Emergencia: 500-Superior
#
# Esto quiere decir si la medición es de menos de 99, la calidad es buena, si la medición es de menos de 199, pero más de 100 es regular, etc.
#
# (Fuente: http://portal.mma.gob.cl pronostico-rm/)
#
# Hemos escrito el siguiente código que recibe esta medición e imprime la calidad del aire:
""" numero = int(input("Ingrese calidad del aire"))
if numero >= 0 and numero <= 99:
  print("Bueno")
elif numero >= 100 and numero <= 199:
  print("Regular")
elif numero >= 200 and numero <= 299:
  print("Alerta")
elif numero >= 300 and numero <= 499:
  print("Preemergencia")
else:
  print("Emergencia")
# (x) Emergencia """

# Pregunta 8: Para definir la calidad del aire se hace una medición de partículas presentes en este. Dependiendo de su valor se definen 5 posibles estados de calidad de aire:
#
# Bueno: 0-99
# Regular: 100-199
# Alerta: 200-299
# Premergencia: 300-499
# Emergencia: 500-Superior
#
# Esto quiere decir si la medición es de menos de 99, la calidad es buena, si la medición es de menos de 199, pero más de 100 es regular, etc.
#
# (Fuente: http://portal.mma.gob.cl pronostico-rm/)
#
# Hemos escrito el siguiente código que recibe esta medición e imprime la calidad del aire:
""" numero = int(input("Ingrese calidad del aire"))
if numero>=0 and numero<=99:
  print("Bueno")
if numero>=100 and numero<=199:
  print("Regular")
if numero>=200 and numero<=299:
  print("Alerta")
if numero>=300 and numero<=499:
  print("Preemergencia")
else:
  print("Emergencia")
# (x) Regular, Emergencia """

# Pregunta 9: Queremos escribir un programa que imprima "par" si un número es par, y nada en otro caso. ¿Cuál es el código correcto para esto?
""" # (x)
numero = int(input("Ingrese numero"))
if numero%2==0:
  print("Es par")
# Es par """

# Pregunta 10: Se conoce como año bisiesto a un año que tiene un día extra. Todo año bisiesto debe cumplir alguna de las siguientes condiciones:
#
# 1. Debe ser divisible por 4, pero no por 100.
# 2. Debe ser divisible por 100, pero no por 400.
#
# Por ejemplo, 1996 es año bisiesto porque cumple la condición uno. Por otro lado 1900 no lo es, ya que no cumple ninguna de las condiciones. 
#
# ¿Cuál de las siguientes condiciones es la que permite determinar si un año A es bisiesto?
""" # (x)
A = 1996
if (A % 4 == 0 and A % 100 != 0) or (A % 100 == 0 and A % 400 == 0):
  print("Es bisiesto")
# Es bisiesto """

def sueldo(cargo):

  if cargo == "Ejecutivo":
    dinero = 90
  elif cargo == "Jefe":
    dinero = 100
  elif cargo == "Externo":
    dinero = 50
  else:
    dinero = 0

  return dinero

# Ejemplo de uso
cargo = "Externo"
sueldo_asignado = sueldo(cargo)
print(f"El sueldo para el cargo {cargo} es de {sueldo_asignado}")