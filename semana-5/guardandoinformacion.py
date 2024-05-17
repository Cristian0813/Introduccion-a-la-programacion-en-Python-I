# GUARDANDO INFORMACIÓN 

# Escribir archivo escritura.write() 

# ● Para escribir en un archivo, se ene que haber abierto en modo "w" 
# ● Cuidado: si el archivo existe, se borrará para crear uno nuevo 
# ● Para escribir algo se ocupa el método write(), pasando como parámetro el string que se quiere escribir 

escritura = open("archivo.txt", "w") 
escritura.write("Esto se escribe en el archivo")

# ● Para escribir más líneas, se deben indicar los "saltos de línea" mediante el símbolo "\n" 

escritura.write("Uno \nDos \nTres") 
 
#---------------------------------------------------------------------------------------------------

# Cerrar archivo archivo.close() 

# ● Similar a la función open, existe la función close 
# ● Esta debe llamarse una vez terminado lo que queríamos hacer  
""" archivo.close()  """

#---------------------------------------------------------------------------------------------------

# Importancia close archivo.close() 

# ● Esta función permite que el archivo se guarde correctamente 
# ● Y permite también que el programa siga funcionando sin problemas 

#---------------------------------------------------------------------------------------------------

# Ejemplo

# Abrir el archivo en modo de escritura ('w')
escritura = open("nuevo_nombre.txt", "w")
# Escribir en el archivo
escritura.write("Esto se escribe en el archivo\n")
escritura.write("Uno\nDos\nTres\n")
# Cerrar el archivo
escritura.close()

