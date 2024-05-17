# Pregunta 1 Escriba una función de nombre promedio_std(). La función debe recibir una lista de 
# números llamada lista, y debe retornar retornar el promedio de ellos, junto con su desviación estándar.

# Hint 1: La desviación estándar corresponde a la raíz de la suma de los cuadrados de las diferencias de cada elemento respecto al promedio, divididos por la cantidad de elementos.
# Hint 2: Recuerda que puedes retonar dos valores x e y utilizando la notación

""" return (x,y) """

def raiz_cuadrada(num):
    return num ** 0.5

def promedio_std(lista):
    promedio = sum(lista) / len(lista)
    suma_cuadra_diff = sum((x - promedio) ** 2 for x in lista)
    desviacion_estandar = raiz_cuadrada(suma_cuadra_diff / len(lista))
    return (promedio, desviacion_estandar)

numeros=[1, 2, 3, 4, 5]
promedio, std_dev = promedio_std(numeros)
print("Promedio:", promedio)
print("Desviación estándar:", std_dev)

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Pregunta 2 Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: 
# azul, rojo, verde y amarillo. Desea saber cual de esos colores es el que más se repite. 
# Escriba una función color_frecuente que reciba como argumento a una lista de strings llamada 
# lista y retorne el string más repetido y el número de ocurrencias del mismo.

# Por ejemplo para la lista ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 
# 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']

# Debe retornar: "verde", 8

# En caso de que haya varios colores con el máximo número, se retornará con la siguiente prioridad: 
# azul, rojo, verde, amarillo. Es decir, por ejemplo si la lista es l = ['rojo', 'rojo', 'azul', azul'], 
#la función debe retornar "azul", 2

def color_frecuente(lista):
    contador = {'azul': 0, 'rojo': 0, 'verde': 0, 'amarillo': 0}

    for color in lista:
        contador[color] += 1

    max_ocurrencias = max(contador.values())
    colores_mas_frecuentes = [color for color, ocurrencias in contador.items() if ocurrencias == max_ocurrencias]

    prioridad_colores = ['azul', 'rojo', 'verde', 'amarillo']

    for color in prioridad_colores:
        if color in colores_mas_frecuentes:
            return color, max_ocurrencias

lista_colores = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
resultado = color_frecuente(lista_colores)
print(resultado)

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Pregunta 3 Un uso muy común de las listas es el de representar tableros con ellas. Para eso se utilizan 
# listas de listas, de este modo, se puede entender una lista de listas como una matriz. 
# Así, para acceder a un elemento i,j de la matriz, se debe acceder a: matriz[i][j]. 

# Para ese ejercicio se dispone de un tablero de buscaminas especial, donde lo único que hay es
# bombas en las distintas posiciones. Este tablero es de la forma:

#   ┌───────┬───────┬───────┬───────┐
#   │       │   X   │       │   X   │
#   ├───────┼───────┼───────┼───────┤
#   │   X   │       │       │       │
#   ├───────┼───────┼───────┼───────┤
#   │       │   X   │   X   │       │
#   ├───────┼───────┼───────┼───────┤
#   │   X   │       │       │   X   │
#   └───────┴───────┴───────┴───────┘

# Donde las X representan las bombas. Ese tablero, en representación matricial de Python, 
# donde se utilizan strings con un espacio: " " y "X" para representar espacios libres y bombas respectivamente, viene dado por:

# tablero = [[' ', 'X', ' ', 'X'],
#            ['X', ' ', ' ', ' '],
#            [' ', 'X', 'X', ' '],
#            ['X', ' ', ' ', 'X']]

# El objetivo de este ejercicio, es que programes una función buscaminas que reciba como 
# argumento a una matriz tablero y dos coordenadas i, j, y que entregue la cantidad de bombas que rodean a esa posición. 

# Por ejemplo, si la el tablero dado es el representado en la tabla, y la posición viene dada por 
# i=0 y j=0, tu función debe retornar el valor 2, ya que hay dos bombas rodeándola, en (0,1) y (1,0). 

# Por otro lado, si el tablero es el mismo, y las coordenadas son i=1, j=1, tu función debe retornar 4, 
# pues hay bombas rodeando la posición en (1,0), en (0,1), en (2,1) y en (2,2).

# Hint: recuerda que el tablero puede ser de un tamaño arbitrario y que al escribir posiciones 
# más grandes que ese tamaño o menores que 0, tu programa arrojará error.

def buscaminas(tablero, i, j):
    filas = len(tablero)
    columnas = len(tablero[0])
    bombas_alrededor = 0

    for fila in range(max(0, i-1), min(filas, i+2)):
        for columna in range(max(0, j-1), min(columnas, j+2)):
            if (fila, columna) != (i, j) and tablero[fila][columna] == 'X':
                bombas_alrededor += 1

    return bombas_alrededor

tablero = [[' ', 'X', ' ', 'X'],
           ['X', ' ', ' ', ' '],
           [' ', 'X', 'X', ' '],
           ['X', ' ', ' ', 'X']]
print(buscaminas(tablero, 0, 0))
print(buscaminas(tablero, 1, 1))