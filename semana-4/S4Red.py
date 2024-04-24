def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __   _________                _____                  __     
       ____ ___  (_)  ________  ____/ /  /___  ___/_________  ____/ ___/_____(_)___  ____/ /_____
      / __ `__ \/ /  / ___/ _ \/ __  /      / /   / __  /___`´___/ __/ / ___/ / __ \/ __  /_____/
     / / / / / / /  / /  /  __/ /_/ /      / /   / /_/ /   / /  / /   / /  / /  ___/ /_/ /____ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/      /_/   /_____/   /_/  /_/   /_/  /_/\____/\__,_/_____/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    print(f"Hola {nombre}, bienvenido a Mi Red ToyFriends")
    print()
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2024-agno-1

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_num_amigos():
    amigos = int(input("Cuéntame cuantos amigos tienes. "))
    return amigos

def obtener_genero():
    genero = input("¿Cuál es tu genero? ")
    return genero

def obtener_num_telefono():
    telefono = int(input("¿Cuál es tu número telefónico? "))
    return telefono

def obtener_ciudad():
    ciudad = input("¿En qué ciudad vives? ")
    return ciudad

def obtener_pais():
    pais = input("Muy bien. Finalmente, ¿Cuál es tu país de nacimiento?. ")
    return pais

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    g = obtener_genero()
    nt = obtener_num_telefono()
    c = obtener_ciudad()
    p = obtener_pais()
    return (n,e,em,ec,na, g, nt, c, p)

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais, mensaje_publico, mensajes_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
    print("Amigos:   ", num_amigos)
    print("Genero:   ", genero)
    print("Teléfono:   ", num_telefono)
    print("Ciudad:   ", ciudad)
    print("Pais:   ", pais)
    print("Mensaje público:")
    if mensaje_publico:
        print(mensaje_publico)
    else:
        print("(No hay mensaje público)")
    print("Mensajes a amigos:")
    if mensajes_amigos:
        for amigo, mensaje in mensajes_amigos.items():
            print(f"@{amigo}: {mensaje}")
    else:
        print("(No hay mensajes para amigos)")
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def obtener_mensaje_amigo(nombre_amigo):
    mensaje_amigo = input(f"¿Qué mensaje quieres enviarle a {nombre_amigo}? ")
    return mensaje_amigo

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")