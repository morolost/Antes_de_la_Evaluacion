class Pila:
    def __init__(self):
        self.pila = []
    def apilar(self, x):
        self.pila.append(x)
    def desapilar(self):
        self.pila.pop()
    def  esta_vacia(self):
        if len(self.pila) == 0:
            print("esta vacia")
            return None
    def tamaño(self):
        return len(self.pila)