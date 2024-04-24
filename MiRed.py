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

    sexo = input("¿Cuál es tu sexo? ")
    print()
    
    num_telefono = input("¿Cuál es tu número de teléfono? ")
    print()
    
    ciudad = input("¿En qué ciudad vives? ")
    print()