from lista import Lista

class Cliente(Lista):
    dni = int
    nombre = str
    correo = str
    nss = int

    def __init__(self, dni="", nombre="", correo="", nss=""):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.nss = nss
        self.lista = []

    def __str__(self):
        return (str(self.dni) + " | " + self.nombre + " | " + self.correo + " | " + str(self.nss))