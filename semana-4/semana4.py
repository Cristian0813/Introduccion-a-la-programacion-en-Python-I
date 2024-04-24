# REUTILIZANDO CÓDIGO 
# Funciones 
# Aprendiendo	a	programar	con	Python


# Pregunta
# A continuación tienen un código que convierte los segundos que tarda un estudiante en ir a la universidad, 
# estar en la universidad, y volver de la universidad, a horas, minutos y segundos 
# ¿Cuantos errores eres capaz de identificar en este código?

""" #Ida
ida = int(input("IDA en segundos: "))
ida_h = ida // 3600
resto_ida = ida % 3600
ida_m = resto_ida // 60
ida_s = resto_ida % 60
print("IDA:",ida_h,"(h)",ida_m,"(m)",ida_s,"(s)") 
#Uni
uni = int(input("UNI en segundos: "))
uni_h = uni // 3600
resto_uni = uni % 3600
uni_m = resto_uni // 60
uni_s = resto_uni % 60
print("UNI:",uni_h,"(h)",uni_m,"(m)",uni_s,"(s)") 
#Vuelta
vuelta = int(input("VUELTA en segundos: "))
vuelta_h = vuelta // 3600
resto_vuelta = vuelta % 3600
vuelta_m = resto_vuelta // 60
vuelta_s = resto_vuelta % 60
print("VUELTA:",vuelta_h,"(h)",vuelta_m,"(m)",vuelta_s,"(s)") 
 """
# 1
# 3
# 0
# (x) 2
# Correcto
#   Efectivamente, hay 2 errores probablemente resultado de cortar-y-pegar el código 3 veces: 1) 
#   la línea 11 debería ser uni % 3600 y no ida % 3600, y 2) en la línea 18 debería ser 3600 y no 360


def mcd(n1,n2):
    while n2:
        n1, n2 =n2, n1 % n2
    return n1

resultado = mcd(10,15)
print("El maximo común divisor es: ", resultado)


def exponente(n):
    exp = 0
    while 2 ** exp <= n:
        exp += 1
    return exp - 1

numero = 65
resultado = exponente(numero)
print("El número {} tiene una base 2 exponencial de {}" .format(numero,exponente(numero)))





def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return False
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def panprimo(n):
    digitos = set(str(n))
    if len(digitos) !=10:
        return False
    ultimos_tres = n % 1000
    if es_primo(ultimos_tres):
        return True
    else:
        return False

print(panprimo(2424643))        
print(panprimo(1234567890))     
print(panprimo(10123485769)) 