class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si est� vac�a. """

    def __init__(self):
        """ Crea una cola vac�a. """
        # La cola vac�a se representa con una lista vac�a
        self.items = []

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola est� vac�a levanta una excepci�n. """
        try:
            atendido = self.items[0]
            self.items.pop(0)
            return atendido
        except IndexError:
            print
            "La cola esta vacia"

    def es_vacia(self):
        """ Devuelve True si la lista est� vac�a, False si no. """
        return self.items == []

    def tamano(self):
        return len(self.items)