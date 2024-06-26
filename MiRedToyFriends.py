import MiRed as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

if Red.existe_archivo(nombre + ".user"):
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)
else:
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
Red.mostrar_mensaje(nombre, estado)

opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        Red.mostrar_muro(muro)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 5:
        Red.agregar_amigo(amigos)
    elif opcion == 6:
        Red.mostrar_ultimos_estados_amigos(amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ", nombre + ".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro)
        print("Archivo", nombre + ".user", "guardado")

print("Gracias por usar Mi Red. ¡Hasta pronto!")
