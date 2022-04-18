#1
from msilib.schema import Class


class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

perro = Perro()
print(perro.comer(100))
print(perro._alimento)
print(perro._caricias)
print(perro.energia())

#2
class Golondrina():
    def __init__(self, energia):
        self.energia = energia

    def volar(self):
        if self.energia <= 0:
            return "No puede volar debido a su energia"
        else:
            self.energia += 10
golondrina = Golondrina(1110)
print(golondrina.volar())

#3
class Notebook():
    def __init__(self, precio):
        self.marca = "HP"
        self.modelo = 2022
        self.precio = precio
    
    def descuento(self, porcentaje):
        return self.precio * (1 - porcentaje / 100)

notebook = Notebook(100)
print(notebook.marca)
print(notebook.precio)
print(notebook.modelo)
print(notebook.descuento(40)) 

#4
class Contador():
    def __init__(self, precio):
        self.precio = precio
    
    def inc(self):
        self.precio += 1
    
    def dis(self):
        self.precio -= 1
    
    def reset(self):
        self.precio = 0
    
    def valorActual(self):
        return self.precio
    
    def valorNuevo(self, nuevo_valor):
        self.precio = nuevo_valor

contador = Contador(10)
print(contador.inc())
print(contador.inc())
print(contador.dis())
print(contador.inc())
print(contador.valorActual())
print(contador.valorNuevo(27))
print(contador.dis())
print(contador.dis())
print(contador.valorActual()) 

#5


#6 
class Calculadora():
    def __init__(self):
        self.numero = 0
    
    def sumar(self, numero):
        self.numero += numero
    
    def restar(self, numero):
        self.numero -= numero
    
    def multiplicar(self, numero):
        self.numero *= numero
    
    def cargar(self, numero):
        self.numero = numero
    
    def valorActual(self):
        return self.numero

calculadora = Calculadora()
print(calculadora.cargar(0))
print(calculadora.sumar(4))
print(calculadora.multiplicar(5))
print(calculadora.restar(8))
print(calculadora.multiplicar(2))
print(calculadora.valorActual())

#7 
"""
class Gorriones():
    def __init__(self):
        self.km = 0
        self.gramos = 0
        self.veces_comio = 0
        self.veces_volo = 0

    def volar(self, km):
        self.volar += km
        self.veces_volo += 1
    
    def comer(self, gramos):
        self.comer = gramos
        self.veces_comio += 1
    
    def css(self):
        return self.km / self.gramos
    
    def cssv(self):
        return self.veces_volo / self.veces_comio
    
gorriones = Gorriones()
print(gorriones.volar(2))
"""





#PRACTICA OBJETOS PARTE 2

#1
"""
INTERFACES: comer, acariciar, pasear (de las cuales comparten comer y acariciar)
ESTADOS: caricias, alimentos
Son polimorficas debido a que saben responder a los mensajes que se les envia
"""

#2
class Golondrina():
    def __init__(self, energia):
        self.energia = energia
    def esta_en_equilibrio(self):
        if 150 <= self.energia <= 300:
            return "Esta en equilibrio"
        else:
            return "NO esta en equilibrio"

#3

#4
class Auto():
    def __init__(self, combustible):
        self.combustible = combustible
    
    def andar(self, kms):
        self.combustible -= kms/2
            
    def cargar_combistible(self, litros):
        self.combustible += litros
    
    def entran(self, cant_personas):
        if 0 <= cant_personas <= 5:
            return True
        else:
            return "El maximo de personas permitidas es 5"

auto = Auto(100)
print(auto.combustible)
print(auto.andar(10))
print(auto.combustible)
print(auto.cargar_combistible(5))
print(auto.combustible)
print(auto.entran(1))

class Moto():
    def __init__(self, combustible):
        self.combustible = combustible
    
    def andar(self, kms):
        self.combustible -= kms
            
    def cargar_combistible(self, litros):
        self.combustible += litros
    
    def entran(self, cant_personas):
        if 0 <= cant_personas <= 2:
            return True
        else:
            return "El maximo de personas permitidas es 2"
moto = Moto(100)
print(moto.combustible)
print(moto.andar(10))
print(moto.combustible)
print(moto.cargar_combistible(5))
print(moto.combustible)
print(moto.entran(3))

