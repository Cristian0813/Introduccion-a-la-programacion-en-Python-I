# INSTRUCCIONES DE FLUJO  CONDICIONAL


# Flujo condicional IF - ELSE
#
#
# TOMA DECISIONES
# ¿Como hacer que el programa decida?
#
# Objetivo: Lograr que el programa decida en base a una condición  
# Condición 
# • Si la condición es verdadera, la persona realizará una acción. 
# • Si la condición es falsa, realizará otra acción 
#
# Operadores de comparación
# 
""" Menor <  """; 5 < 5.1  #True
""" Menor o igual <= """; 44<=50 #True
""" Mayor > """; 2 > 8 #False
""" Mayor o igual >= """; 3 >=5  #False
""" Distinto """;  3!=5  #True
""" Igual """; 6==9  #False

# ¿Qué valor entregará a <= b, si a=10 y b=7?
a = 10
b  = 7
a<=b  #False

# Operadores para tipos lógicos
# not and or
""" Negación --> not """;  not 3>5  #True

""" Conjunción --> and """;  3>5 and 2<6  #False

""" Disyunción --> or """;  3>5 or 2<6  #True


# Flujo condicional IF

# • Ejemplos if

llueve=True 
if llueve==True: 
    print("Llevaré paraguas") 
else: 
   print("No llevaré paraguas") # Print Llevaré paraguas
print("Ahora saldré a la calle") # Print Ahora saldré a la calle

llueve=True 
temperatura=12 
if llueve==True and temperatura <20: 
    print("Llevaré paraguas y abrigo") 
else: 
    print("No necesito paraguas o abrigo") # Print Llevaré paraguas y abrigo

# Resumiendo 
# • Instrucción de flujo condicional: if-else 
#
# if condición: 
#     instrucción1 
# else: 
#     instrucción2 
#
# • Si condición es True, se ejecuta el código dentro de if. 
# • Si condición es False, se ejecuta el código dentro de else.


# • Ejemplo if sin else
#   Podemos omitir el else

charco = True 
print("Comienza la caminata!") # Print Comienza la caminata! 
if charco==True: 
    print("Asaltar!") # Print A saltar! 
print("Fin de la caminata") # Print Fin de la caminata

charco = False 
print("Comienza la caminata!")  # Print Comienza la caminata! 
if charco==True: 
    print("Asaltar!") 
print("Fin de la caminata") # Print Fin de la caminata

# • else sin if
#   No puede haber else sin if

""" charco = False 
else: 
    print("No saltaré") 
print("Sigo caminando") """
# Print
#     else:
#     ^^^^
# SyntaxError: invalid syntax

""" charco = False 
if charco == True: 
    print("A saltar!") 
print("Sigo caminando") 
else: 
   print("No saltaré") """
# Print
#     else:
#     ^^^^
# SyntaxError: invalid syntax

# Resumiendo 
# Instrucción de flujo condicional: if 
# • Instrucción de flujo condicional: if 

# if condición: instrucción1 
# instrucción2 

# • Si condicion es True, se ejecuta el código dentro de if 
# • Condiciones simples y complejas



# Flujo condicional ELIF

# Tomando decisiones más complejas 
# Usando if/else anidados


llueve=True 
temperatura=int(input("Ingresa tempº ")) 
if temperatura < 18: 
    if llueve==True: 
        print("Llevaré paraguas y abrigo") 
    else: print("Solo llevaré abrigo") 
else: print("No necesito paraguas ni abrigo")

# Instrucción condicional:

# elif Flujo con 2 condiciones 
# if condición1: 
#     instrucción1 
# elif condición2: 
#     instrucción2 
# else: 
#     instrucción3

# Programa que decide en base a dos condiciones 
#
# • Ejemplo elif

llueve = True 
temperatura=int(input("Ingresa tempº ")) 
if temperatura < 18 and llueve==True: 
    print("Llevaré paraguas y abrigo") 
elif temperatura < 18 and llueve == False: 
    print("Solo llevaré abrigo") 
else: print("No llevaré paraguas ni abrigo")


llueve = True 
temperatura = int(input("Ingresa tempº ")) 
if temperatura >= 18: 
    print("No llevaré paraguas ni abrigo") 
elif llueve == True: 
    print("Llevaré paraguas y abrigo") 
else: 
   print("Solo llevaré abrigo")

# Resumiendo 
# • Instrucción de flujo condicional: if-else 
# if condición1:          
#     instrucción1        • Si condicion1 es True, se ejecuta la instrucción1
# elif condición2: 
#     instrucción2        • Si condicion2 es True, se ejecuta la instrucción2
# elif condición3: 
#     instrucción3        • ...
# ... 
# else: 
#    instrucciónN          • Si ninguna de las anteriores es True, se ejecuta la instrucciónN
