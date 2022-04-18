import re

#1
def caracter_permitido(string):
    return bool(re.search("[A-Za-z0-9]", string))
print(caracter_permitido("."))

#2
def caracter_permitido2(string):
    return bool(re.findall("[A-Za-z0-9]", string))
print(caracter_permitido2("//"))

#3
def condicion_he(string):
    return bool(re.search("he+", string))
print(condicion_he("hefff"))
print(condicion_he("irgfrhoeif"))

def condicion_he_dos_o_tres(string):
    return bool(re.search("he{2,3}", string))
print(condicion_he_dos_o_tres("heeefrgtb"))
print(condicion_he_dos_o_tres("ggghe"))

#4
def guion_bajo(string):
    if re.findall(".*_.*", string) == []:
        return "No hay dos palabras unidas por un _ en el string"
    return re.findall(".*_.*", string)
print(guion_bajo("messi_lionel"))
print(guion_bajo("lalala"))

#5
def empieza_con(string, numero):
    return bool(re.findall(str(numero), string[0:len(str(numero))]))
print(empieza_con("4opjk", 4))
print(empieza_con("4opjk", 2))
print(empieza_con("40opjk", 40))

#6
   
#7
def ej7(string):
    return re.findall("[A-Za-z0-9]", string)
print(ej7("holaKJGKHGJH"))

#8
def numeros(string):
    return re.findall("[0-9]", string)
print(numeros("0ngsdf322f4"))

#9
def guiones(string):
    return re.findall("-(.*?)-", string)
print(guiones("fff -esto- ff  ggrgr-esto tambien-gg"))

#10
def substrings(string):
    return re.search("@(.*?)&", string) or re.search("&(.*?)@", string) 
print(substrings("tomas.scarfo@gmail&.com"))
print(substrings("tomas.scarfo&gmail@.com"))

#11 - ROMPE
"""def letra_p(lista):
    return re.findall("[^p]", lista)
lista111 = ["papa mama", "practica python"]
print(letra_p(lista111))"""
 
 #12
def sustituir(string):
    return re.sub("[_ :]", "|", string)
print(sustituir("tomas_alejandro:scarfo "))

#13
def no_numerico(string):
    return re.sub("\W"[0:2], "_", string,2)
print(no_numerico("///messi__"))

#14
def espacios_y_tab(string):
    return re.sub("[\s\t]", ";", string)
print(espacios_y_tab("espacios y    tabulaciones"))

#15
def correo_electronico(mail):
    return bool(re.findall("[a-z0-9.-_]"+"@"+"[a-z0-9.-_]"+"."+"[a-z]", mail))
print(correo_electronico("tomas.scarfo@gmail.com"))
print(correo_electronico("tomas/scarfo.gmail.com"))
