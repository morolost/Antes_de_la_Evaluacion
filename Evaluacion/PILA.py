class Pila:
    
    def __init__(self):
        self.pila = []
        
    def apilar(self,x):
        self.pila.append(x)
        
    def pila_vacia(self):
        return len(self.pila) == 0
    
    def desapilar(self):
        self.pila.pop()
        