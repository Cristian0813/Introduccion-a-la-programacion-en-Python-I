# CUARTO PROGRAMA MI RED

##  Parte 1

Hasta ahora, cuentas con un programa con las siguientes características: 

- Obtener datos del usuario
- Consultar y mostrar varios mensajes de estado del usuario
- Escoger entre distintas acciones que el usuario puede realizar a partir de un menú
- Modificar el menú de usuario

Todo esto se hace a partir de un programa principal y de un programa que se importa en el principal y que contiene funciones. Esta vez, y dado que tu programa es ahora más corto, podemos centrarnos en el programa principal para evolucionar el código y tu red social. Para hacerlo, descarga los archivos **_"S5Red.py"_** y **_"MiRedS5-Archivos.py"._**

## EJECUTA EL CÓDIGO

Ejecuta el código "MiRedS5-Archivos.py". Habrás notado que cada vez que ejecutas el programa de red social, se tienen que ingresar todos los datos del usuario que está utilizando el programa, antes de poder imprimir el menu de opciones. Esto es bastante engorroso. 

Sin embargo, ahora sabemos que podemos utilizar memoria secundaria de nuestro computador, esto es, espacio del disco, para guardar archivos. Vamos a usar esto para que nuestro programa pueda recordar los datos de los usuarios, y evitar tener que escribirlos en cada ocasión. 

Para hacer esto podemos utilizar la siguiente estrategia: 

- Cada vez que un usuario nuevo utilice nuestro programa, vamos a guardar en un archivo todos sus datos. 
- El nombre de este archivo llevará al nombre del usuario seguido de la extensión ".user". 
- En este archivo guardaremos una línea por cada variable de información sobre el usuario almacenado. 

Con esta solución, conseguiremos que, la próxima vez que ejecutemos nuestro programa, lo primeros que haga sera preguntar el nombre del usuario. Si existe un archivo con el nombre de dicho usuario, lo leeremos desde disco y evitaremos preguntarle sus datos. En caso de que no exista, nuestro programa seguirá comportándose de la misma manera, tratándolo como un usuario nuevo, preguntándole todos los datos, para luego crear un archivo. 

Fíjate en el módulo "S5Red.py". Este incluye un módulo denominado "os". Este módulo nos permite consultar si un archivo existe o no. 

Cuando ejecutes el programa "MiRedS5-Archivos.py" por primera vez, verás que se crea un archivo nuevo en tu computador cada vez que ingresas con el nombre de un usuario nuevo. Prueba a ingresar con un nombre de usuario que ya hayas usado antes. 

Este programa es bastante más completo de los que teníamos antes. Sin embargo, aún quedan cosas por mejorar. Por ejemplo, ¿qué ocurre si el archivo está mal escrito, o si le falta alguna línea? ¿Qué ocurre si en una ocasión ingreso mi nombre en mayúsculas y en otra con minúsculas? Ejecuta varias veces el programa "MiRedS5-Archivos.py", analízalo y realiza los Ejercicios 1 y 2 para mejorarlo.

### EJERCICIO 1

Al leer las líneas del archivo, siempre se leen como últimos caracteres algunos caracteres blancos, como espacios o el caracter cambio de línea ('\n'). Esto hace que los nombres de archivos creados incluyan estos caracteres adicionales. Utiliza los métodos de 'str' para elminar este tipo de caracteres que denominamos "no imprimibles". Es decir, "limpia" toda línea que leas, de manera que no tengan caracteres adicionales a lo esperado (ya sean saltos de línea y/o espacios en blanco).

### EJERCICIO 2

Utiliza tu conocimiento de funciones para crear funciones que lean desde un archivo, y retornen el conjunto de datos leídos, de manera de encapsular el proceso de lectura y escritura, y reducir el tamaño de tu código. 

---

## Parte 2

De la versión del programa anterior (Cuarto Programa MI RED - Parte 1) has podido construir un programa que contiene varias funciones adicionales y que se han almacenado en el fichero "S5Red2". En el fichero "MiRedS5b-Archivos.py" puede encontrar la versión del programa que utiliza archivos para almacenar y leer los datos de cada usuario de nuestra red. Parte de este fichero para extender el programa y hacerlo algo más complejo.

**_"S5Red2.py"_**
**_"MiRedS5b-Archivos.py"._**

## EJECUTA EL CÓDIGO

Ejecuta el código "MiRedS5b-Archivos.py". Habrás notado que este programa almacena archivos para almacenar y leer datos de cada usuario de nuestra red.  Revisa el contenidos del código, analízalo y realiza los ejercicios 1 y 2 que te proponemos a continuación. Estos ejercicios te ayudarán a comprender mejor el programa y a responder el cuestionario de evaluación.

### EJERCICIO 1

Ingresa  al programa de red social con distintos usuarios. Después de esto, tendrás varios archivos generados con extensión '.user'. Abre cualquiera de estos archivos con un editor de texto y edita alguno de los valores del fichero. Por ejemplo, cambia el nombre de usuario de alguno de los usuarios de la red. A continuación, ejecuta de nuevo tu programa y entra con el nombre de uno de los usuarios que constaba en alguno de los archivos con extensión '.user'. ¿Se han actualizado los datos que cambiaste en el fichero? Prueba esto varias veces a ver qué ocurre.

### EJERCICIO 2

Agrega al menú una nueva opción que se llame "Cambiar de usuario". Esta opción debe permitir al usuario que está en el programa, sin salirse de la red, solicitar un nuevo nombre de usuario y, en caso de que exista un archivo con este nombre, cargar sus datos. Si el archivo no existe, basta con indicar que no se puede cambiar este usuario.

