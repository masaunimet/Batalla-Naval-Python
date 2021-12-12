class Usuarios():

    def __init__(self, username, name, edad, genero,puntos):
        
        self.username = username
        self.name = name
        self.edad = edad
        self.genero = genero
        self.puntos = puntos

    #Muestra la informacion del objeto(usuario) 
    def __str__(self):
        return (f"{self.username},{self.name},{self.edad},{self.genero},{self.puntos}")
