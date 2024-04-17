# Pregunta video
# ¿Cuándo se termina un ciclo while?
# (x) Cuando se evalúa la condición del ciclo, y ésta es Falsa (False).
# Cuando se evalúa la condición del ciclo, y ésta es Verdadera (True).
# Después de un número predeterminado de ejecuciones del ciclo.
# En cualquier momento de ejecución de las instrucciones en que la condición sea Falsa (False), inmediatamente se termina el ciclo.

# Pregunta video
# nota = 5
# suma = 0
# suma = suma+nota
# suma = suma+nota
# ¿Cuánto vale suma al final del código?
# 0
# 5
# (x) 10
# 15
# Correcto. Suma va acumulando los valores de nota. Dado que se le suma dos veces el valor de nota, finalmente suma vale 10.

# Pregunta video
# La instrucción range(123) genera los números desde 0 hasta ... (ingresa el último número que se genera)
# 122
# Correcto. range(x) genera los números desde 0 hasta x-1, por lo tanto en este caso, desde 0 hasta 122.

# Pregunta video
# range(100,110,2) genera la secuencia...
# 100, 102, 104, 106, 108, 110
# 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110
# (x) 100, 102, 104, 106, 108
# 100, 101, 102, 103, 104, 105, 106, 107, 108, 109
# Correcto. range(100,110,2) genera la secuencia desde 100 hasta 109, saltando de 2 en 2, por lo que generará 100, 102, 104, 106 y 108 (pero no 110, dado que es mayor que 109)

for i in range(10):
    print('hola mundo')