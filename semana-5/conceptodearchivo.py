# CONCEPTO DE ARCHIVO

# Archivos

# ¿Qué es un archivo?  Introducción 

# ● Toda información en un computador se guarda en alguna parte 
# ● Esta se organiza en directorios (o carpetas), y dentro de ellos archivos 
# ● A veces queremos guardar información aun cuando se haya terminado de ejecutar un programa 
# ● O queremos leer información que tengamos en nuestro computador 
# ● Para estas labores se ocupan los archivos 
# ● Existen muchos pos: estos se ven en la terminación (.doc, .ppt, .txt) 
# ● Aquí solo ocuparemos archivos .txt 

#----------------------------------------------------------------------------------------------------

# ¿Por qué ocuparlos con Python? 
# Posibles acciones 
# ● Es necesario aprender de archivos cuando se está programando, porque así se comunican datos o resultados 
# ● Los archivos se pueden leer, escribir, copiar, etc. 
# ● Por ejemplo, un programa puede leer notas obtenidas por alumnos, calcular la nota final y si aprobó el curso 
# ● Aquí habrá un archivo con los datos de entrada, y otro donde se escriben los resultados 

#----------------------------------------------------------------------------------------------------

# Abrir y leer archivos 

# Abrir archivos Observaciones 

# ● Lo primero será abrir el archivo. 
# ● Se necesita el nombre del archivo 
# ● Que esté guardado en la misma parte que el programa (en la misma carpeta) 

#----------------------------------------------------------------------------------------------------

# Abrir archivos open("archivo.txt") 

# ● Para abrirlo se ocupará la función open 
# ● Se le debe dar como parámetro el nombre del archivo (incluyendo la terminación después del punto) 
a = open("archivo.txt")
# ● Si no se encuentra el archivo, se genera un error

#----------------------------------------------------------------------------------------------------

# Abrir archivos open("archivo", "modo") 

# ● La función open toma un segundo parámetro: el modo 
# ● Indica si se quiere leer o escribir el archivo  
# "r": solo lectura (read) 
# "w": escritura (write) 
lectura = open("archivo.txt", "r") 
escritura = open("archivo.txt", "w") 
# ● ¿Qué se muestra si imprimimos el contenido de la variable lectura? 
""" <_io.TextIOWrapper name='arch.txt'... """ 

#----------------------------------------------------------------------------------------------------

# Leer archivos lectura.read() 

# ● Para leer el archivo, se debe llamar al método read sobre la variable que guarda al objeto open 
lectura = open("archivo.txt", "r") 
leer = lectura.read() 

# Si "archivo.txt" contiene las líneas  Holaa! Este es el archivo 
# ¿Qué ocurre cuando imprimimos esta variable? leer = lectura.read() 
leer = lectura.read() 
print(leer) 
""" 
    >> Holaa! 
    >> Este es el archivo 
"""

#----------------------------------------------------------------------------------------------------


# Leer archivos lectura.readline() 
# ● En vez de leer todo el archivo con .read(), se puede leer una línea con .readline() 
# ● Cada vez que se llama a la función, se lee la siguiente línea 

leer = lectura.readline()
print(leer) 
""" 
    >> Holaa! 
"""

leer = lectura.readline() 
print(leer) 
leer2 = lectura.readline() 
print(leer2) 

""" 
    >> Holaa! 
    >> Este es el archivo 
"""

#----------------------------------------------------------------------------------------------------

# Explicación tenemos un archivo .txt llamado archivo.text

a = open("archivo.txt", "r")
print(a)

""" >> <_io.TextIOWrapper name='archivo.txt' mode='r' encoding='cp1252'> """ 

# Aquí hay una explicación de cada parte de la impresión:
#          <_io.TextIOWrapper: Esto indica que el objeto es un "envoltorio de texto de E/S" en Python. 
#                              Es la forma en que Python maneja la lectura y escritura de archivos de texto.
#          name='archivo.txt': Esto indica el nombre del archivo que se ha abierto. En este caso, 
#                              el archivo se llama "archivo.txt".
#          mode='r':           Esto indica el modo en que se abrió el archivo. En este caso, 'r' 
#                              significa que el archivo se abrió en modo de solo lectura.
#          encoding='cp1252':  Esto indica la codificación de caracteres utilizada para interpretar los 
#                              caracteres en el archivo. En este caso, 'cp1252' es un tipo de codificación 
#                              de caracteres que es comúnmente utilizado en sistemas Windows.

# En resumen, la representación que estás viendo describe el archivo "archivo.txt" que se ha abierto en modo de solo lectura y se está utilizando la codificación 'cp1252' para interpretar los caracteres.
 
#---------------------------------------------------------------------------------------------------

# Ejemplo

# Abrir el archivo en modo de lectura ('r')
lectura = open("nuevo_nombre.txt", "r")
# Leer el contenido del archivo
contenido = lectura.read()
# Imprimir el contenido
print(contenido)
# Cerrar el archivo
lectura.close()
