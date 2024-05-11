# Pregunta 1 Determina el valor de x al final del siguiente código:

x = 1
i = 0
while i < 4:
    x = x * 2
    i += 1 # es lo mismo que i = i + 1
print(x) # Print 16

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# Pregunta 2 Al final de este código:

x = 48
y = 8
n = 0
while x > 0:
    x = x - y
    n = n + 1

# El valor de n es:
print(n) # Print x // y

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# Pregunta 3 Considerando las variables del siguiente código:

a = 5
b = 8
r = 0
while a > 0:
    r = r + b
    a = a - 1
print(r) 

#El output del mismo es equivalente a imprimir:
# Print  a * b

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# pregunta 4 Determina una opción que entregue el mismo resultado que el código a continuación:

a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1

# Print b ** a

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------



# Pregunta 5 ¿Cuál es el valor de a tras la ejecución de este programa?

a = 3
for i in range(2, 3):
    a = a * i
print(a) # Print 6

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# Pregunta 6 ¿Qué debería ir en lugar de OBJECT en el siguiente código

a = 2
for i in OBJECT:  # type: ignore
    a = i ** a
print(a) # Print range(1, 4)

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# Pregunta 7 Determine lo que debiese ir en lugar de OBJECT para que el siguiente código

for i in OBJECT: # type: ignore
    print('hola mundo')

range(10)


print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

# Pregunta 8 Determine lo que imprime este programa

a = 0
for i in range(3):
    a = a + i
print(a)

# Print 3

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------

#Pregunta 9 ¿Qué hace el siguiente código?

numero = 1
while numero <= 5:
  print(numero, numero**2)
# print Escribe "1 1" infinitas veces.

print()
print("|------------------------------------------------------------------|")
print()

#---------------------------------------------------------------------------------


# Pregunta 10 ¿Qué imprime el siguiente código?

123
for i in range(1,101):
  for j in range(1,101):
    print(i,j)
# Print Para cada número del 1 al 100, imprime los números del 1 al 100, por lo tanto imprime 1 1, 1 2, 1 3, 1 4, ..., 1 100, 2 1, 2 2, 2 3, ..., 100 100


