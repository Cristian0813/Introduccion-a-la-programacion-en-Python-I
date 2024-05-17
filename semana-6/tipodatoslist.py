# LISTAS DE ELEMENTOS TIPO LIST

# Comprender como escribr listas en Python 

# Objetivo:	Comprender	como	escribr listas	en	Python
# • Listas en la vida diaria Listade vuelos 
#       Lista de compras 
#       Lista de vuelos 
#       Lista de tareas 
#       Lista de películas 
#       Lista de libros 
#       Lista de amigos
# • Listas en el lenguaje de programación 


#---------------------------------------------------------------------------------------------

# Listas 
# Escribiendo

# No olvidar
#   ┌──────────────┐
#   │ □ "huevos"   │
#   ├──────────────┤
#   │ □ "palta"    │
#   ├──────────────┤
#   │ □ "lechuga"  │
#   ├──────────────┤
#   │ □ "naranjas" │
#   ├──────────────┤
#   │ □ $ 7000     │
#   └──────────────┘
#           ↓
no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 

# • Listas como secuencias de elementos 
# • Elementos puede ser de cualquier tipo 
# • Elementos se encuentran ordenados Escribiendo listas listaSupermercado.py 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Tipo de dato: list Tipo de dato: 
# Sintaxis de listas 

#   ┌───────────────────────────────────────────────┐
#   │ list [elemento0, elemento1, ..., elementoN-1] │
#   └───────────────────────────────────────────────┘
 
# • 0 o más elementos, de cualquier tipo
no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 
print(type(no_olvidar)) 
""" 
    >> <class 'list'> 
""" 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Tipo de dato: list Definiendo listas

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 
print(no_olvidar) 
""" 
    >> ['huevos', 'palta', 'lechuga', 'naranjas', 7000] 
""" 
# • Elementos puede ser de cualquier tipo 
# • Elementos se encuentran ordenados 

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Tipode dato: list Listas con variables y expresiones 

mesa = 5 
producto = "espresso" 
cantidad = 2 
costo = 500 
pedido = [producto, mesa, cantidad, costo, cantidad*costo] 
print(pedido) 
""" 
    >> ['espresso', 5, 2, 500, 1000] 
""" 
# • Podemos usar variables y expresiones 1 2 3 4 5 6

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Tipode dato: list 
# Listas con listas 
unpedido= ["espresso", 5, 2, 500, 1000] 
otropedido= ["cortado", 8, 3, 800, 2400] 
especial = ["café del día", 10] 
pedidos = [unpedido, otropedido, especial, True] 
print(pedidos) 
""" 
    >> [['espresso', 5, 2, 500, 1000], ['cortado', 8, 3, 800, 2400], ['café del día', 10], True] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Tipode dato: list 
# Listas vacías 
vacia1 = [] 
vacia2 = list() 
print(vacia1) 
print(vacia2) 
"""
    >> [] [] 
""" 
# • Podemos crear listas vacías
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Resumiendo 
# Definiendo listas 

# • Listas como secuencias de elementos ordenados, de cualquier tipo 
# • Definición de listas: tipo list 
# • Listas vacías, y listas de listas