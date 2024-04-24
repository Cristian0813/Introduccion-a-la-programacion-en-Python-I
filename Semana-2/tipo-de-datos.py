""" # ¿QUÉ VALORES PUEDES USAR? TIPOS DE DATOS 
#Representando letras y números 
#
#Tipos básicos o primitivos 
# • Tipos numéricos: int, float 
# • Tipos de texto: str 
# • Tipos lógicos (booleanos): bool

#Tipo de dato int Números enteros 
# • int representa números enteros como
# 0 1 2 42 17948141 -89 -139 2017 33  
#
#Ejemplos
entero = type(42)
print("El tipo de dato es: ", entero)
#>>> type(42)  <class 'int'>
entero = type(-139)
print("El tipo de dato es: ", entero)
#>>> type(-139) <class 'int'>

# Tipo de dato float Números con punto flotante
# • float representa números con punto decimal 
# 0.5 3.933333333 5.0 1.25 12. 23.01 -42.3899
#
# Ejemplos
flotante = type(1.25)
print("El tipo de dato es: ", flotante)
#>>>type(1.25) <class 'float'>
flotante = type(-03.23)
print("El tipo de dato es: ", flotante)
# >>>type(-3.0) <class 'float'>

# Tipo de dato str Texto o string 
# • str representa secuencias o cadenas (string) de caracteres. 
# "J" "Cristian" "¿2+2 = 5?" "4" 'Tengo 10 amigos' 
# "Aprendo a programar" '-3.0' "98394255"
#
# Ejemplos
string = type ("Quiero Aprender Python")
print("El tipo de dato es: ", string)
# >>> type("Quiero Aprender Python") <class 'str'>

# Tipo de dato bool ¿Verdadero o Falso? 
# • bool representa valores booleanos o de lógica binaria:
# Verdadero o Falso
# 
# Ejemplos
boleano = type(True)
print("El tipo de dato es: ", boleano)
#>>> type(True) <class 'bool'>
#>>> type(true) <NameError: name 'false' is not defined>
boleano = type(False)
print("El tipo de dato es: ", boleano)
#>>> type(False) <class 'bool'>
#>>> type(false) <NameError: name 'false' is not defined>

# ===================================================================================================

# CALCULANDO VALORES OPERADORES Y EXPRESIONES
# Operadores para tipos numéricos Operadores aritméticos 
#
#• Operadores sobre int y float 
# Suma + >>> 7+5 Salida 12
suma = 7 + 5
print (suma)

# Resta - >>> 7-5 Salida 2
resta = 7 - 5
print (resta)

# Multiplicación *  >>> 7*5 Salida 35
multiplicacion = 7 * 5
print (multiplicacion)

# División / >>> 7/5 Salida 1.4
division = 7 /5 
print(division)
 
# Inverso aditivo +/- >>> -5 Salida -5
inverso = -5
print(inverso)

# Exponenciación ** >>> 7**5  Salida 16807
Exponenciacion = 7 ** 5
print(Exponenciacion)

# División entera // >>> 7//5 Salida 1
division_entera = 7 // 5
print(division_entera)

# Módulo % >>> 7%5 Salida 2
modulo = 7 % 5
print(modulo)

# >> (3+5//4-2)-2**4+3*(7-2) Salida 1 
#
#• Expresiones con más de un operador
#  se evalúan por precedencia
#• Operaciones con igual precedencia se resuelven 
#  por orden de asociatividad
#• Dentro de cada paréntesis se evalúa: 


#  __________________________________________________________________________
#  | Operador           | Preced. | Asociatividad     | Ejemplo | Resultado |
#  |--------------------|---------|-------------------|---------|-----------|
#  | **                 | 1       | Derecha Izquierda | 2**3**2 | 512       |
#  |--------------------|---------|-------------------|---------|-----------|
#  | +,-                | 2       |                   | -2**2   | -4        |
#  |--------------------|---------|-------------------|---------|-----------|
#  | *,/,//,%  (unarios)| 3       | Izquierda Derecha | 15/3*2  | 10        |
#  |--------------------|---------|-------------------|---------|-----------|
#  | +,- (binarios)     | 4       | Izquierda Derecha | 3-4+5   | 4         |
#  |--------------------|---------|-------------------|---------|-----------|  


#• Se aplican a int o float 
#  <  <=  >  >=  !=  == 
#
#• Siempre entregan un tipo bool 
#
# Menor < >>> 5<5.1 Salida True
menor = 5 < 5.1
print(menor)

# Mayor o igual >= >>> 3>=5 Salida False
mayor_o_igual = 3 >= 5
print(mayor_o_igual)

# Distinto != >>> 3!=5 Salida True
distinto = 3 != 5
print(distinto)

# Igualdad == >>> 6==9 Salida False
igualdad = 6 == 9
print(igualdad)


#• Se aplican a bool not and or 
#
#• Siempre entregan un tipo bool 
#
# Negación not >>> not 3>5 Salida True
negación = not (3 > 5)
print(negación)
# Conjunción lógica (Y) and >>> 3>5 and 2<6 Salida False
conjunción_y = (3 > 5) and (2 < 6)
print(conjunción_y)

# Disyunción lógica (O) or  >>> 3>5 or 2<6  Salida True
disyunción_o = (3 > 5) or (2 < 6)
print(disyunción_o)


#  _______________________________________________________________________________
#  | Operador           | Asociatividad     | Ejemplo                | Resultado |
#  |--------------------|-------------------|------------------------|-----------|
#  | <,<=,>,>=,!=,==    | Derecha Izquierda | 3<4<=4<5               | True      |
#  |--------------------|-------------------|------------------------|-----------|
#  | not                | Izquierda Derecha | not not 5>2            | True      |
#  |--------------------|-------------------|------------------------|-----------|
#  | and                |                   | not True and False     | False     |
#  |--------------------|-------------------|------------------------|-----------|
#  | or                 | Izquierda Derecha | True or True and False | True      |
#  |--------------------|-------------------|------------------------|-----------|  


# Ante la duda, use paréntesis 
# Paréntesis tienen la mayor prioridad 
#
# >>> 5//4 > 3 or 2<5**2 Salida True 
confusión = 5 // 4 > 3 or 2 < 5 **  2
print(confusión)
#
# • Es equivalente a: 
# >>> ((5//4) > 3) or (2<(5**2)) Salida True
explicación = (5 // 4) > 3 or 2 < (5 ** 2)
print(explicación)


# • Operadores para str 
#
# Concatenación + >>> "Yo soy " + "tu padre" Salida 'Yo soy tu padre'                
concatenación = "Yo soy " + "tu padre"
print(concatenación)

# Repetición * >>> "Ja" * 4  Salida 'JaJaJaJa'
repetición = "Ja" * 4
print(repetición)

# ===================================================================================================

# MANICPULACIÓN DATOS CONVERSIÓN DE TIPOS

# • Operando con valores Valores del mismo tipo 
# >>> 3*9 Salida 27 
operando_del_mismo_tipo = 3 * 9
print(operando_del_mismo_tipo)
#
# >>> 5.2+2.37 Salida 7.57
suma_de_diferentes_tipos = 5.2 + 2.37
print(suma_de_diferentes_tipos)
#
# >>> 3<=5 and 7>6.5 Salida True
comparaciones_conversiones = 3 <= 5 and 7 > 6.5
print(comparaciones_conversiones)
#
# >>> "¿Dónde queda " + "Chañaral?" Salida '¿Dónde queda Chañaral?'
cadena1 = "¿Dónde queda "
cadena2 = "Chañaral?"
concatenacion_cadenas = cadena1 + cadena2
print(concatenacion_cadenas)


# • Operando con valores Tipos de expresiones 
#
# >>> type(3*9) Salida <class 'int'> 
tipo_expresion_entera = type(3 * 9)
print(tipo_expresion_entera)
#
# >>> type(5.2 + 2.37) Salida <class 'float'> 
tipo_expresion_decimal = type(5.2 + 2.37)
print(tipo_expresion_decimal)
#
# >>> type(3 <= 5 and 7 > 6.5) Salida <class 'bool'>
tipo_expresion_logica = type(3 <= 5 and 7 > 6.5)
print(tipo_expresion_logica)
#
# >>> type("¿Dónde queda " + "Chañaral?") Salida <class 'str'>
tipo_expresion_cadena = type("¿Dónde queda " + "Chañaral?")
print(tipo_expresion_cadena)


# • Operando con valores Valores de distinto tipo 
# >>> 3 * 5.37 Salida 16.11
multiplicacion_distinto_tipo = 3 * 5.37
print(multiplicacion_distinto_tipo)
# 
# >>> 8 / 1.5 Salida 5.3333333333333333
division_distinto_tipo = 8 / 1.5
print(division_distinto_tipo)
#
# >>> "Son las " + (3 + 12) Salida TypeError: Can´t convert 'int' object to str implicitly
suma_y_conversion = "Son las " + (3 + 12)
print(suma_y_conversion)


# • Operando con tipos distintos Tipos de expresiones 
# >>> 3 * 5.37 Salida 16.11
valor_entero = 3
valor_decimal= 5.37
resultado_multiplicacion = valor_entero * valor_decimal
print(type(resultado_multiplicacion))
#
# >>> 8 / 1.5 Salida 5.3333333333333333
valor_real = 8
valor_complejo = 1.5
resultado_division = valor_real / valor_complejo
print(type(resultado_division))
#
# >>> "Son las " + 15 Salida TypeError: Can´t convert 'int' object to str implicitly
mensaje = "Son las "
numero = 15
resultado_concatenacion = mensaje + numero
print(type(resultado_concatenacion), resultado_concatenacion)


# • Conversión de valores str() al rescate 
# >>> str(15) Salida '15'
conversion_str = str(15)
print(conversion_str)
#
# >>> type(str(22)) Salida <class 'str'>
clase_de_dato = type(str(15))
print(clase_de_dato)
#
# >>> "Son las " + (3 + 12) > Salida 'Son las 15'
mensaje = "Son las "
numero = 3 + 12
resultado_concatenacion = mensaje + str(numero)
print(resultado_concatenacion)


# • Conversiones a int 
# >>> int(3.55546) Salida 3
valor_decimal = 3.55546
resultado_redondeo_abajo = int(valor_decimal)
print(resultado_redondeo_abajo)
#
# >>> int("3") + 12 Salida 15
suma_entre_enteros = int("3") + 12
print(suma_entre_enteros)
#
# >>> int("El 3") Salida ValueError: invalid literal for int() with base 10: 'El 3'
error_literal = int("El 3")
print(error_literal)


# • Conversiones a float 
# >>> float(3) Salida 3.0
entero_convertido_a_flotante = float(3)
print(entero_convertido_a_flotante)
#
# >>> float("3.5") + 12 Salida 15.5
suma_entre_flotantes = float("3.5") + 12
print(suma_entre_flotantes)
#
# >>> float("3.5s") Salida ValueError: could not convert string to float: '3.5s' 
error_letra = float("3.5s")
print(error_letra)


# • Conversiones de tipos bool()
#   0ó""es False, el resto es True 
# >>> bool(0) Salida False
bool_cero = bool(0)
print(bool_cero)
#
# >>> bool(15.5) Salida True
bool_décima = bool(15.5)
print(bool_décima)
#
# >>> bool("False") Salida True
bool_string_falso = bool("False")
print(bool_string_falso)
#
# >>> bool("") Salida False
bool_vacío = bool("")
print(bool_vacío)
#
# >>> bool("True") Salida True
bool_string_verdadero = bool("True")
print(bool_string_verdadero)
#
# >>> bool("0") Salida True
bool_string_cero = bool("0")
print(bool_string_cero)


# • Conversiones a str 
# >>> str(3.0) Salida '3.0'
conversion_entero_str = str(3)
print(conversion_entero_str)
#
# >>> str(8 + 1.76) + " segundos" Salida '9.76 segundos'
conversion_decimal_str = str(8+1.76) + " segundos"
print(conversion_decimal_str)
#
# >>> str(3<5 and 9.76 < 10) Salida 'True'
conversion_logica_str = str(3<5 and 9.76 < 10)
print(conversion_logica_str)

# =================================================================================================== """

# RECORDANDO VALORES. VARIABLES Y ASIGNACIÓN

#Recordando valores ¿Para qué recordar valores? 
#
#>>> (19-14)*200 Salida 1000
resultado_valores = (19 - 14) * 200
print(resultado_valores)
#
# Objetivo: Recordar valores para usarlos posteriormente
# • Asignamos un nombre a un valor
# • A estos nombres le llamamos variables


# Recordando valores ¿Cómo se guardan? 
# >>> llegada = 14 
# >>> (19-llegada)*200 Salida 1000
llegada = 14
resta_y_asignacion = (19 - llegada) *  200
print(resta_y_asignacion)

# • = asigna un valor a una variable 
# • Recuperamos el valor usando el nombre de la variable 


# Recordando valores Asignando valores a variables 
# >>> pesos_por_hora = 200 
# >>> llegada = 14 
# >>> (19-llegada)*pesos_por_hora Salida 1000
pesos_por_hora = 200
llegada = 14
calculo_parqueadero = (19 - llegada) * pesos_por_hora
print(calculo_parqueadero)
# >>> llegada = 20 
# >>> salida = 22 
# >>> (salida-llegada)*pesos_por_hora Salida 400
llegada = 20
salida = 22
horas_parqueadero = (salida - llegada) * pesos_por_hora
print(horas_parqueadero)


# Instrucción de asignación Asignación: = 
# nombre = expresión
#
# >>> r = 5 
# >>> pi = 3.14159 
# >>> s = "El área es" 
# >>> area= pi * r**2 
# >>> area  Salida 78.53795
r = 5
pi = 3.14159
s = "El área es"
area = pi * r ** 2
print(area)
  
#                     💻
#                /-----------\
#               /   Memoria   \
#       _______/---------------\
#       \  r   |       5       |
#       _\-----|---------------|
#       \  pi  |    3.14159    |
#       _\-----|---------------|
#       \ area | "El área es " |
#       _\-----|---------------|
#       \      |               |
#       _\-----|---------------|





# Reasignando valores  Asignación 
# nombre = expresión
# >>> r = 12.8 
# >>> r + 10 Salida 22.8 
# >>> area Salida 78.53795
# memoria r5 pi3.14159 s"El área es " area 78.53795 12.8

# ¡Cuidado! Las variables deben existir
# nombre = expresión
# >>> r = 12.8 
# >>> r + 10 Salida 22.8 
# >>> area Salida 78.53795
# >>> area = pi * radio ** 2 Salida NameError: name 'radio' is not defined 
# memoria r5 pi3.14159 s"El área es " area 78.53795 r 12.8


# Nombres de variables  ¿Qué nombres puedo usar? 
# • Debenempezar con una letra o '_' 
# • Puede seguir con letras, números, '_' 
# ✔️ pesos_por_hora   || ✖️ Min+Seg
# ✔️ i                || ✖️ 12deLaNoche 
# ✔️ Clark            || ✖️ Bruce Wayne
# ✔️ _CRISTIAN        || ✖️ 
# ✔️ km20s            || ✖️
# ✔️ vAlErIa          || ✖️ 
# ✔️ j0rg3            || ✖️
#  • Las mayúsculas / minúsculas importan 
# Vivaldi ≠ vivaldi ≠ viValdi ≠ VIVALDI 


# Nombres de variables Palabras reservadas 
#
# • Estas palabras NUNCA pueden ser usadas 
#
# and      || del     || from   || nonlocal || while 
# as       || elif    || global || not      || with
# assert   || else    || if     || or       || yield
# break    || except  || import || pass     || True 
# class    || exec    || in     || raise    || False 
# continue || finally || is     || return   || None
# def      || for     || lambda || try      || 