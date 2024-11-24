from PILA import Pila
import os

class jenga:
    def __init__(self):
          self.jenga = Pila()
          
    def poner_ficha(self):
        self.jenga.apilar("ficha")
        
    def sacar_ficha(self):
        self.jenga.desapilar()
        
    def mostrar_cantidad(self):
        if not self.jenga:
                print(f"Hay esta cantidad de fichas en la pila: '{len(self.jenga)}'")
        else:
            print("no hay nada en la pila")    
    
    def derrumbe(self):
        if len(self.jenga.pila) == 10:
            os.system("cls")
            print("la torre se a derrumbado")
            

def main():
    torre = jenga()
    e=9
    while e != 0:
        e=int(input("1)poner ficha\n2)sacar ficha\n3)mostrar cantidad de fichas\nQue desea hacer: "))
        if e == 1:
            torre.poner_ficha()
            torre.derrumbe()
        elif e == 2:
            torre.sacar_ficha()
        elif e == 3:
            torre.mostrar_cantidad()
    
if __name__ == "__main__":
    main()
    