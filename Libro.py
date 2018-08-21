from Pila import *

class Libro:
	
    def __init__(self,nombre,cat,autor):
        self.nombre=nombre
        self.cat=cat
        self.autor=autor

pila = Pila()

pila.apilar(Libro("El Cartero de los Suenos"," Infantil","Laura Gallego"))
pila.apilar(Libro("Un fantasma en apuros"," Infantil","Laura Gallego"))
pila.apilar(Libro("Max ya no hace reir"," Infantil","Laura Gallego"))
pila.apilar(Libro("Donde esta  Alba?"," Infantil","Laura Gallego"))
pila.apilar(Libro("Alba tiene una amiga muy especial"," Infantil","Laura Gallego"))
pila.apilar(Libro("Por una rosa","Relatos","Laura Gallego"))
pila.apilar(Libro("Manana todavia. ","Relatos","Laura Gallego"))

print("La pila tiene ", pila.tamano(), " libros \n")

while pila.es_vacia() == False:
    Libro = pila.desapilar()
    print(pila.tamano()+1,")",Libro.nombre)
    print("Categoria: ",Libro.cat)
    print("Autor: ",Libro.autor)
    print("\n")