# Mensaje de bienvenida
print("Bienvenido a ... ")
print("""
              _                  __   _________                _____                  __     
   ____ ___  (_)  ________  ____/ /  /___  ___/_________  ____/ ___/_____(_)___  ____/ /_____
  / __ `__ \/ /  / ___/ _ \/ __  /      / /   / __  /___`´___/ __/ / ___/ / __ \/ __  /_____/
 / / / / / / /  / /  /  __/ /_/ /      / /   / /_/ /   / /  / /   / /  / /  ___/ /_/ /____ /
/_/ /_/ /_/_/  /_/   \___/\__,_/      /_/   /_____/   /_/  /_/   /_/  /_/\____/\__,_/_____/  
              
""")

# Función para calcular la edad
def calcular_edad(agno_nacimiento):
    return 2024 - agno_nacimiento

# Función para convertir la estatura a metros y centímetros
def convertir_estatura(estatura):
    metros = int(estatura)
    centimetros = int((estatura - metros) * 100)
    return metros, centimetros

# Función para actualizar el perfil de usuario
def actualizar_perfil():
    nombre = input("Para empezar, dime como te llamas. ")
    print(f"Hola {nombre}, bienvenido a Mi Red ToyFriends")
    print()

    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    edad = calcular_edad(agno)
    print()

    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dimelo en metros. "))
    estatura_m, estatura_cm = convertir_estatura(estatura)
    print()

    num_amigos = int(input("Muy bien. Finalmente, Cuéntame cuántos amigos tienes. "))
    print()

    genero = input("¿Cuál es tu genero? ")
    print()
    
    num_telefono = input("¿Cuál es tu número de teléfono? ")
    print()
    
    ciudad = input("¿En qué ciudad vives? ")
    print()

    pais_nacimiento = input("¿Cuál es tu país de nacimiento? ")
    print()

    #Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
    print()
    print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", edad, "años")
    print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
    print("Amigos:  ", num_amigos)
    print("genero:      ", genero)
    print("Teléfono:  ", num_telefono)
    print("Ciudad:    ", ciudad)
    print("País de nacimiento:    ", pais_nacimiento)
    print("--------------------------------------------------")
    print()
    return nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais_nacimiento

# Mensaje de despedida
def despedida():
    print("Gracias por la información. Esperamos que disfrutes con Mi Red Toy Friends!")

# Función principal
def main():
    nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais_nacimiento = actualizar_perfil()
    mensajes_amigos = {}

    opcion = 1
    while opcion != 0:
        print("Acciones disponibles:")
        print(" 1. Escribir un mensaje público")
        print(" 2. Escribir un mensaje solo a algunos amigos")
        print(" 3. Mostrar los información de perfil")
        print(" 4. Actualizar el perfil de usuario")
        print(" 0. Salir")
        print()
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            mensaje_publico = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
            print()
            print("--------------------------------------------------")
            print(nombre, "dice:", mensaje_publico)
            print("--------------------------------------------------")

        elif opcion == 2:
            for i in range(num_amigos):
                nombre_amigo = input(f"Ingresa el nombre del amigo {i+1}: ")
                mensaje_amigo = input(f"¿Qué mensaje deseas enviar a {nombre_amigo}? ")
                mensajes_amigos[nombre_amigo] = mensaje_amigo
                print("--------------------------------------------------")
                print(nombre, "dice:", "@"+nombre_amigo, mensaje_amigo)
                print("--------------------------------------------------")

        elif opcion == 3:
            print("--------------------------------------------------")
            print("Nombre:  ", nombre)
            print("Edad:    ", edad, "años")
            print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
            print("Amigos:  ", num_amigos)
            print("genero:      ", genero)
            print("Teléfono:  ", num_telefono)
            print("Ciudad:    ", ciudad)
            print("País de nacimiento:    ", pais_nacimiento)
            print(nombre, "dice:", mensaje_publico)
            for amigo, mensaje in mensajes_amigos.items():
                print(f"@{amigo}: {mensaje}")
            print("--------------------------------------------------")
        
        elif opcion == 4:
            nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad = actualizar_perfil()


        elif opcion == 0:
            print("Has decidido salir.")

        else:
            print()
            print("No conozco la opción que has ingresado. Inténtalo otra vez.")
            print()

    despedida()

if __name__ == "__main__":
    main()

