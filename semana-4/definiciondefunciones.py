# DEFINICIÓN DE FUNCIONES

# Estructura básica 
# Escribiendo funciones 

# Se debe tener en cuenta lo siguiente: 
# 1. Comienzan con def. 
# 2. Nombre. 
# 3. Paréntesis, que pueden llevar los parámetros dentro. 
# 4. Se tienen que indicar los dos puntos. 
# 5. El código y los retornos, indentados. 

#-------------------------------------------------------------------------------------------------------------------------

# Estructura tipo 
# El siguiente código corresponde a 
# una estructura tipo de una función: 

def nombre(parametro1, parametro2, parametroN): 
    # aquí va el código de la función 
    # y todo lo relacionado, las 
    # variables usadas, los retornos 
    valor = 0 
    return valor

#-------------------------------------------------------------------------------------------------------------------------

# Un ejemplo 
# La siguiente función retorna el divisor más grande de un 
#número n dado (excluyéndolo): 

def max_divisor(n):             # => Def, nombre, paréntesis y parámetros
    maximo_actual = 0           #  ‾↓
    i = 1                       # Código
    while i < n:                # de 
        if n % i == 0:          # la
            maximo_actual = i   # función
            i += 1              #  _↑
        return maximo_actual    # => Retorno de la función

#-------------------------------------------------------------------------------------------------------------------------

# Otros ejemplos 
# En muchos casos las funciones tienen múltiples parámetros y retornos: 

def potencia_positiva(base, exponente): 
    if exponente == 0: 
        return 1 
    else: 
        resultado = 1 
        while exponente > 0: 
            resultado *= base 
            exponente -= 1 
        return resultado  

#-------------------------------------------------------------------------------------------------------------------------

# Consideraciones 
# • Las funciones se definen una única vez. 
# • Para llamar a una función, ésta debe estar definida antes del llamado.