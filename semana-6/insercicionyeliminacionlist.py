# INSERCIÓN Y ELIMINACIÓN TIPO LIST

# Modificando la lista 
# Lista son mutables

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000, "apio"]

# Objetivo: Modificar la composición de una lista 
# • Listas son mutables (no como str) 
# • Agregar elementos 
# • Eliminar elementos 

print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------


# Operadores sobre listas 
# Concatenación y repetición 

# • Podemos concatenar listas (+) 
# • Podemos repetir listas (*) 

no_olvidar = ["huevos", "palta", "lechuga", "naranjas", 7000] 
tambien = ["apio", "tomates"] 
no_olvidar = no_olvidar+ tambien 
print(no_olvidar) 
print(tambien* 2) 
"""
    >> ['huevos', 'palta', 'lechuga', 'naranjas', 7000, 'apio', 'tomates'] 
    >> ['apio', 'tomates', 'apio', 'tomates'] 
"""

# • No modifica la lista, sino crea una nueva 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Agregar al final de la lista list.append(elem) 

# lista.append(elemento) 
# • Agrega elemento al final de lista 

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar.append("apio") 
print(no_olvidar) 
""" 
    >> ['huevos', 'palta', 'lechuga', 'naranjas', 7000, 'apio'] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# no_olvidar
#    ┌──────────┬─────────┬───────────┬────────────┬──────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │
#    └──────────┴─────────┴───────────┴────────────┴──────┘
#        [0]        [1]          [2]        [3]       [4] 

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar.append("apio") 
print(no_olvidar[5]) 
""" 
    >> apio
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Agregar todos los elementos lista.extend(list) 

# no_olvidar                                                  [0]     [1]  
#    ┌──────────┬─────────┬───────────┬────────────┬──────┬────┴───────┴─────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │ "apio" "tomates" │ 
#    └──────────┴─────────┴───────────┴────────────┴──────┴──────────────────┘
#        [0]        [1]          [2]        [3]       [4]         [5]  


no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar.append(["apio", "tomates"]) 
print(no_olvidar) 
print(no_olvidar[5])
""" 
    >> ['huevos', 'palta', 'lechuga', 'naranjas', 7000, ['apio', 'tomates']] 
    >> ['apio', 'tomates'] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()


# no_olvidar                                                                    
#    ┌──────────┬─────────┬───────────┬────────────┬──────┬────────┬───────────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │ "apio" │ "tomates" │
#    └──────────┴─────────┴───────────┴────────────┴──────┴────────┴───────────┘
#        [0]        [1]          [2]        [3]       [4]     [5]       [6]      

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar.extend(["apio", "tomates"]) 
print(no_olvidar) 
print(no_olvidar[5])
""" 
    >> ['huevos', 'palta', 'lechuga', 'naranjas', 7000, ['apio', 'tomates']] 
    >> ['apio', 'tomates'] 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Agregar en cualquier posición 
# list.insert(index,elem) 

# lista.insert(index, elemento) 
# • Agrega elemento en la posición index

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar.insert(2, 5000) 
print(no_olvidar) 
print(no_olvidar[2])
""" 
    >> ['huevos', 'palta', 5000, 'lechuga', 'naranjas', 7000] 
    >> 5000 
"""
print()
print("-------------------------------------------------------------------------------------")
print()


# no_olvidar                                                                    
#    ┌──────────┬─────────┬──────┬───────────┬────────────┬──────┐
#    │ "huevos" │ "palta" │ 5000 │ "lechuga" │ "naranjas" │ 7000 │
#    └──────────┴─────────┴──────┴───────────┴────────────┴──────┘
#        [0]        [1]     [2]       [3]         [4]        [5]      


no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
no_olvidar.insert(2, 5000) 
print(no_olvidar) 
print(no_olvidar[3])
""" 
    >> ['huevos', 'palta', 5000, 'lechuga', 'naranjas', 7000] 
    >> lechuga
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Sacar el primer elemento 
# list.pop() 

# • Elimina y retorna el primer elemento

# no_olvidar                                                                    
#    ┌──────────┬─────────┬───────────┬────────────┬──────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │
#    └──────────┴─────────┴───────────┴────────────┴──────┘
#        [0]        [1]        [2]          [3]      [4]         

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
comprado = no_olvidar.pop() 
print(no_olvidar) 
print("Ya compré: ", comprado)
""" 
    >> ['palta', 'lechuga', 'naranjas', 7000] 
    >> Ya compré huevos 
""" 
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Sacar de cualquier posición 
# list.remove(index) 

# • Elimina y retorna elemento de la posición index 

# no_olvidar                                                                    
#    ┌──────────┬─────────┬───────────┬────────────┬──────┐
#    │ "huevos" │ "palta" │ "lechuga" │ "naranjas" │ 7000 │
#    └──────────┴─────────┴───────────┴────────────┴──────┘
#        [0]        [1]        [2]          [3]      [4] 

no_olvidar= ["huevos", "palta", "lechuga", "naranjas", 7000] 
comprado = no_olvidar.remove(3) 
print(no_olvidar) 
print("Ya compré: ", comprado)
""" 
    >> ['huevos', 'palta', 'lechuga', 7000] 
    >> Ya compré naranjas lista.remove(index) 
"""
print()
print("-------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------

# Resumiendo 
# Modificando el contenido de la lista 

# • Operadores sobre listas: +, * 
# • Agregar elementos append, extend, insert 
# • Eliminar elementos pop, remove