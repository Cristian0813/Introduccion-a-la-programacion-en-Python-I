# Flujo cíclico: while

# Ejemplo 
#Programa que imprime conversiones 

print("fº cº") 
print("32 0") 
print("42 5") 
print("52 11") 
print("62 16") 
print("72 22")

# Instrucción ciclo: while 
# flujo cíclico

#instrucción cíclica 

# while condición: # => indentación 
#     instrucciones # => dentro while
#
#     while: nos permite repetir 
#     tantas veces como queramos 
#     un conjunto de instrucciones

# Ejemplo while 
# Programa para convertir fahrenheita celsius 

temp=32 
print("fº cº") 
# while temp sea menora 73: 
#     imprimir temp y su conversióna Cº sumar 1 a temp

temp=32 
print("fº cº") 
while temp<73: 
    print(temp," ",int((temp-32)*5/9)) 
    temp=temp+1
# Print fº cº
# Print 32   0
# Print 33   0
# Print 34   1
# Print 35   1
# Print 36   2
# Print 37   2
# Print 38   3
# Print 39   3
# Print 40   4
# Print 41   5
# Print 42   5
# Print 43   6
# Print 44   6
# Print 45   7
# Print 46   7
# Print 47   8
# Print 48   8
# Print 49   9
# Print 50   10
# Print 51   10
# Print 52   11
# Print 53   11
# Print 54   12
# Print 55   12
# Print 56   13
# Print 57   13
# Print 58   14
# Print 59   15
# Print 60   15
# Print 61   16
# Print 62   16
# Print 63   17
# Print 64   17
# Print 65   18
# Print 66   18
# Print 67   19
# Print 68   20
# Print 69   20
# Print 70   21
# Print 71   21
# Print 72   22

temp=32 
print("fº cº") 
while temp<73: 
    print(temp," ",int((temp-32)*5/9))

# Resumiendo 
# Instrucción de ciclo: while 

# • Instrucción de ciclo: while 
#     while condición: 
#         instrucciones 

# • Si condicion es True, se ejecuta el código dentro de while 
# • Si condicion es False, se ejecuta el código que sigue al while


# Flujo cíclico for

# Ejemplo while 
# Programa para convertir fahrenheita celsius 

temp=0 
print("fº cº") 
while temp<21: 
    print(temp," ",int((temp-32)*5/9)) 
    temp=temp+1

# Ejemplo for 
# Programa para convertir fahrenheita celsius 

print("fº cº") 
for temp in range(21): 
    print(temp," ",int((temp-32)*5/9))

# Uso de range 
# Creando secuencias de números sobre las cuales iterar 

# • Usamos una nueva expresión: range(fin) 
# • Rangecrea una secuencia de números, que parte desde 0 y llega hasta fin – 1. 

for i in range(7): 
    print(i) 
    
# • range(inicio, fin) crea una secuencia de números, que parte desde inicio y llega hasta fin – 1. 
for i in range(8,14): 
    print(i) 
    
# • range(inicio, fin, paso) crea una secuencia de números, que parte desde inicio 
#   y llega hasta fin – 1, avanzando de a paso números. 

for i in range(4,101,3): 
    print(i) 
    
# Instrucción ciclo: for 

# for variable in secuencia: => Identación
#     instrucciones => dentro de for 

# for: nos permite recorrer elemento por elemento una secuencia. 
# Podemos generar secuencias con range. 

# for Comparado con while… 

for i in range(1,100): 
    if i<18:
        print(i, "menor de edad") 
    else:
        print(i, "mayor de edad")
     
i = 1 
while i < 100: 
    if i<18: 
        print(i, "menor de edad") 
    else: 
        print(i, "mayor de edad") 
    i = i+1
        
# Resumiendo 

# • Instrucción de ciclo: for 
# for variable in range(i,j,k): 
#     instrucciones 

# • Genera secuencia desde i hasta j-1, con paso k, e itera sobre ella (i, k opcionales)}


