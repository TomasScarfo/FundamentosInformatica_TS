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
