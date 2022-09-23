from automovil import Automovil
from cliente import Cliente

class Renta:

    def __init__(self, cliente, automovil, precio, dias):
        self.cliente = cliente
        self.automovil = automovil
        self.precio = precio
        self.dias = dias