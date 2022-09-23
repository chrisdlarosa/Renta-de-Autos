class Lista:
    def __init__(self):
        self.lista=[]
    
    def agregar(self, objeto):
        self.lista.append(objeto)
        
    def eliminar(self, indice):
        del self.lista[indice]
    
    def modificar(self, indice, objeto):
        self.lista[indice] = objeto

    def getLista(self):
        return self.lista