import os
from lista import Lista
from automovil import Automovil

class InterfazAutomovil:

    def __init__(self):
        self.lista = Automovil()
    
    def imprimirMenu(self):
        self.limpiarInterfaz()
        print("==**RENTA DE AUTOS**============================")
        print("==**INTERFAZ DE AUTOMOVIL**======================")
        print("( 1 ) Agregar Automovil")
        print("( 2 ) Eliminar Automovil")
        print("( 3 ) Modificar Automovil")
        print("( 4 ) Imprimir Automoviles")
        print("( 5 ) Salir")
        
        opcion = int(input("Opcion: "))
        return opcion

    def interfazAgregarAutomovil(self):
        self.limpiarInterfaz()
        print("==**Agregar Automovil**============================")
        serie = int(input("Serie: "))
        fabricante = str(input("Fabricane: "))
        modelo = str(input("Modelo: "))
        ano = int(input("Año: "))
        color = str(input("Color: "))
        automovil = Automovil(serie, fabricante, modelo, ano, color)
        self.lista.agregar(automovil)

    def interfazEliminarAutomovil(self):
        self.limpiarInterfaz()
        print("==**Eliminar Automovil**============================")
        indice = int(input("Indice de automovil a eliminar: "))
        self.lista.eliminar(indice)

    def interfazModificarAutomovil(self):
        self.limpiarInterfaz()
        print("==**Modificar Automovil**============================")
        indice = int(input("Indice de automovil a modificar: "))
        serie = int(input("Serie: "))
        fabricante = str(input("Fabricane: "))
        modelo = str(input("Modelo: "))
        ano = int(input("Año: "))
        color = str(input("Color: "))
        automovil = Automovil(serie, fabricante, modelo, ano, color)
        self.lista.modificar(indice, automovil)

    def interfazImprimirAutomovil(self):
        self.limpiarInterfaz()
        print("==**Imprimir Automovil**============================")
        automovil=self.lista.getLista() 
        for indice in range(len(automovil)):
            print("---------------------------------------------------")
            print(indice,automovil[indice])
        print("___________________________________________________")
        print("Cantidad: " + str(len(self.lista.getLista())))
        input("Preciona una tecla para continiar....")

    def limpiarInterfaz(self):
        os.system ("clear")

    def menuAutomovil(self):
        opcion = None
        while opcion != 5:
            opcion = self.imprimirMenu()
            if opcion == 1:
                self.interfazAgregarAutomovil()
            elif opcion == 2:
                self.interfazEliminarAutomovil()
            elif opcion == 3:
                self.interfazModificarAutomovil()
            elif opcion == 4:
                self.interfazImprimirAutomovil()

if __name__ == "__main__":
    interfa =InterfazAutomovil() 
    interfa.menuAutomovil()