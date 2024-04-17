# Guía resolución Cuestionarios Prácticos

## GUÍA PARA RESOLVER CUESTIONARIOS PRÁCTICOS  

A partir de la segunda semana del curso es necesario resolver cuestionarios prácticos de programación para aprobar. Si bien las cosas más importantes para poder responder las preguntas de cada semana serán enseñadas en las lecciones de la unidad respectiva, es importante saber el modo de responder estas preguntas. 

La principal dificultad radica en que el código debe integrarse dentro de una función, concepto que se ve recién en la cuarta semana del curso. Sin embargo, no es necesario conocer con entereza cómo operan las funciones para poder responder estos cuestionarios. 

El código que verán en cada pregunta será de la siguiente forma:

````python
def funcion(a, b):
  c = a + b
  return c
````

En la primera línea lo más importante son los términos entre paréntesis. Estos son los parámetros de la función, y son los valores que necesitamos para realizar las operaciones que debe hacer nuestra función. Si, por ejemplo, queremos saludar a alguien, el parámetro que necesitará la función será el nombre de la persona a saludar. O, si queremos sumar dos números (como en la imagen de arriba), los parámetros serán los sumandos.   

En el cuerpo de la función pondremos las operaciones que debemos realizar para obtener el resultado buscado. Y una vez que tengamos en una variable el valor que nos piden, debemos retornarlo. Esto es lo que hacemos para devolver el valor solicitado. Es decir, si nos piden una función que sume dos números, tendremos que retornar la suma de los dos sumandos. Siendo los parámetros a y b, esto puede hacerse de dos maneras equivalentes: c = a + b y después return c, o bien directamente return a + b. 

Algo importante para que funcione el código entregado en el cuestionario es no poner ninguna instrucción print, ni tampoco cambiarle el nombre a la función o a los parámetros. Además, si el valor a retornar es un string, se debe tener cuidado en que este sea exactamente igual a lo pedido (lo que se debe comprobar con el ejemplo que siempre se da). Un último punto importante es notar que el intérprete de Coursera es Python 3, por lo que si se usa Python 2 en PyCharm puede ocurrir que el mismo código no funcione cuando se mande por la plataforma. Por esto se aconseja ocupar siempre Python 3 y ahorrarse cualquier problema. 

Si se tienen problemas en la resolución de alguno de estos ejercicios, son más que bienvenidos a plantear las dudas en el foro. No obstante, se pide encarecidamente que no pongan código en sus mensajes, ya que el resto de los alumnos pierde la oportunidad de aprender por los propios medios.  

¡Saludos, mucha suerte y ánimo! 
