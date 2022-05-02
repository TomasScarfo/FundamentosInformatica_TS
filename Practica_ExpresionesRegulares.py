import re

#1
def caracter_permitido(string):
    return bool(re.findall("\w", string))
#print(caracter_permitido("."))
#print(caracter_permitido(".ddd"))

#2
def caracter_permitido2(string):
    resultado = True
    for caracter in string:
        if not bool(re.findall("\w", caracter)):
            return False
        else:
            return resultado
#print(caracter_permitido2("tgtD0gte"))
#print(caracter_permitido2("/rogknetg/"))
#print(caracter_permitido2("**"))

#3
def condicion_una_o_mas(string):
    return bool(re.search("he+", string))
#print(condicion_he("hefff"))
#print(condicion_he("irgfrhoeif"))

def condicion_he_dos_o_tres(string):
    return bool(re.search("he{2,3}", string))
#print(condicion_he_dos_o_tres("heeefrgtb"))
#print(condicion_he_dos_o_tres("ggghe"))

def condicion_ninguna_o_mas(string):
    return bool(re.findall("he*", string))
#print(condicion_ninguna_o_mas("hee"))

#4
def guion_bajo(string):
    return re.findall("\w*_\w*", string)
#print(guion_bajo("mes si_lionel"))
#print(guion_bajo("lalala"))

#5
def empieza_con(string, numero):
    return bool(re.findall(str(numero), string[0:len(str(numero))]))
#print(empieza_con("4opjk", 4))
#print(empieza_con("4opjk", 2))
#print(empieza_con("40opjk", 40))

#6
def ej6(lista_string, frase):
    for string in lista_string:
        resultado = bool(re.findall(string, frase))
    return resultado

print(ej6(["hola", "como", "te"], "hola como va"))

#7
def ej7(string):
    resultado = ""
    lista = re.findall("[\w\s]", string)
    for caracter in lista:
        resultado += caracter
    return resultado

#print(ej7("holaK GKHGJH"))

#8
def numeros(string):
    return re.findall("\d", string)
print(numeros("0ngsdf322f4"))

#9
def guiones(string):
    return re.findall("-(.*?)-", string)
#print(guiones("fff -esto- ff  ggrgr-esto tambien-gg"))

#10
def substrings(string):
    return re.search("(@|&)(.*?)(&|@)", string)
print(substrings("tomas.scarfo@gmail&.com"))
print(substrings("tomas.scarfo&gmail@.com"))
print(substrings("tomas.scarfo&gmail&.com"))
print(substrings("tomas.scarfo@gmail@.com"))

#11
def letra_p(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())
    
print(letra_p(["papa mama", "practica python", "pa ld"]))

 #12
def sustituir(string):
    return re.sub("[_ :]", "|", string)
print(sustituir("tomas_aleja ndro:scarfo "))

#13
def no_numerico(string):
    return re.sub("\W", "_", string, 2)
#print(no_numerico("/dd/messi__"))

#14
def espacios_y_tab(string):
    return re.sub("[\s\t]", ";", string)
print(espacios_y_tab("espacios\sy\ttabulaciones"))

#15
def correo_electronico(mail):
    return bool(re.findall("[\w]+[-_\.]*[\w]+@[a-z]{1,9}(\.[a-z]{2,4}){0,1}", mail))

#print(correo_electronico("toma/s.scarfo@gmail.com"))
#print(correo_electronico("tomas/scarfo.gmail.com"))
#print(correo_electronico("tomas.scarfo@gmaiijjjjjjjjjggggggl.commmmmmmm"))