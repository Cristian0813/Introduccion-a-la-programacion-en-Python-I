import RedToyFriends as Red

#Aquí­ empieza el programa principal.
Red.mostrar_bienvenida()
(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais) = Red.obtener_datos()

print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
mensajes_amigos = {}
mensaje_publico = ""
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais, mensaje_publico, mensajes_amigos)
print("Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con Mi Red ToyFriends")
print("--------------------------------------------------")

opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        mensaje_publico = Red.obtener_mensaje()
    elif opcion == 2:
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            mensaje_amigo = Red.obtener_mensaje_amigo(nombre_amigo)
            mensajes_amigos[nombre_amigo] = mensaje_amigo
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais, mensaje_publico, mensajes_amigos)
    elif opcion == 4:
        nombre, edad, (estatura_m, estatura_cm), num_amigos, genero, num_telefono, ciudad, pais = Red.obtener_datos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, num_telefono, ciudad, pais, mensaje_publico, mensajes_amigos)
    elif opcion == 0:
        print("Has decidido salir.")

print("Gracias por usar Mi Red ToyFriends. ¡Hasta pronto!")
