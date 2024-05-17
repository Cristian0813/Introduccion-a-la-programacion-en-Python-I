# FUNCIONES SOBRE LISTAS TIPO LIST

# Funsiones sobre lista
# listaSupermercado.py 

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 

# Objetivo: Conocer funciones útiles sobre listas 

# • ¿Cuántos elementos tiene? 
# • ¿Podemos ordenar sus elementos? 
# • ¿Estará "vino" en la lista? 

#---------------------------------------------------------------------------------------------

#  ¿Cuántos elementos hay? 
# len(lista) Cantidad de elementos de una lista

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
print("Hay", len(no_olvidar), "cosas por comprar") 
no_olvidar.append("jamón") 
print("Hay", len(no_olvidar), "cosas por comprar") 
""" 
    >> Hay 5 cosas por comprar 
    >> Hay 6 cosas por comprar 
"""

#---------------------------------------------------------------------------------------------

# ¿Está este elemento? in 

#elemento in lista ¿Existe elementoen lista
no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
print("¿Debo comprar vino?", ("vino"in no_olvidar)) 
print("¿Debo comprar palta?", ("palta"in no_olvidar)) 

""" 
    >> ¿Debo comprar vino? False 
    >> ¿Debo comprar palta? True
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# ¿Dónde está este elemento? Buscando en una lista 

# lista.index(elemento) 
""" 
no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
print("Lechuga:", no_olvidar.index("lechuga")) 
print("Queso:", no_olvidar.index("queso")) 
    >> Lechuga: 2 
    >> Queso: ValueError: 'queso' isnotin list
"""

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# De stra list Leyendo una lista 

texto = input("Ingrese una lista: ") 
print("Primero :", texto[0]) 
print("No Lista:", texto) 
no_olvidar= [] 
inicio = 0 
for i in range(0,len(texto)): 
    if texto[i] == ",": 
        no_olvidar.append(texto[inicio:i]) 
        inicio = i+1 
no_olvidar.append(texto[inicio:]) 
print("Lista:", no_olvidar) 
""" 
    >> Ingrese una lista: huevos,palta,lechuga,7000
    >> Primero : h 
    >> No Lista: huevos,palta,lechuga,7000 
    >> Lista: ['huevos', 'palta', 'lechuga', '7000']
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# string.split(separador) Conversión de stringa lista 
# • Separa stringen separador y lo guarda en una lista 

texto = input("Ingrese una lista: ") 
no_olvidar= texto.split(",") 
print("Lista:", no_olvidar) 
""" 
    >> Ingrese una lista: huevos,palta,lechuga,7000 
    >> Lista: ['huevos', 'palta', 'lechuga', '7000'] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  De str a list str.split(sep) 

# string.split(separador) 
# • Separa stringen separador y lo guarda en una lista 

texto = input("Ingrese una lista: ") 
no_olvidar= texto.split("a") 
print("Lista:", no_olvidar) 
""" 
    >> Ingrese una lista: huevos,palta,lechuga,7000 
    >> Lista: ['huevos,p', 'lt', ',lechug', ',7000'] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Ordenando una lista list.sort() 

# lista.sort() Ordena el contenido de una lista 
# • Ordena los elementos de una lista

no_olvidar= ["huevos", "palta", "lechuga","naranjas"] 
print("Original:", no_olvidar) 
no_olvidar.sort() 
print("Ordenada:", no_olvidar) 
""" 
    >> Original: ['huevos', 'palta', 'lechuga', 'naranjas'] 
    >> Ordenada: ['huevos', 'lechuga', 'naranjas', 'palta'] 
""" 
print()
print("-------------------------------------------------------------------------------------")
print()

list.sort() 
precios = [1800, 2300, 450, 610] 
print("Original:", precios) 
precios.sort() 
print("Ordenada:", precios) 
""" 
    >> Original: [1800, 2300, 450, 610] 
    >> Ordenada: [450, 610, 1800, 2300] 
""" 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

#  Ordenando listas de listas 

# • Ordena de acuerdo al primer elementoResumiendo Funciones sobre listas 

comprar = [ [1800,"huevos"], [2300,"palta"], [450,"naranjas"], [610,"queso"]] 
print("Original:", comprar) 
comprar.sort() 
print("Ordenada:", comprar)
"""  
    >> Original: [[1800, 'huevos'], [2300, 'palta'], [450, 'naranjas'], [610, 'queso']] 
    >> Ordenada: [[450, 'naranjas'], [610, 'queso'], [1800, 'huevos'], [2300, 'palta']] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Resumiendo
 
# • Longitud de una lista: len 
# • Saber si un elemento existe: in 
# • Conocer posición de elemento index 
# • Separar un string y formar una lista split 
# • Ordenar elementos: sort