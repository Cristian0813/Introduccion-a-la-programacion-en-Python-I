# Pregunta 1 Escribe una función que reciba dos strings (de largo > 2) como parámetros, 
# y retorne un string de largo 4 que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.

# Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".

def mezclar(string_a, string_b):
   primera_letra = (string_a[:2])
   segunda_letra = (string_b[-2:])
   return primera_letra + segunda_letra

resultado = mezclar("familia", "abrigo")
print(resultado)


print()
print("---------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------

# Pregunta 2 Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que 
# consista del primero, pero con el segundo string intercalado entre cada letra del primero.

# Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"

def intercalar(string_a, string_b):
    resultado = ""
    i = 0
    while i < len(string_a):
       resultado += string_a[i] + string_b
       i += 1
    return resultado

print(intercalar("paz", "so"))
print(intercalar("chao", "hu"))

print()
print("---------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------

# Pregunta 3 Escriba una función que reciba un string consistente de unos y ceros y retorne la 
# cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.

# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)

def ocurrencias(string):
    contador_uno = 0
    contador_dos = 0
    for char in string:
        if char == '1':
            contador_uno +=1
        elif char == '0':
            contador_dos += 1
        else:            
            print("El string contiene caracteres diferentes de '0' y '1'")
    return contador_uno - contador_dos

# Ejemplo de uso:
resultado = ocurrencias("11000110101")
print(resultado)  # Debería imprimir: 1

print()
print("---------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------

# Pregunta 4 Escriba una función que reciba un string s y un número n como parámetros y 
# retorne el mismo string s pero sin el elemento en el índice n.

# Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".
# Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.

def remover_enesimo(s, n):
  if n < 0 or n >= len(s):
    print("El indice está fuera de los lomites")
    return None    
  return s[:n] + s[n+1:] 
print(remover_enesimo("Hasta luego", 3))

print()
print("---------------------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------------------

# Pregunta 5 Escriba una función que reciba un string como parámetro y retorne el string, pero con 
# cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.

# Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".

def reemplazo(string):
  resultado = ''
  for char in string:
    if char.isupper():
      resultado += '$'
    else:
      resultado += char
  return resultado

print(reemplazo("Viva la Vida"))
