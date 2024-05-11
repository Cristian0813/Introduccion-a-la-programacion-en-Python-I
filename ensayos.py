# tupla = (1, 2, 3, 5, 6, 7, 8, 9)
# lista_modificada = list(tupla)
# lista_modificada.insert(4, 4)
# tupla_nueva = tuple(lista_modificada)

# print(tupla_nueva)  # Salida: (1, 2, 3, 4, 5, 6, 7, 8, 9)

# m1 = ('Toy Story', 1995, '01:21', ['animacion', 'comedia'])
# m1[3].append( 'infantil' )
# print(m1)

# tupla = (2.0, 4.7, 6.8, 5.1)
# lista = []
# for nota in tupla:
#     lista.append(nota)
# lista[0] = 3.2
# print("Lista de notas: ", lista)

# from collections import deque
# deq = deque( (1,4,5,3,2) )
# print( deq.popleft() )
# print( deq.pop() )
# print( deq.pop() )
# print( deq.popleft() )
# print( deq.count(5) * 5 )

# # pregunta 9

# from collections import deque

# # Creamos las colas de pasajeros
# pasajeros_prioritarios = deque(['Niño 1', 'Anciano 1', 'Mujer embarazada 1'])
# pasajeros = deque(['Pasajero 1', 'Pasajero 2', 'Pasajero 3'])
# tripulacion = deque(['Tripulante 1', 'Tripulante 2', 'Tripulante 3'])

# # Vaciamos las colas en orden
# while len(pasajeros_prioritarios) > 0:
#     print(f"Evacuando pasajero prioritario: {pasajeros_prioritarios.pop()}")

# while len(pasajeros) > 0:
#     print(f"Evacuando pasajero: {pasajeros.pop()}")

# while len(tripulacion) > 0:
#     print(f"Evacuando tripulante: {tripulacion.pop()}")


# #pregunta 10

# from collections import deque

# def llenar_cola(cola, elementos):
#     """
#     Llena la cola especificada con los elementos proporcionados.

#     Args:
#         cola (deque): La cola que se desea llenar.
#         elementos (list): La lista de elementos que se agregarán a la cola.

#     Ejemplo de uso:
#         cola = deque()
#         elementos = ['Elemento 1', 'Elemento 2', 'Elemento 3']
#         llenar_cola(cola, elementos)
#         print(cola)  # Salida: deque(['Elemento 1', 'Elemento 2', 'Elemento 3'])
#     """
#     for elemento in elementos:
#         cola.append(elemento)


# def invertir_cola(cola):
#     """
#     Invierte el orden de los elementos en la cola especificada.

#     Args:
#         cola (deque): La cola cuyo orden se desea invertir.

#     Ejemplo de uso:
#         cola = deque(['Elemento 3', 'Elemento 2', 'Elemento 1'])
#         invertir_cola(cola)
#         print(cola)  # Salida: deque(['Elemento 1', 'Elemento 2', 'Elemento 3'])
#     """
#     aux = deque()  # Cola auxiliar para invertir el orden

#     while len(cola) > 0:
#         aux.append(cola.pop())  # Pasamos los elementos de la cola original a la cola auxiliar, en orden inverso

#     cola = aux  # La cola original se convierte en la cola auxiliar invertida


# # Ejemplo de uso
# cola = deque()
# llenar_cola(cola, ['Elemento 3', 'Elemento 2', 'Elemento 1'])  # Llenamos la cola
# print(f"Cola original: {cola}")  # Mostramos la cola original

# invertir_cola(cola)  # Invertimos el orden de la cola
# print(f"Cola invertida: {cola}")  # Mostramos la cola invertida


# tupla = (1,2,3,5,6,7,8,9)
# tupla.insert(4, 4)
# print(tupla)


# def vuelos_disponibles(vuelos, origen, destino, pasajeros):
#     vuelos_disponibles = [vuelos[0]]  # Inicializamos la lista de vuelos disponibles con el header

#     for vuelo in vuelos[1:]:
#         if vuelo[0] == origen and vuelo[1] == destino and vuelo[3] >= pasajeros:
#             vuelos_disponibles.append(vuelo)

#     return vuelos_disponibles

# def mostrar_vuelos(vuelos):
#     for vuelo in vuelos:
#         print(', '.join(map(str, vuelo)))

# vuelos = [
#     ['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha'],
#     ['Santiago', 'Puerto Montt', 35000, 30, '11 Enero 2023'],
#     ['Santiago', 'Concepción', 30000, 40, '20 Febrero 2023'],
#     ['Santiago', 'Puerto Montt', 28000, 2, '19 Enero 2023'],
#     ['Santiago', 'Puerto Montt', 12000, 100, '20 Mayo 2023'],
#     ['Antofagasta', 'Santiago', 27000, 14, '18 Abril 2023']
# ]

# origen = 'Santiago'
# destino = 'Puerto Montt'
# pasajeros = 5

# vuelos_disponibles_result = vuelos_disponibles(vuelos, origen, destino, pasajeros)
# mostrar_vuelos(vuelos_disponibles_result)

# opciones = {'Si', 'No'}
# print(opciones)
# opciones.add('No se')
# opciones.add('No')
# print(opciones)

# cuando = {'Mañana', 'Pasado', 'Hoy'}


# poema = ['Mis', 'pasos', 'en', 'esta', 'calle', 'Resuenan', 'En', 'otra', 'calle', 'Donde', 'Oigo', 'mis', 'pasos', 'Pasar', 'en', 'esta', 'calle', 'Donde', 'Sólo', 'es', 'real', 'la', 'niebla']
# prohibidas = set( ['calle', 'mis', 'pasos'] )

# """ for palabra in prohibidas:
#     if palabra in poema:
#         poema.remove(palabra) """

# for palabra in prohibidas:
#     while palabra in poema:
#         poema.remove(palabra)

# print(poema)
# print()
# print()

# lista = [1,2,1,1,5,6,4,4,4,6,7,5,1,1,7,7,7,2,1,2]

# # a. 
# datos = set(lista)
# print(len(datos))

# # b.
# for num in lista:
#     veces = lista.count(num)
#     for i in range(veces):
#         lista.remove(num)
# print(len(lista))

# # c.
# no_repetidos = dict()
# for num in lista:
#     no_repetidos[num] = num
# print(len(no_repetidos))

# # d.
# no_repetidos = []
# for num in lista:
#     if num not in no_repetidos:
#         no_repetidos.append(num)
# print(len(no_repetidos))
# print()
# print()

# lista = [1,2,1,1,5,6,4,4,4,6,7,5,1,1,7,7,7,2,1,2]
# # resultado {1: 6, 2: 3, 5: 2, 6: 2, 4: 3, 7: 4}

# d = dict()
# for num in set(lista):
#     d[num] = lista.count(num)
# print(d)
# print()
# print()

# clientes = {
#     'Alicia': (28, 'Chile', 1200),
#     'Bob': (45, 'Francia', 2000),
#     'Carlos': (30, 'Argentina', 500),
#     'David': (23, 'Inglaterra', 0)
# }

# for cliente in clientes:
#     edad, residencia, deuda = clientes[cliente]
#     if deuda > 1000:
#         print(cliente)
# print()
# print()

# amigos = {'Bob': ['Patricio', 'Calamardo', 'Arenita', 'Don Cangrejo'],
#     'Patricio': ['Bob', 'Calamardo'],
#     'Arenita': ['Bob'],
#     'Calamardo': [],
#     'Don Cangrejo': ['Bob', 'Calamardo']
# }
# Resultado
# {'Bob': 3,
# 'Patricio': 1,
# 'Arenita': 1,
# 'Calamardo': 3,
# 'Don Cangrejo': 1
# }

# otro = dict()
# for nombre, lista_amigos in amigos.items():
#     otro[nombre] = 0
#     for amigo in lista_amigos:
#         otro[amigo] += 1
# print(otro)
# print()
# print()
# print()


#--------------------------------------------------------------------------


# Pregunta 1
# Cada vez que vas al supermercado pides que te manden la boleta al correo.
# Luego de ir un par de veces decides descargar todas tus boletas. 
# La información de cada boleta viene en un diccionario con el siguiente formato:

# {'fecha_compra' : '30-05-22',
# 'precio' : 12000,
# 'productos' : {
#     'Leche' : 2,
#     'Chocolate': 1,
#     'Arroz': 5
#     }
# }

# Es decir, la boleta es un diccionario con las keys: fecha_compra, precio y productos.
# fecha_compra, es un string con la fecha de la compra 
# precio es un entero con el precio final de la compra
# productos es un diccionario, donde la key tiene el nombre de un producto comprado y 
# el value es un int con la cantidad comprada de ese producto.
# Como ejemplo, la compra anterior fue realizada el 30-05-22, el precio total de esta compra fue de 12000 y 
# se compraron 2 unidades de leche, 1 de chocolate y 5 de arroz.
# Al descargar las boletas, el programa te retorna una lista con varios diccionarios en el formato anterior, 
# por ejemplo, si has realizado tres compras, entonces el programa te podría retornar:

# boletas = [{'fecha_compra' : '29-05-22',
# 'precio' : 12000,
# 'productos' : {'Chocolate': 1,
# 'Mantequilla': 1,
# 'Huevos': 12,
# 'Pan' : 1}
# },
# {'fecha_compra' : '31-05-22',
# 'precio' : 2400,
# 'productos' : {'Pan': 1, 'Leche' : 2}

# Una vez descargada esta información decides crear un programa que te de un resumen de tus compras. 
# Parte 1
# Para esta parte deberás definir la función precio_total(boletas), la cual recibe como parámetro una 
# lista de boletas en el formato anterior. La función deberá retornar el precio total de todas tus compras.


# def precio_total(boletas):
#   """
#   Calcula el precio total de todas las compras.

#   Args:
#       boletas: Lista de diccionarios con información de las compras.

#   Returns:
#       int: Precio total de todas las compras.
#   """
#   precio_total = 0
#   for boleta in boletas:
#     precio_total += boleta["precio"]
#   return precio_total

# # Ejemplo de uso
# boletas_ejemplo = [
#     {'fecha_compra': '29-05-22', 'precio': 12000, 'productos': {'Chocolate': 1, 'Mantequilla': 1, 'Huevos': 12, 'Pan': 1}},
#     {'fecha_compra': '31-05-22', 'precio': 2400, 'productos': {'Pan': 1, 'Leche': 2}},
#     {'fecha_compra': '01-06-22', 'precio': 3000, 'productos': {'Mantequilla': 2, 'Azucar': 1}}
# ]

# precio_total_ejemplo = precio_total(boletas_ejemplo)
# print(f"Precio total de compras: {precio_total_ejemplo}")



# Pregunta 3
# Cada vez que vas al supermercado pides que te manden la boleta al correo. Luego de ir un par de veces decides descargar todas tus boletas. La información de cada boleta viene en un diccionario con el siguiente formato:
# {'fecha_compra' : '30-05-22',
# 'precio' : 12000,
# 'productos' : {
#     'Leche' : 2,
#     'Chocolate': 1,
#     'Arroz': 5
#     }
# }
# Es decir, la boleta es un diccionario con las keys: fecha_compra, precio y productos.

# fecha_compra, es un string con la fecha de la compra 
# precio es un entero con el precio final de la compra
# productos es un diccionario, donde la key tiene el nombre de un producto comprado y el value es un int con la cantidad comprada de ese producto.

# Como ejemplo, la compra anterior fue realizada el 30-05-22, el precio total de esta compra fue de 12000 y se compraron 2 unidades de leche, 1 de chocolate y 5 de arroz.

# Al descargar las boletas, el programa te retorna una lista con varios diccionarios en el formato anterior, por ejemplo, si has realizado tres compras, entonces el programa te podría retornar:
# boletas = [{'fecha_compra' : '29-05-22',
# 'precio' : 12000,
# 'productos' : {'Chocolate': 1,
# 'Mantequilla': 1,
# 'Huevos': 12,
# 'Pan' : 1}
# },
# {'fecha_compra' : '31-05-22',
# 'precio' : 2400,
# 'productos' : {'Pan': 1, 'Leche' : 2}
# },
# {'fecha_compra' : '01-06-22',
# 'precio' : 3000,
# 'productos' : {'Mantequilla': 2, 'Azucar' : 1}
# }
# ]
# Una vez descargada esta información decides crear un programa que te de un resumen de tus compras. 
# Parte 3
# Para esta parte deberás definir la función productos_frecuentes(boletas), la cuál recibe como parámetro una lista de boletas en el formato anterior. La función deberá retornar un set con aquellos productos que estén en al menos el 50% de las boletas, es decir, aquellos productos que se compraron en la mitad de todas las compras o más. Para el ejemplo anterior, este set deberá contener:
# {'Pan', 'Mantequilla'}

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

# Pregunta 1
# Dada la definición de Carta vista en clases. Si quieres crear una nueva clase Carta que tenga como atributos la pinta, 
# el número y la baraja a la que pertenece (“Azul” o “Roja”). ¿Cuál sería la definición correcta de la clase con su 
# constructor?


class Carta:
    def __init__(self, p, num, bar):
        self.pinta = p
        self.num = num
        self.bar = bar

carta1 = Carta("Azul", 10, "Roja")
carta2 = Carta("Verde", 7, "Verde")

print("Respuesta de la pregunta 1")
print(carta1.pinta)  # Salida: Azul
print(carta1.num)  # Salida: 10
print(carta1.bar)  # Salida: Roja

print(carta2.pinta)  # Salida: Verde
print(carta2.num)  # Salida: 7
print(carta2.bar)  # Salida: Verde
print()
print("-----------------------------------------------------------------------------------------")
print()

#--------------------------------------------------------------------------

# Pregunta 2.
# Quieres definir la clase Adulto, la cual recibe como parámetro un nombre y una edad y 
# guarda esa información en los atributos nombre y edad respectivamente. 
# ¿Cuál de los siguientes códigos la define correctamente?


class Adulto:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

adulto1 = Adulto("Juan", 35)
adulto2 = Adulto("Maria", 28)

print("Respuesta de la pregunta 2")
print(adulto1.nombre)  # Output: Juan
print(adulto1.edad)  # Output: 35

print(adulto2.nombre)  # Output: Maria
print(adulto2.edad)  # Output: 28
print()
print("-----------------------------------------------------------------------------------------")
print()

#--------------------------------------------------------------------------

# Pregunta 3
# Dada la definición de Estudiante vista en clases:
# class Estudiante:
#     def __init__(self,n,p,f):
#         self.nombre = n
#         self.parcial = p
#         self.final = f
# 
# El profesor decide sumarle 5 a la nota final de todos los alumnos. 
# ¿Cuál de los siguientes códigos modifica el inicializador anterior para que la nota final que guarde
# el alumno sea 5 más que la nota que recibe como parámetro f?

class Estudiante:
    def __init__(self, n, p, f):
        self.nombre = n
        self.parcial = p
        self.final = f + 5

estudiante1 = Estudiante("Ana", 5, 64)
estudiante2 = Estudiante("Cristian", 10, 70)
estudiante3 = Estudiante("Pedro", 90, 85)

print("Respuesta de la pregunta 3")
print(estudiante1.nombre)  # Output: Ana
print(estudiante1.parcial)  # Output: 5
print(estudiante1.final)  # Output: 69

print(estudiante2.nombre)  # Output: Cristian
print(estudiante2.parcial)  # Output: 10
print(estudiante2.final)  # Output: 75

print(estudiante3.nombre)  # Output: Pedro
print(estudiante3.parcial)  # Output: 90
print(estudiante3.final)  # Output: 90
print()
print("-----------------------------------------------------------------------------------------")
print()

#--------------------------------------------------------------------------

# Pregunta 4
# Dada la definición de Estudiante vista en clases:
# class Estudiante:
#     def __init__(self,n,p,f):
#         self.nombre = n
#         self.parcial = p
#         self.final = f
# El profesor decide no almacenar el nombre de cada alumno, sino que en su lugar decide guardar 
# en el atributo nombre solamente la primera letra del nombre recibido. 
# Considerando que el constructor recibe el nombre completo del alumno, su nota parcial y su nota final. 
# ¿Cuál de los siguientes código hace lo pedido por el profesor?

class Estudiante:
    def __init__(self,n,p,f):
        self.nombre = n[0]
        self.parcial = p
        self.final = f

estudiante1 = Estudiante("Ana", 5, 64)
estudiante2 = Estudiante("Cristian", 10, 70)
estudiante3 = Estudiante("Pedro", 90, 85)

print("Respuesta de la pregunta 4")
print(estudiante1.nombre)  # Output: Ana
print(estudiante1.parcial)  # Output: 5
print(estudiante1.final)  # Output: 69

print(estudiante2.nombre)  # Output: Cristian
print(estudiante2.parcial)  # Output: 10
print(estudiante2.final)  # Output: 75

print(estudiante3.nombre)  # Output: Pedro
print(estudiante3.parcial)  # Output: 90
print(estudiante3.final)  # Output: 90
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

# Pregunta 5
# Dada la definición de Carta vista en clases: 
# class Carta:
#     def __init__(self, p, num)
#         self.pinta = p
#         self.num = n
# Se quiere cambiar el constructor para recibir primero el parámetro de número y 
# después el parámetro de pinta. ¿Cuál de los siguientes constructores NO cumple este requisitos?

class Carta:
    def __init__(self, num, p):
        self.pinta = num
        self.num = p

carta1 = Carta(10, "Azul")
carta2 = Carta("Azul", 10)  # This would cause an error

print("Respuesta de la pregunta 5")
print(carta1.num)   # Output: 10
print(carta1.pinta)  # Output: Azul
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

# Pregunta 6
# Quieres definir una clase Empleado, la cuál recibe como parámetro de su constructor un nombre y un número de teléfono.
# El número de teléfono puede venir en uno de los siguientes formatos:
# - Un entero de 8 dígitos
# - Un entero de 9 dígitos que comienza con 9
# - Un string de 9 dígitos que comienza con 9
# - Un string que comienza con +569 seguido de 8 dígitos
# El constructor de la clase Empleado deberá recibir un nombre y un número en uno de los 
# formatos anteriores. La clase deberá guardar el nombre, además del número con el formato +569 seguido de 8 dígitos.
# ¿Cuál de los siguientes códigos define correctamente el constructor de la clase Empleado?

# NO SON ESTÁS
# class Empleado:
#     def __init__(self, nombre, numero):
#         self.nombre = nombre

#         if type(numero) == str:
#             if numero[0] == '+':
#                 self.numero = numero
#             else:
#                 self.numero = '+56' + numero
#         else:
#             if len( str(numero) ) == 8:
#                 self.numero = '+569' + numero
#             else:
#                 self.numero = '+56' + numero
#
# class Empleado:
#     def __init__(self, nombre, numero):
#         self.nombre = nombre

#         if numero[0] == '+':
#             self.numero = numero
#         elif len(numero) == 9:
#             self.numero = '+56' + numero
#         elif len(numero) == 8:
#             self.numero = '+569' + numero

# class Empleado:
#     def __init__(self, nombre, numero):
#         self.nombre = nombre

#         self.numero = str(numero)
#         if len(numero) == 8:
#             self.numero = '+569' + numero
#         elif len(numero) == 9:
#             self.numero = '+56' + numero
#         else:
#             self.numero = numero

class Empleado:
    def __init__(self, nombre, numero):
        self.nombre = nombre

        numero = str(numero)
        faltan = 12 - len(numero)
        self.numero = '+569'[:faltan] + numero

empleado1 = Empleado("Juan", "12345678")
empleado2 = Empleado("Maria", "+56987654321")
empleado3 = Empleado("Pedro", "987654321")

print("Respuesta de la pregunta 6")
print("Nombre:", empleado1.nombre)
print("Número de teléfono:", empleado1.numero)
print("Nombre:", empleado2.nombre)
print("Número de teléfono:", empleado2.numero)
print("Nombre:", empleado3.nombre)
print("Número de teléfono:", empleado3.numero)

print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

# Pregunta 7
# Dada la definición de Estudiante vista en clases: 
#   class Estudiante: 
#       def __init__(self,n,p,f): 
#           self.nombre = n 
#           self.parcial = p 
#           self.final = f 
# ¿Cuál es los siguientes códigos le agrega correctamente a la clase el método recorreccion_parcial(self, nota_nueva), 
# el cual recibe como parámetro la nota recorregida de la evaluación parcial del alumno? 
# El método debe reemplazar la nota del parcial que tenía el alumno por la nota nota_nueva. 

class Estudiante:
    def __init__(self, n, p, f):
        self.nombre = n
        self.parcial = p
        self.final = f

    def recorreccion_parcial(self, nota_nueva):
        self.parcial = nota_nueva 

    def __str__(self):
        return f"Nombre: {self.nombre}\nParcial: {self.parcial}\nFinal: {self.final}"

estudiante1 = Estudiante("Juan Pérez", 7.5, 8.0)
estudiante2 = Estudiante("Ana Gómez", 6.0, 9.5)
estudiante1.recorreccion_parcial(8.5)

print("Respuesta de la pregunta 7")
print(estudiante1)
print(estudiante2)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

# Pregunta 8
# Tienes la siguiente clase: 
#   class Estudiante: 
#       def __init__(self, n):
#           self.nombre = n 
#       self.notas = [] 
# ¿Cuál de los siguientes códigos le agrega correctamente a la clase anterior el método agregar_nota(self, nota)? 
# Este método deberá recibir como parámetro un entero nota. El método deberá agregar la nota recibida a la 
# lista de notas del alumno. 

class Estudiante:
    def __init__(self, n):
        self.nombre = n
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota) 
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nNota: {self.notas}"

estudiante1 = Estudiante("David Sánchez")
estudiante1.agregar_nota(4.5)
print("Respuesta de la pregunta 8")
print(estudiante1)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

# Pregunta 9
# Tienes la clase: 
#   class Estudiante:
#       def __init__(self, nombre, notas)
#           self.nombre = nombre
#           self.notas = notas
# Sabemos que nombre es un string y notas es una lista de floats, por ejemplo, 
# notas puede ser [6.2, 5.5,4.8]. Al imprimir esta clase quieres que se imprima lo siguiente:
# Nota mínima X - Nota máxima Y
# Por ejemplo, si tienes una Estudiante Alicia con las notas [6.2, 5.5, 4.8]. 
# Entonces deberá imprimir: Nota mínima 4.8 - Nota máxima 6.2
# ¿Cuál de los siguientes códigos hace lo pedido?

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def __str__(self):
        menor = min(self.notas)
        mayor = max(self.notas)
        return 'Nota mínima '+str(menor)+' - Nota máxima ' + str(mayor)


# Ejemplo de uso
estudiante1 = Estudiante("Alicia", [6.2, 5.5, 4.8])
estudiante2 = Estudiante("Juan", [7.5, 8.0, 9.0])

print("Respuesta de la pregunta 9")
print(estudiante1)
print(estudiante2)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

# Pregunta 10
# Tienes la siguiente clase ya definida: 
#   class Gato:
#       def __init__(self):
#           self.tablero = [[' ']*3,
#                           [' '] * 3,
#                           [' '] * 3]
# Esta clase representa un juego de Gato, donde inicialmente hay un tablero vacío. 
# Esta clase necesita el método jugada(self, fila, columna, figura), el cual recibe como parámetros dos enteros 
# (fila y columna) y un string figura. El método deberá asegurarse de lo siguiente:
#   (a) fila y columna deben ser enteros entre 0 y 2 inclusive.
#   (b) figura tiene que ser un string de un solo carácter
#   (c) la posición indicada del tablero debe estar vacía (ser un string inicial del tablero)
# Si no se cumple alguna de estas condiciones, la función deberá retornar False. En caso de que se cumplan todas las condiciones se deberá actualizar el tablero con la jugada y retornar True. 
# ¿Cuál de los siguientes códigos define el método correctamente?

# NO SON ESTÁS
# class Gato:
#     def __init__(self):
#         self.tablero = [[' ']*3,
#                         [' '] * 3,
#                         [' '] * 3]
#
#     def jugada(self, fila, columna, figura):
#         if fila < 0 and 2 < fila:
#             return False
#         if columna < 0 and 2 < columna:
#             return False
#         if len(figura) != 1:
#             return False
#         if self.tablero[fila][columna] != ' ':
#             return False
#         self.tablero[fila][columna] = figura
#         return True
#
# class Gato:
#     def __init__(self):
#         self.tablero = [[' ']*3,
#                         [' '] * 3,
#                         [' '] * 3]
#
#     def jugada(self, fila, columna, figura):
#         if fila < 0 or 2 < fila:
#             return False
#         if columna < 0 or 2 < columna:
#             return False
#         if len(figura) != 1:
#             return False
#         if self.tablero[fila][columna] != ' ':
#             return False
#         else:
#             self.tablero[fila][columna] = figura
#             return True
#
# class Gato:
#     def __init__(self):
#         self.tablero = [[' ']*3,
#                         [' '] * 3,
#                         [' '] * 3]

#     def jugada(self, fila, columna, figura):
#         if (fila or columna) < 0 or (fila or columna) < 2:
#             return False
#         elif len(figura) != 1 or self.tablero[fila][columna] != ' ':
#             return False
#         else:
#             self.tablero[fila][columna] = figura
#             return True

class Gato:
    def __init__(self):
        self.tablero = [[' ']*3,
                        [' '] * 3,
                        [' '] * 3]

    def jugada(self, fila, columna, figura):
        if fila < 0 or fila > 2:
            return False
        if columna < 0 or columna > 2:
            return False
        if len(figura) != 1:
            return False
        if self.tablero[fila][columna] != ' ':
            return False
        self.tablero[fila][columna] = figura
        return True
    
juego_gato = Gato()

jugada_valida = juego_gato.jugada(1, 1, 'X')
print("¿La jugada es válida?", jugada_valida)
jugada_invalida = juego_gato.jugada(0, 0, 'O')
print("¿La jugada es válida?", jugada_invalida)
print()
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

class Planta:
    def __init__(self, especie, altura):
        self.especie = especie
        self.altura = altura

a = Planta('Washingtonia filifera', 15)
print(a.especie)
print(a.altura)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

class Menu:
    def __init__(self, comidas: list, precios: list) -> None: 
        assert len(comidas) == len(precios), "comidas debe tener la misma longitud que precios para crear el Menú"
        self.comidas = comidas 
        self.precios = precios 

    def __str__(self) -> str:
        tex = []
        for (comida, precio) in zip(self.comidas, self.precios):
            tex.append(comida + ": " + str(precio))
        return "\n".join(tex)

comidas = ['Pato a la mostaza', 'Hamburguesa', 'Ensalada', 'Lasagna'] 
precios = [20000, 8000, 6000, 9000] 
menu = Menu(comidas, precios)
print(menu)
print()
print("-----------------------------------------------------------------------------------------")
print()

#-----------------------------------------------------------------------------------------

class Enemigo:
    def __init__(self, nombre, vida, fuerza_ataque):
        self.nombre = nombre
        self.vida = vida
        self.fuerza_ataque = fuerza_ataque

    def recibir_ataque(self, daño):
        self.vida = max(0, self.vida - daño)

    def atacar(self, otro):
        otro.recibir_ataque(self.fuerza_ataque)

    def __str__(self):
        return f"{self.nombre} - {self.vida}"

# Ejemplo de uso
a = Enemigo('Ladrón', 14, 3)
b = Enemigo('Kraken', 12, 6)

print(a)
print(b)

b.recibir_ataque(5)
a.atacar(b)
print(a)
print(b)

b.recibir_ataque(7)
b.atacar(a)
print(a)
print(b)

a.recibir_ataque(5)
b.atacar(a)
print(a)
print(b)

