from lista import Lista

class Automovil(Lista):
    serie = int
    fabricante = str
    modelo = str
    ano = int
    color = str

    def __init__(self, serie="", fabricante="", modelo="", ano="", color=""):
        self.serie = serie
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.color = color
        self.lista = []

    def __str__(self):
        return (str(self.serie) + " | " + self.fabricante + " | " + self.modelo + " | " + str(self.ano) + " | " + self.color)