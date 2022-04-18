from logging.handlers import QueueListener

#1
def medir(string):
    return len(string)
print(medir("messi"))

#2
def quinta_sexta(string):
    return str.upper(string[4]) + str.upper(string[5])
print(quinta_sexta("messidoro"))

#3
def saludo(nombre, apellido):
    return "¡Hola, " + nombre + " " + apellido + "!"
print(saludo("lionel", "messi"))

#4
def iniciales(nombre, apellido1, apellido2):
    return str.upper(nombre[0] + apellido1[0] + apellido2[0])
print(iniciales("Lionel", "Messi", "Cuccitini"))

#5
def promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3
print(promedio(1, 2, 3))

#6
def minutos(minutos):
    return str(minutos // 60) + " horas " + str(minutos % 60) + " minutos"
print(minutos(150))

#7


#8
respuestas = input("respuesta1: "), input("respuesta2: "), input("respuesta3: ")
nota = 0
for respuesta in respuestas:
    if respuesta == "Correcto":
        nota += 4
    if respuesta == "Incorrecto":
        nota -= 1
    if respuesta == "":
        nota += 0
print(nota)


#EJERCICIO EN GRUPO
costo_total = int(input("costo_total: ")
porcentaje_deposito = 0,25
cantidad_ahorrada = int(input("cantidad_ahorrada: ")
g = 0.04
sueldo_anual = 0
porcentaje_ahorrado = 
