from Cola import *

class Moto:

    def __init__(self,nombre,codigo,placa):
        self.nombre = nombre
        self.codigo = codigo
        self.placa = placa

cola = Cola()

cola.encolar(Moto("Johan Sebastian Lopez","20142020013","AGZ154"))
cola.encolar(Moto("Oscar Adrian Bautista","20142020213","ABC458"))
cola.encolar(Moto("Andres Felipe Pachon","20142020212","BHS458"))
cola.encolar(Moto("Brayan Alejandro Gomez","2015101025","JKC589"))

print(cola.tamano(),"\n")

while cola.es_vacia() == False:
    moto = cola.desencolar()
    print(cola.tamano(),moto.nombre)
    print("Codigo: ",moto.codigo)
    print("Placa: ",moto.placa)
    print("\n")
