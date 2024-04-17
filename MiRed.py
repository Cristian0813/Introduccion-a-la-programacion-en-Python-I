print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()
# Cálculo de edad
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2024-agno-1
print()
#Tercera interacció. Solicitamos la estatura, medida en metros.
#Utilizamos la conversió a 'int', y una expresió para convertir esto
#a una medida en metros y centÃ­metros
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
#Cuarta interacció. Consultamos cuÃ¡ntos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
# Quinta interacción. Solicitamos el sexo del usuario.
sexo = input("¿Cuál es tu sexo? ")
print()
# Sexta interacción. Solicitamos el número de teléfono del usuario.
numero_telefono = input("¿Cuál es tu número de teléfono? ")
print()
# Séptima interacción. Solicitamos la ciudad donde vive el usuario.
ciudad = input("¿En qué ciudad vives? ")
print()

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("Sexo:      ", sexo)
print("Teléfono:  ", numero_telefono)
print("Ciudad:    ", ciudad)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecución hasta que el usuario desee salir
while continuar:

    #Solicitamos opción al usuario
    print("¿Qué acción deseas realizar?")
    print("1. Escribir un mensaje")
    print("2. Modificar nombre")
    print("3. Salir")
    
    opcion = input("Ingrese el número de la acción que desea realizar: ")

    if opcion == "1":
        #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
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

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")
