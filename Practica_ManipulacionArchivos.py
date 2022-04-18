#1
from re import X


def CuantasNO(archivo, letra):
    suma = 0
    with open(archivo, "r") as f:
        for linea in f.readlines().split("\n"):
            if linea[0] != letra:
                suma += 1
    print(suma)

#2
def imprimir_lineas(archivo, n):
    with open(archivo, "r") as f:
        f.readlines()[:n]

#3
def guardar_lineas(archivo, n):
    lista_de_lineas = []
    with open(archivo, "r") as f:
        for i in f:
            lista_de_lineas.append(i)
    print(lista_de_lineas[-n:])
print(guardar_lineas("bio.txt", 4))

#4
def cantidadPalabras(archivo):
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
    print(len(lista_palabras))
print(cantidadPalabras("bio.txt"))

#5


#6
def removerSaltos(documento1, documento2):
    with open(documento1, "r") as file, open(documento2, "w") as s:
        for line in file.read():
            s.write(line.strip("\n"))
print(removerSaltos("bio.txt", "miarch2.txt"))

#7
def palabra_mas_larga(documento):
    palabra = ""
    longitud_max = 0
    with open(documento, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > longitud_max:
                longitud_max = len(word)
                palabra = word
    return palabra, longitud_max

#8
def unir_archivos(doc1, doc2, doc3):
    with open(doc1, "r") as f1, open(doc2, "r") as f2, open(doc3, "a") as f3:
        f3.write(doc1.read() + doc2.read())
    print(unir_archivos("documento1", "documento2", "documento3"))

#9
def FrecuenciaPalabras(archivo):
    with open(archivo, "r") as f:
        palabras = {}
        for palabra in f.read().split():
            if palabra not in palabras:
                palabras[palabra] = round(1 / len(archivo), 3)
            else:
                palabras[palabra] += round(1 / len(archivo), 3)
        return palabras

#10
import glob
import os
def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as s:
        for f in lista_txt:
            file = open(f, "r")
            s.write(file.read())
            file.close()



with open("bio.txt", "r") as mi_archivotxt:
    mi_archivotxt.read()

#DESAFIO IV

def abrir(archivo):
    with open(archivo, "r") as my_file:
        print("manipulacion_archivos.txt".read())

bio = open("bio.txt", "r")
bio.read()



def check_int_type(X):
    try:
        type(X)  == str()
    except:
        TypeError("Only strings are allowed")

print(check_int_type(4))