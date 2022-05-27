#1
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
"""
perro = Perro()
print(perro.comer(100))
print(perro._alimento)
print(perro._caricias)
print(perro.energia())
print(perro.energia)
print(perro.energia())"""

#2
class Golondrina():
    def __init__(self, energia):
        self.energia = energia

    def volar(self):
        if self.energia <= 0:
            return "No puede volar debido a su energia"
        else:
            self.energia += 10
#golondrina = Golondrina(1110)
#print(golondrina.volar())

#3
class Notebook():
    def __init__(self, precio):
        self.marca = "HP"
        self.modelo = 2022
        self.precio = precio
    
    def descuento(self, porcentaje):
        return self.precio * (1 - porcentaje / 100)
"""
notebook = Notebook(100)
print(notebook.marca)
print(notebook.precio)
print(notebook.modelo)
print(notebook.descuento(40)) """

#4
class Contador():
    def __init__(self, precio):
        self.precio = precio
        self.ultimo = ""
    
    def inc(self):
        self.precio += 1
        self.ultimo = "Incremento"
    
    def dis(self):
        self.precio -= 1
        self.ultimo = "Disminucion"
    
    def reset(self):
        self.precio = 0
        self.ultimo = "Reset"
    
    def valorActual(self):
        return self.precio
    
    def valorNuevo(self, nuevo_valor):
        self.precio = nuevo_valor
        self.ultimo = "Actualizacion"
    
    def ultimoComando(self):
        return self.ultimo

contador = Contador(10)
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.inc()
contador.inc()
print(contador.ultimoComando())
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

"""calculadora = Calculadora()
print(calculadora.cargar(0))
print(calculadora.sumar(4))
print(calculadora.multiplicar(5))
print(calculadora.restar(8))
print(calculadora.multiplicar(2))
print(calculadora.valorActual())"""

#7 

class Gorrion:
    def __init__(self):
        self.km = 0
        self.gramos = 0
        self.listakm = []
        self.listagramos = []

    def volar(self, km):
        self.km += km
        self.listakm.append(km)
                    
    def comer(self, gramos):
        self.gramos += gramos
        self.listagramos.append(gramos)
    
    def css(self):
        if self.gramos > 0:
            return self.km / self.gramos
        else:
            return None
    
    def cssv(self):
        return len(self.listakm) / len(self.listagramos)
    
    def cssp(self):
        return max(self.listakm) / max(self.listagramos)
    
    def equilibrio(self):
        return 0.5 <= self.css() <= 2

"""  
pepe = Gorrion()
print("css, cssp, cssv: ")
print(pepe.volar(10))
print(pepe.volar(6))
print(pepe.comer(1))
print(pepe.comer(2))
print("css")
print(pepe.css())
print("cssv")
print(pepe.cssv())
print("cssp")
print(pepe.cssp())
print(pepe.equilibrio())"""


#PRACTICA OBJETOS PARTE 2

#1

# INTERFACES: comer, acariciar, pasear (de las cuales comparten comer y acariciar)
# ESTADOS: caricias, alimentos
# NO son polimorficas debido a que falta un objeto que les de ordenes/mensajes



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
class Ornitologo():
    def __init__(self):
        self.aves = []
#Aves que va a entrenar
    def estudiarAve(self, ave):
        self.aves.append(ave)
#Agrega el ave que va a estudiar a la lista    
    def avesEnEstudio(self):
        return self.aves
#Dice que aves esta estudiando
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            self.ave.comer(80)
            self.ave.volar(70)
            self.ave.comer(10)

    def avesEnEquilibrio(self):
        EnEquilibrio = []
        for ave in self.aves:
            if self.ave.equilibrio:
                EnEquilibrio.append(ave)
        return EnEquilibrio                
#4
class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible
              
    def cargar_combistible(self, litros):
        self.combustible += litros
    
    def combustible_actual(self):
        return self.combustible
    
    def entran(self, personas):
        return personas <= self.maxPasajeros()

class Auto(MedioDeTransporte):
    def recorrer(self, kms):
        self.combustible -= kms/2

    def maxPasajeros(self):
        return 5

class Moto(MedioDeTransporte):
    def recorrer(self, kms):
        self.combustible -= kms

    def maxPasajeros(self):
        return 2
"""
print("auto:")
auto = Auto(100)
print(auto.combustible)
print(auto.recorrer(10))
print(auto.combustible)
print(auto.cargar_combistible(5))
print(auto.combustible)
print(auto.entran(1))
print(auto.entran(6))

print("moto:")
moto = Moto(100)
print(moto.combustible)
print(moto.recorrer(10))
print(moto.combustible)
print(moto.cargar_combistible(5))
print(moto.combustible)
print(moto.entran(2))
print(moto.entran(3))"""


# EJERCICIO PARCIAL

class Persona:
    def __init__(self, energia):
        self.energia = energia
        self.feliz = False
    
    def energia(self):
        return self.energia

    def dormir(self, horas):
        if horas >= 8:
            self.energia = 100
        elif (self.energia + 12.5 * horas) <= 100:
            self.energia = 100
        else:
            self.energia += (12.5 * horas)

    def comer(self):
        self.energia += 10
    
    def hacerEjercicio(self, minutos):
        self.energia -= (minutos * 25) / 30

class Estudiante(Persona):
    def estudiar(self, horas):
        self.energia -= (horas * 20)
    
    def aprobo(self):
        self.estadoDeAnimo = True
        return True
"""
estudiante = Estudiante(100)
estudiante.hacerEjercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobo())
print(estudiante.energia)"""