
# Bienvenida

print("Bienvenido a ... ")
print("""
              _                  __   _________                _____                  __     
   ____ ___  (_)  ________  ____/ /  /___  ___/_________  ____/ ___/_____(_)___  ____/ /_____
  / __ `__ \/ /  / ___/ _ \/ __  /      / /   / __  /___`´___/ __/ / ___/ / __ \/ __  /_____/
 / / / / / / /  / /  /  __/ /_/ /      / /   / /_/ /   / /  / /   / /  / /  ___/ /_/ /____ /
/_/ /_/ /_/_/  /_/   \___/\__,_/      /_/   /_____/   /_/  /_/   /_/  /_/\____/\__,_/_____/  
              
""")

# Ejercicio 1: Modificación del programa para que termine únicamente cuando se ingresa "N" o "n"
# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

# Cálculo de edad
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2024-agno-1
print()

# Cálculo de estatura
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

# Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

# Ejercicio 2: Modificación del menú para permitir al usuario realizar más de una acción
# Usaremos una variable bool para indicar si el usuario desea continuar utilizando el programa o no
# Este ciclo se mantiene en ejecución hasta que el usuario desee salir
continuar = True
while continuar:
    # Solicitamos opción al usuario
    print("¿Qué acción deseas realizar?")
    print("1. Escribir un mensaje")
    print("2. Modificar nombre")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la acción que desea realizar: ")

    if opcion == "1":
        # Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
        escribir_mensaje = input("¿Deseas escribir un mensaje? (S/N) ")
        if escribir_mensaje.lower() == "s" or escribir_mensaje == "":
            mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
            print()
            print("--------------------------------------------------")
            print(nombre, "dice:", mensaje)
            print("--------------------------------------------------")
        elif escribir_mensaje.lower() == "n":
            continuar = False
        else:
            print("Opción inválida. Por favor, ingresa 'S' para escribir un mensaje o 'N' para salir.")
    elif opcion == "2":
        nuevo_nombre = input("Ingrese su nuevo nombre: ")
        nombre = nuevo_nombre
        print("Tu nombre se ha actualizado a:", nombre)
    elif opcion == "3":
        continuar = False
    else:
        print("Opción inválida. Por favor, ingresa un número válido.")

# Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")



#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opción al usuario.
#
#2. Modifica este menú para que le permita el usuario realizar más de una acción.
#   Por ejemplo, puedes agregar una acción que permita al usuario modificar su nombre.


























