class Vehiculos_marinos():

    def __init__(self, tamaño,ejex,ejey):

        self.tamaño = tamaño
        self.ejex = ejex
        self.ejey = ejey

class Buque(Vehiculos_marinos):

    def __init__(self,tamaño,ejex,ejey,lado):

        super().__init__(tamaño,ejex,ejey)
        self.lado = lado

    def info(self):

        return("tiene la capacidad de aterrizar helicópteros")

class Barco(Vehiculos_marinos):

    def __init__(self,tamaño,ejex,ejey,lado):

        super().__init__(tamaño,ejex,ejey)
        self.lado = lado

    def info(self):

        return("tiene la capacidad de comunicarse con tierra y los otros miembros de la flota")

class Submarino(Vehiculos_marinos):

    def __init__(self,tamaño,ejex,ejey):

        super().__init__(tamaño,ejex,ejey)

    def info(self):

        return("tienen la capacidad de poder sumergirse y emerger del agua")