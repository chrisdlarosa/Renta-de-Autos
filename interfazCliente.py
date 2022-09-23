import os
from lista import Lista
from cliente import Cliente

class InterfazCliente:

    def __init__(self):
        self.lista=Cliente()
    
    def imprimirMenu(self):
        self.limpiarInterfaz()
        print("==**RENTA DE AUTOS**============================")
        print("==**INTERFAZ DE CLIENTES**======================")
        print("( 1 ) Agregar Cliente")
        print("( 2 ) Eliminar Cliente")
        print("( 3 ) Modificar Cliente")
        print("( 4 ) Imprimir Clientes")
        print("( 5 ) Salir")
        
        opcion = int(input("Opcion: "))
        return opcion

    def interfazAgregarCliente(self):
        self.limpiarInterfaz()
        print("==**Agregar Cliente**============================")
        dni = int(input("DNI: "))
        nombre = str(input("Nombre: "))
        correo = str(input("Correo: "))
        nss = int(input("NSS: "))
        cliente = Cliente(dni, nombre, correo, nss)
        self.lista.agregar(cliente)

    def interfazEliminarCliente(self):
        self.limpiarInterfaz()
        print("==**Eliminar Cliente**============================")
        indice = int(input("Indice de cliente a eliminar: "))
        self.lista.eliminar(indice)

    def interfazModificarCliente(self):
        self.limpiarInterfaz()
        print("==**Modificar Cliente**============================")
        indice = int(input("Indice de cliente a modificar: "))
        dni = int(input("DNI: "))
        nombre = str(input("Nombre: "))
        correo = str(input("Correo: "))
        nss = int(input("NSS: "))
        cliente = Cliente(dni, nombre, correo, nss)
        self.lista.modificar(indice, cliente)

    def interfazImprimirCliente(self):
        self.limpiarInterfaz()
        print("==**Imprimir Clientes**============================")
        cliente=self.lista.getLista() 
        for indice in range(len(cliente)):
            print("---------------------------------------------------")
            print(indice,cliente[indice])
        print("___________________________________________________")
        print("Cantidad: " + str(len(self.lista.getLista())))
        input("Preciona una tecla para continiar....")

    def limpiarInterfaz(self):
        os.system ("clear")

    def menuCliente(self):
        opcion = None
        while opcion != 5:
            opcion = self.imprimirMenu()
            if opcion == 1:
                self.interfazAgregarCliente()
            elif opcion == 2:
                self.interfazEliminarCliente()
            elif opcion == 3:
                self.interfazModificarCliente()
            elif opcion == 4:
                self.interfazImprimirCliente()

#if __name__ == "__main__":
#    interfa =InterfazCliente() 
#    interfa.menuCliente()