# Tercer Programa Mi RED

## Parte 1
Ahora ya cuentas con un programa que interactúa con el usuario con un menú. Partamos con el programa "Segundo Programa Mi RED" de la semana anterior, que te permitía generar un menú con las siguientes funciones: 

Obtener datos del usuario

* Consultar y mostrar varios mensajes de estado del usuario
* Escoger entre distintas acciones que el usuario puede realizar

En esta ocasión, puedes descargar y examinar los contenidos del archivo 
_**"MiRedS4-Funciones.py"**_

## EJECUTA EL CÓDIGO

Si corres y revisas el código "MiRedS4-Funciones.py" verás que funciona correctamente, pero que es bastante largo. ¡Tiene casi 140 líneas! Esto no es malo. Sin embargo, si le pones atención, verás que hay código que hemos tenido que repetir varias veces. Por ejemplo, el código para mostrar el perfil de usuario está escrito tres veces. Imagina que ahora queremos agregar un nuevo dato del usuario, por ejemplo, el país donde vive. En este caso, deberíamos modificar al menos tres partes distintas del programa. Esto lo podemos hacer, tal vez  sin cometer errores, en un programa pequeño como este. Pero ¿qué pasa con los programas más complejos y largos? En este caso, es muy fácil cometer errores replicando partes del código. Cuando tenemos instrucciones que se repiten varias veces podemos hacer funciones. 

Revisa bien el código, ejecútalo y resuelve el Ejercicio 1 que te proponemos . 

### EJERCICIO 1

Piensa al menos 3 alternativas o funcionalidades del código del archivo "MiRedS4-Funciones.py" que podrían convertirse en función. Modifica el código para incluir estas funciones y no repetir código. 

Cuando hayas terminado de ejecutar el código y programar el Ejercicio 1 contesta al cuestionario "Cuestionario Proyecto Mi Red Parte 1: Identificando funciones".

---

## Parte 2
Ahora ya cuentas con un programa que interactúa con el usuario con un menú y que tiene código encapsulado en funciones. Partamos con el programa "Tercer Programa Mi RED - Parte 1" y tratemos de encapsular el código en distintas funciones. Para partir todos con el mismo código, te pedimos que descargues el archivo 

**_"MiRed4b-Funciones.py"_**

## EJECUTA EL CÓDIGO

Ejecuta el código "MiredS4b-Funciones.py". En este caso, el código permite hacer lo siguiente:

* Mensaje de bienvenida al usuario
* Solicitar datos al usuario
* Mostrar el perfil del usuario
* Mostrar un mensaje en pantalla

Además, este programa organiza en funciones distintas partes del código y las llama desde el programa principal. Como puedes observar en el código, una vez se terminan de definir las funcione, el programa principal empieza a ejecutarse. Si lo lees, verás que es mucho más corto que lo que habíamos programado la semana anterior. 

Revisa bien el código, ejecútalo y resuelve el Ejercicio 1 que te proponemos .

### EJERCICIO 1

Agrega los atributos "género" y "pais de nacimiento" (no pongas tilde en "país" en tu código) a los datos que se le piden al usuario. Realiza un código que solicite datos y los lea utilizando funciones. Identifica qué partes del código que te facilitamos en "MiredS4b-Funciones.py" debes variar para hacerlo.

Cuando hayas terminado de ejecutar el código y programar el Ejercicio 1 contesta al cuestionario "Cuestionario Proyecto Mi Red Parte 2: Utilizando funciones".

---

## Parte 3
Ahora ya cuentas con un programa que interactúa con el usuario con un menú, que tiene código encapsulado en funciones y que tiene un programa principal. Partamos con el programa "Tercer Programa Mi RED - Parte 2" y tratemos de mejorarlo. Para ello, hemos creado un archivo llamado "S4Red.py" donde hemos copiado todas las funciones que tenía nuestro programa.  

**_"S4Red.py"._** 

El archivo "S4Red.py" lo puedes descargar. Te servirá para llamar a las funciones de generadas sin necesidad de poner su código en el archivo donde se encuentra el programa principal con la instrucción "import". Para partir todos con el mismo código, te pedimos que descargues el archivo 

**_"MiRed4c-Funciones.py"._**

## EJECUTA EL CÓDIGO

Ejecuta el código "MiredS4c-Funciones.py". Como puedes ver, la parte principal de tu programa ahora es aún más corta que en tus programas anteriores. Gran parte de las funcionalidades están encapsuladas en funciones que ahora importamos desde el archivo "S4Red.py". 

Al usar funciones, podemos concentrarnos en partes más específicas de nuestro código, y nos ayuda a tenerlo más ordenado y organizado, para pensar mejor. 

Cuando hayas terminado de ejecutar el código y leerlo con atención contesta al cuestionario "Cuestionario Proyecto Mi Red Parte 3: Usando módulos".
