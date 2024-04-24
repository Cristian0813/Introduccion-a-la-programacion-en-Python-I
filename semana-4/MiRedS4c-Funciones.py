#Finalmente, podemos ver que nuestro archivo es cada vez mÃ¡s grande.

#Vamos a crear un nuevo archivo .py y copiaremos en Ã©l todas las funciones que hemos definido.
#Llamaremos a este archivo S4Red.py. Luego, para poder utilizar estas funciones dentro de nuestro archivo
#principal, utilizaremos la instrucciÃ³n import.


import S4Red as Red

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


#Como puedes ver, la parte principal de tu programa ahora es mucho mÃ¡s corto.
#Gran parte de la funcionalidad estÃ¡ encapsulada en funciones, y estas funciones estÃ¡n definidas
# en otro archivo que hemos importado.

#Al usar funciones podemos concentrarnos en partes mÃ¡s especÃ­ficas de nuestro cÃ³digo,
# y nos ayuda a razonar a un nivel mÃ¡s alto.
