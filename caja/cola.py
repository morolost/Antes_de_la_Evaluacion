class Cola:
    def __init__(self):
        self.cola = []
    def encolar(self,e):#poner primero
        self.cola.append(e)
    def desencolar(self):#sacar primero
        x = self.cola.pop(0)
        return x
    def esta_vacio(self):
        return len(self.cola) == 0
    def mostrar_primero(self):
        print(self.cola[0])
    def tamalo(self):
        return(self.cola)